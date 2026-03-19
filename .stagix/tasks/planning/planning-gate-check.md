# Task: planning-gate-check

## Purpose

10-category pre-handoff validation that runs before the Scrum Master marks Group 1 as complete. Ensures all planning artifacts are consistent, complete, and ready for the Engineering Collective.

## When to Run

After the Scrum Master creates all Jira stories but before the final Group 1 gate is submitted. The Planning Lead should trigger this check.

## The 10 Categories

### 1. Requirements Coverage
- [ ] Every goal in project-brief.md has at least one epic in prd.md
- [ ] Every in-scope item has a corresponding feature
- [ ] Out-of-scope items are still excluded

### 2. Architecture Completeness
- [ ] architecture.md covers all epics in the PRD
- [ ] coding-standards.md exists and is non-empty
- [ ] tech-stack.md lists every technology with version
- [ ] source-tree.md defines the complete folder structure

### 3. Schema Alignment
- [ ] Every data entity in the PRD has a corresponding table in db-schema.md
- [ ] Foreign keys match the relationships described in architecture.md
- [ ] Migration plan is ordered and zero-downtime

### 4. UX Coverage
- [ ] Every user-facing feature in PRD has a user flow in ux-spec.md
- [ ] Component inventory covers all screens
- [ ] design-system/MASTER.md has colours, typography, spacing defined

### 5. API Contract Coverage
- [ ] Every endpoint referenced in stories exists in api-contracts.md
- [ ] Request/response shapes are fully typed
- [ ] Auth requirements specified per endpoint

### 6. Cross-Document Consistency
- [ ] Tech stack in architecture.md matches detected_stack in core-config.yaml
- [ ] Table names in db-schema.md match entity names in api-contracts.md
- [ ] Component names in ux-spec.md match source-tree.md conventions

### 7. Brownfield Compatibility (if applicable)
- [ ] Existing patterns from discovery report are respected
- [ ] No breaking changes to existing APIs without ADR
- [ ] Migration strategy accounts for existing schema

### 8. NFR Coverage
- [ ] Performance requirements specified (response time, throughput)
- [ ] Security requirements specified (auth, data protection)
- [ ] Scalability approach defined
- [ ] Accessibility level stated (WCAG AA minimum)

### 9. Security Considerations
- [ ] Auth/authz approach defined in architecture
- [ ] Secrets management strategy specified
- [ ] Input validation requirements noted
- [ ] Security-relevant stories have security notes

### 10. Test Strategy
- [ ] Testing framework identified in tech-stack.md
- [ ] Coverage threshold set in core-config.yaml
- [ ] Test types expected per story (unit, integration, E2E)

## Result

If ALL categories pass: Proceed to Scrum Master gate submission.
If ANY category fails: Report specific missing items. The relevant agent must address them before proceeding.
