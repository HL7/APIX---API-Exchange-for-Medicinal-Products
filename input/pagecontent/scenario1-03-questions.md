## Scenario 1: Questions (Information Request)

This scenario demonstrates a regulatory information request (List of Questions) in the APIX workflow. The regulator sends a List of Questions to the applicant, triggering a clock stop in the review timeline.

### Task Overview

| Element | Value |
|---------|-------|
| **Task ID** | scenario1-03-questions |
| **Task Status** | requested |
| **Business Status** | Clock Stop |
| **Task Code** | information-request |

### Context

After the successful validation of the initial submission, the regulatory review team identifies areas requiring clarification or additional data. The regulator issues a formal List of Questions (LoQ) to the applicant.

### Key Information

- **Timeline**: The applicant typically has 30-60 days to respond, depending on the jurisdiction and procedure type
- **Content**: The LoQ identifies specific sections or information gaps requiring response
- **Business Impact**: The regulatory clock stops upon issuance of the LoQ and restarts upon receipt of an acceptable response

### Next Steps

The applicant will prepare a comprehensive response addressing each question, typically resulting in a "Response to Information Request" task.
