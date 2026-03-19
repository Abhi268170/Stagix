# Planning Gate Checklist (10 Categories)

Pre-Group-2 validation. ALL categories must pass before Scrum Master gate is submitted.

## 1. Requirements Coverage
- [ ] Every goal in project-brief.md has at least one epic in prd.md
- [ ] Every in-scope item has a corresponding feature
- [ ] Out-of-scope items are still excluded

## 2. Architecture Completeness
- [ ] architecture.md covers all epics
- [ ] coding-standards.md exists and is substantive
- [ ] tech-stack.md lists every technology with version
- [ ] source-tree.md defines complete folder structure

## 3. Schema Alignment
- [ ] Every data entity in PRD has a table in db-schema.md
- [ ] Foreign keys match architecture relationships
- [ ] Migration plan is ordered and zero-downtime

## 4. UX Coverage
- [ ] Every user-facing feature has a user flow in ux-spec.md
- [ ] Component inventory covers all screens
- [ ] MASTER.md has colours, typography, spacing defined

## 5. API Contract Coverage
- [ ] Every endpoint referenced in stories exists in api-contracts.md
- [ ] Request/response shapes fully typed
- [ ] Auth requirements per endpoint specified

## 6. Cross-Document Consistency
- [ ] Tech stack matches detected_stack in core-config.yaml
- [ ] Table names consistent across db-schema and api-contracts
- [ ] Component names consistent between ux-spec and source-tree

## 7. Brownfield Compatibility (if applicable)
- [ ] Existing patterns from discovery report respected
- [ ] No breaking changes without ADR
- [ ] Migration strategy accounts for existing schema

## 8. NFR Coverage
- [ ] Performance requirements specified
- [ ] Security requirements specified
- [ ] Scalability approach defined
- [ ] Accessibility level stated (WCAG AA minimum)

## 9. Security Considerations
- [ ] Auth/authz approach in architecture
- [ ] Secrets management specified
- [ ] Input validation noted
- [ ] Security-relevant stories have security notes

## 10. Test Strategy
- [ ] Testing framework in tech-stack.md
- [ ] Coverage threshold in core-config.yaml
- [ ] Test types expected per story
