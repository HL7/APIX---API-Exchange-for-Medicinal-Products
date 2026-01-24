<!--ReleaseHeader--><p id="publish-box">Publish Box goes here</p><!--EndReleaseHeader-->

## Example: APIX Task (Shelf Life)

This page presents an example APIX Task resource demonstrating the submission of shelf life data for a medicinal product.

### Overview

This example illustrates how a regulatory applicant submits stability and shelf life data for a medicinal product using the APIX Task profile.

### Example Details

**Task ID**: example-apix-shelf-life-original

**Task Type**: Post-approval Change / Supplement

**Business Scenario**: 
- Initial approval granted for a medicinal product
- New stability data generated demonstrating longer shelf life
- Applicant submits variation request with updated shelf life claim

### Key Elements Demonstrated

1. **Task Metadata**
   - Unique task identifier (UUID)
   - Version tracking and modification timestamps
   - Conformance to APIX Task profile

2. **Regulatory References**
   - Procedure number linking to regulatory submission
   - Parent task grouping for related submissions

3. **Embedded Documents**
   - Stability study reports
   - Shelf life justification documents
   - Quality overall summary updates

4. **Workflow Management**
   - Status transitions (requested → in-progress → completed)
   - Business status tracking
   - Timeline management

### Regulatory Context

Shelf life variations are common in the post-approval phase when:
- Manufacturing process improvements extend product stability
- New packaging materials provide better protection
- Long-term stability data demonstrates extended validity
- Regulatory guidance changes affecting shelf life claims

### Related Resources

- [APIX Task Profile](StructureDefinition-apix-task.html)
- [DocumentReference Profile](StructureDefinition-apix-documentreference.html)
- [Use Cases](usecases.html)
