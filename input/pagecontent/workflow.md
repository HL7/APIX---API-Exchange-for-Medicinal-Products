This page provides a detailed workflow example for a "shelf-life update" scenario, illustrating the process between a Company and a Regulator using APIX Tasks.

### Notification Mechanism
It is important to note that throughout this workflow, the Regulator does not directly "send" messages to the Company. Instead, the Regulator updates the status or content of the `Task` resource on the regulator server. The Company, having subscribed to the Task, receives a notification from the regulator's Subscription service whenever a change occurs.

### Shelf-life Update Workflow

1.  **Company posts a Task to the regulator (Version 1)**
    
The company initiates the process by submitting a task. This submission acts as the initial shelf-life update proposal.
    <br>
**Example:** <a href="Task-scenario1-01-initial-submission.json" target="_blank">JSON Resource</a> | <a href="scenario1-01-initial-submission.html" target="_blank">HTML Action View</a>

**Submission Content:**
    1.  Cover letter
    2.  Application form
    3.  Annotated label
    4.  Clean label
    5.  Pack mockup
    6.  CMC doc #1: Drug Product: Stability Summary and Conclusions
    7.  CMC doc #2: Drug Product: Stability Data
    8.  CMC doc #3: Drug Product: Stability Commitment (if original section needs an update)
    9.  CMC doc #4: Drug Substance: Stability Summary and Conclusions (if any new stability data/ storage period updates)
    10. CMC doc #5: Drug Substance: Stability Data (if applicable)

2.  **Regulator Validates and Acknowledges (Version 2 of Initial Task)**
    
The regulator receives the task (detected via their own system integration), performs an initial validation, and updates the Initial Task to acknowledge receipt and provide validation results.
    <br>
**Example:** <a href="Task-scenario1-02-validation.json" target="_blank">JSON Resource</a> | <a href="scenario1-02-validation.html" target="_blank">HTML Action View</a>
    
*   Regulator updates the Task status to **Accepted**.
*   Regulator prepares the **Acknowledgement of Receipt** and **Validation Results**.
*   Regulator adds these documents to `Task.output` and saves the Task.
*   *Note: This update triggers a notification to the Company.*

3.  **Regulator Processes Submission**
    
The regulator begins the internal processing of the shelf-life update request.

4.  **Regulator finds an issue and Posts a new Task**
    
During processing, the regulator identifies a need for clarification or additional information.
    <br>
**Example:** <a href="Task-scenario1-03-questions.json" target="_blank">JSON Resource</a> | <a href="scenario1-03-questions.html" target="_blank">HTML View</a>

*   The Regulator posts a **new** Task with a specific question in `Task.input`.
*   *Note: This Task has the same `groupIdentifier` as the initial task.*
*   *Note: Creating this new Task triggers a notification to the Company.*

5.  **Company Posts a response**
    
The company reviews the question and provides the necessary information.
    <br>
**Example:** <a href="Task-scenario1-04-response.json" target="_blank">JSON Resource</a> | <a href="scenario1-04-response.html" target="_blank">HTML View</a>

*   Company posts a response to the **question Task** (updating it) with the content of the response in `Task.output`.
*   *Note: This update triggers a notification to the Regulator.*

6.  **Regulator changes the status of the question task to complete**
    
The regulator accepts the company's response and closes the query task.
*   Regulator updates the Task status to **Completed**.
*   *Note: This update triggers a notification to the Company.*

7.  **Regulator conducts the Review**
    
The regulator proceeds with the scientific and regulatory review of the shelf-life data.

8.  **Regulator finds an issue and Posts a new Task**
    
Another issue or question arises during the detailed review.
*   The Regulator posts a **new** Task with a question in `Task.input`.
*   *Note: This Task has the same `groupIdentifier` as the initial task.*
*   *Note: Creating this new Task triggers a notification to the Company.*

9.  **Company Posts a response**
    
The company addresses the second query.
*   Company posts a response to the **question Task** (updating it) with the content of the response in `Task.output`.
*   *Note: This update triggers a notification to the Regulator.*

10. **Regulator changes the status of the question task to complete**
    
The regulator validates the response and closes the second query task.
*   Regulator updates the Task status to **Completed**.
*   *Note: This update triggers a notification to the Company.*

1.  **Regulator completes the review (Version 3 of Initial Task)**
    
The review process concludes.
    <br>
**Example:** <a href="Task-scenario1-05-decision.json" target="_blank">JSON Resource</a> | <a href="scenario1-05-decision.html" target="_blank">HTML View</a>

*   Regulator updates the status of the **Initial Task** to **complete**.
*   Regulator adds the **Cover Letter**, **Decision Letter**, and **Review Report** to `Task.output` of the Initial Task.
*   *Note: This final update triggers a notification to the Company, signaling the end of the process.*
