APIX defines a modern, event‑driven interaction model for regulatory communication. The following illustrates key details of the Regulator-Applicant Exchange

---

### **Overview of the Interaction Pattern**

At its core, the APIX pattern is a structured conversation between an **Applicant** and a **Regulator**, expressed entirely through **FHIR Tasks**, **FHIR Endpoints**, **FHIR Organizations**, **SubscriptionTopics**, and **Subscriptions**.

1. Applicant submits a request using a Task, placing their request documentation in Task.input. 
2. A Subscription is created that subscribes the Applicant to updates of the Task. 
3. Regulator accepts the Task (changing status to 'accept') and begins processing.  
4. Applicant receives notification of Task status change.
5. A Subscription is created that subscribes the Applicant to Tasks created where the `Task.owner` is the Applicant.
6. Regulator issues follow‑up Tasks to the Applicant, placing the instructions or questions into `Task.input`. 
7. Applicant receives notification of Task creation.
8. Applicant completes Tasks and provides evidence in `Task.output`.  
9. Regulator continues issuing Tasks until satisfied.  
10. Regulator completes the original Task, indicating completion by changing `Task.status` of the original Task to complete and providing documentation or a final response in `Task.output`.
11. Applicant receives a final notification and retrieves the response from the Task.

This creates a **real‑time, traceable, lineage‑preserving conversation**—all driven by FHIR R5 Subscriptions.

#### **Simplified Illustration of Interaction Pattern**

<img src="oversimplifiedTransactionPattern.svg" alt="Simplified Illustration of Interaction Pattern" style="max-width: 100%; height: auto;">

---

### **Detailed Interaction Pattern**

#### **Starting Assumptions**

The Regulator:

- Operates an **R5‑compliant FHIR server** with full support for:
  - `SubscriptionTopic`
  - `Subscription`
  - sending REST‑hook notifications
- Has created:
  - A **FHIR Organization** representing the Regulatory agency  
  - A **FHIR Endpoint** for the Regulator to receive notifications  
- Has published **SubscriptionTopics** for:
  - `Task.status` updates filterable by `Task.identifier` [Example](SubscriptionTopic-TaskStatusChangeWithIdentifierFilter.html)
  - Task creation filterable by `Task.owner` [Example](SubscriptionTopic-TaskCreationWithOrganizationAssignedFilter.html)

Optional regulator‑side Subscriptions may monitor:

- Task creation where `Task.owner = null`
- Task creation where `Task.owner = Regulator`
- Task status where `Task.requester = Regulator`

---

#### **Applicant Registration & Authorization**

The Applicant:

- Obtains authorization to the Regulator’s FHIR server (e.g., SMART‑on‑FHIR).
- Registers:
  - A **FHIR Organization** for the Applicant organization [Organization example](Organization-1002.html)
  - A **FHIR Endpoint** for receiving notifications  [Endpoint example](Endpoint-1003.html)
- Operates under access rules ensuring:
  - They may update only Tasks where they are `Task.owner`
  - They may only view Tasks where they are `Task.owner` or `Task.requestor`

Access rules ensure **security**, **privacy**, and **role‑appropriate visibility**.

---

#### **Applicant Submits the Initial Task**

The Applicant prepares a Task with:

- `Task.requester = Applicant FHIR Organization instance`
- `Task.identifier =` globally unique identifier to be used to filter the Task status update Subscription. `Task.identifier` includes an identifier (system, value pair) known to the Applicant Organization and is unique. (There is an alternative where `Task.id` is used but this requires discussion in testing. A `Task.identifier` is globally unique, whereas `Task.id` is locally unique to a specific FHIR server. The Applicant will benefit from having this identifier available for connecting their internal data with the FHIR server data. And, importantly, the `Task.id` is not known when the Task is created. However, the Applicant can create a Subscription at the same time as the Task that is filtered by a `Task.identifier`. This is an area where FHIR offers us different business perspectives, but the pattern of having a Task and Subscription to that specific `Task.status` is key.)
- `Task.status` = requested`
- `Task.code =` type of request
- `Task.requestedPerformer = Regulator FHIR Organization`
- `Task.owner = Regulator Organization` *(optional)*
- `Task.input =` documentation or materials supporting the request (see [Post-then-Link](architecture.html#binary-upload-guide-post-then-link) for detials on use of DocumentReference)

The Task is posted to the Regulator’s FHIR server.

---

#### **Applicant (or Regulator's system) Creates a Subscription for Status Updates**

To receive real‑time updates, the Applicant (or Regulator's system) creates a Subscription [Example](Subscription-Subscription-TaskStatusChange-FullResource.html):

- `Subscription.topic =` Task‑status SubscriptionTopic URL  
- `Subscription.filter_by =` the Task’s identifier  
- `Subscription.endpoint =` Applicant’s Endpoint which contains the Endpoint.address from the Applicant Endpoint FHIR Resource created at registration
- `Subscription.managingEntity =` Applicant Organization  
- `Subscription.content = full-resource` or `id-only`
    The choice here is based on business agreements. A Regulator and/or Applicant may wish to keep the size of the notifications smaller (not include the entire Task). This would be choosing the id_only option, and would require the retrieval of the Task subsequent to receiving the notification. With the entire_resource option, the recipient receives the entire Task in its current state, along with the notification. 

A second Subscription is created for **Task creation** by the Regulator where:

- `Task.owner = Applicant`

This ensures the Applicant is notified whenever the Regulator assigns them new work. It is useful to have this Subscription created concurrenlty with the Task (thus use of Task.identifier for filtering).

---

#### **Regulator Accepts the Task**

The Regulator updates:

`Task.status = accepted`

This triggers the Applicant’s Subscription for Task status updates filtered by the `Task.identifier`, generating a **SubscriptionNotification** [Example](Bundle-eee72492-c236-41f7-a7ba-3af356204f4c.html).

The Applicant now knows the request has been received and accepted.

---

#### **Regulator Issues Follow‑Up Tasks**

To request additional work, the Regulator creates a Task:

- `Task.owner = Applicant`
- `Task.requestor = Regulator`
- `Task.status = requested`
- `Task.input =` instructions, questions, or required documentation
- `Task.basedOn =` lineage of previous Tasks  
  - The Applicant’s original Task appears last (direct parent). The basedOn element is an ordered array, the array element order should not be changed when represented in XML, see [R5 Base FHIR specification](https://hl7.org/fhir/R5/resource-formats.html#comparison).

Posting this Task triggers the **Task‑creation Subscription** filtered by Task.owner = Applicant Organization.

The Applicant receives a SubscriptionNotification at the endpoint used in the Subscription, and then retrieves the Task and processes it. Note: the Subscription can be set to either send the id only or the entire Resource. The Applicant retrieves the Task from the notifications and parses it, paying particular attention to the artifacts in Task.input. The input, description, code and potentially other fields help direct the Applicant as to what action they need to take. 

---

#### **Applicant Completes Assigned Tasks**

After performing the requested action, the Applicant:

- Updates `Task.status = completed`
- Adds evidence or responses in `Task.output`
    - e.g. If the Task from the Regulator requested invoice payment, then the Applicant pays out of band and provides a receipt of payment in the output and updates the status to complete.

The Regulator reviews the output and either:

- Accepts it, or  
- Creates a new Task requesting corrections or additional work.

This iterative loop continues until all requirements are satisfied. Depending on the evolution of the business use there may be branches of Tasks and groups of Tasks. However, the essential pattern of Task based request with input and output and status is expected to be used.

---

#### **Regulator Completes the Original Task**

Once all follow‑up Tasks are resolved, the Regulator:

- Updates the **original** Applicant Task  
- Adds final documentation in `Task.output` 
    - Note: `Task.output` supports references to FHIR Resources, such as DocumentReference. 
- Sets `Task.status = complete`

This triggers the Applicant’s status‑update Subscription, signaling that the entire request is finished, and indicaiting the Task where the final Regulator documentation is found.

---
