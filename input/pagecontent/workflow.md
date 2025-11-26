# APIX Workflow Using the FHIR Task Resource

## Overview

APIX uses the **HL7 FHIR R5 Task** resource as the primary envelope and workflow coordinator for all regulatory exchanges, fully replacing traditional eCTD folders and gateway submissions with an API-driven, structured, auditable, and real-time process.

A single regulatory procedure (e.g., initial MAA, Type II variation, shelf-life extension, PSUR) is represented by a **set of related Tasks** linked by a common `Task.groupIdentifier` (called **ProcedureID** or **TaskSetID** in APIX).  
Each individual message (initial submission, response to questions, approval letter, etc.) is a separate **Task** instance.

This pattern is directly inspired by:
- Uppsala Monitoring Centre (UMC) IDMP Request & Publish API
- Da Vinci Prior Authorization Support (PAS) workflows
- The simple regulatory scenario discussed in the 2025-11-20 Vulcan meeting notes

## Task State Machine (FHIR R5 Task.status)

APIX uses the standard FHIR R5 **Task Status** value set:  
[http://hl7.org/fhir/ValueSet/task-status](http://hl7.org/fhir/ValueSet/task-status)

| Code               | Display            | Meaning in APIX Regulatory Context                                      |
|--------------------|--------------------|--------------------------------------------------------------------------|
| **draft**          | Draft              | Task created locally by company, not yet submitted                       |
| **requested**      | Requested          | Company has POSTed the Task to the regulator                             |
| **received**       | Received           | Regulator server has received the Task (auto-transition)                 |
| **accepted**       | Accepted           | Gateway/technical validation passed                                      |
| **rejected**       | Rejected           | Fatal validation failure → procedure terminated                          |
| **in-progress**    | In Progress        | Scientific/regulatory assessment ongoing                                 |
| **on-hold**        | On Hold            | Clock stopped – regulator has raised questions                           |
| **completed**      | Completed          | Final positive decision (approval)                                       |
| **cancelled**      | Cancelled          | Company withdraws the procedure                                          |
| **entered-in-error**| Entered in Error  | Rare – Task created by mistake                                           |

> **ready**, **failed** are not used in the core APIX workflow.

### Typical State Transitions in a Regulatory Procedure

| From → To                     | Trigger / Example                                             | Who updates   | Subscription notification sent? |
|-------------------------------|---------------------------------------------------------------|---------------|---------------------------------|
| draft → requested             | Company finalises and POSTs the Task                          | Company       | Yes                             |
| requested → received          | Auto-receipt on regulator server                              | Regulator     | Yes                             |
| received → accepted           | Gateway validation successful                                 | Regulator     | Yes (validation passed)         |
| received → rejected           | Gateway validation fails                                      | Regulator     | Yes (rejection)                 |
| accepted → in-progress        | Assessment team begins review                                 | Regulator     | Yes                             |
| in-progress → on-hold         | Regulator creates child Task with questions                   | Regulator     | Yes (clock-stop)                |
| on-hold → in-progress         | Company responds → regulator restarts clock                   | Regulator     | Yes (clock-restart)             |
| in-progress → completed       | Approval letter issued                                        | Regulator     | Yes (final approval)            |
| any → rejected                | Scientific rejection                                          | Regulator     | Yes                             |
| any → cancelled               | Company withdraws                                             | Company       | Yes                             |

## Full Workflow Example – Shelf-Life Update Variation

1. **Company → Regulator: Initial Submission**  
   - Authenticates via SMART Backend Services  
   - POSTs a Task with:  
     - `code` = `initial-submission` (or national submission-type code)  
     - `groupIdentifier` = new ProcedureID (e.g., `PROC-2025-12345`)  
     - `input` contains revised ePI Bundle, CMC documents, cover letter (all contained)  
   - `status` → **requested**

2. **Regulator Gateway Processing**  
   - Auto-transition → **received** → validation → **accepted** (or **rejected**)  
   - Notification sent via Subscription

3. **Regulator raises Questions**  
   - Creates a **child Task** (`partOf` → original)  
     - `code` = `information-request`  
     - `output` contains Questionnaire / list of questions  
   - Original Task → **on-hold** (`businessStatus` = `clock-stop`)

4. **Company Response**  
   - Creates new Task (`partOf` → original)  
     - `code` = `response-to-questions`  
     - `input` contains answers and supporting documents  
   - Regulator validates → original Task back to **in-progress** (`businessStatus` = `clock-restart`)

5. **Regulator Decision**  
   - Updates Task (or creates final Task)  
     - `output` = approval letter (contained DocumentReference) or rejection  
     - `status` = **completed** or **rejected**

## Subscriptions for Real-Time Notification

APIX **requires** support for the R5 Subscription framework (or R5 backport).

- Companies create a Subscription (during onboarding) with criteria such as:  
  - `Task?groupIdentifier={ProcedureID}`  
  - or broader: `Task?requester={CompanyOrgID}`
- Channel: `rest-hook` (preferred) or `websocket`
- Every meaningful status change triggers an immediate notification (id-only or full-resource payload)

Result: **seconds** instead of weeks for status visibility.

## Required Architecture Components

| Component                  | Minimum Requirement                                                                 | Recommendation                     |
|----------------------------|-------------------------------------------------------------------------------------|------------------------------------|
| FHIR Server (Regulator)    | R5 (or R4 + backports), conditional create/update, Subscriptions, SMART Backend Services | HAPI FHIR, Smile CDR, Azure API for FHIR |
| Authentication             | SMART Backend Services (system/* scopes, JWT)                                       | Mandatory                          |
| Subscriptions              | R5 Backport / R5 native, rest-hook + signed webhook                               | Mandatory for production           |
| Validation Engine          | `$validate` + custom regulatory rules Operation                                    | Integrated gateway                 |
| Audit                      | Provenance resource on every Task update                                            | Mandatory                          |
| Search / Grouping          | Support for `groupIdentifier`, `partOf`, chaining                                   | Essential                          |

## Benefits vs Traditional Gateway/eCTD

- Real-time status & notifications (seconds vs weeks)
- Fully structured, queryable regulatory data
- Built-in audit trail (Provenance)
- Hierarchical question/response workflows via `partOf`
- No PDF mining – direct access to regulator content (e.g., labeling, cmc, Adverse event reporting)
- Seamless integration with company RIM/IDMP systems via standard FHIR APIs

