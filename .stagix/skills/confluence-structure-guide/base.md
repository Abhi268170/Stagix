# Confluence Structure Guide

## Space Structure
```
{Project Name} (Home)
├── Project Brief
├── Product Requirements Document
├── UX Specification
├── System Architecture
│   ├── API Contracts
│   └── ADR Log
├── Database Design
├── Stories/
│   ├── Test Plan: PROJ-1
│   ├── Security Audit: PROJ-1
│   ├── Code Review: PROJ-1
│   └── QA Evidence: PROJ-1
└── Brownfield Discovery (if applicable)
```

## Page Naming Convention
- `{Doc Type}: {Project Name}` for planning docs
- `{Doc Type}: {Story Key}` for engineering docs
- Examples: `PRD: TechFlow`, `Security Audit: TECH-3`

## Label Taxonomy
Every page gets three labels:
1. **Project**: `{project-name-lowercase}` (e.g., `techflow`)
2. **Phase**: `planning` or `engineering`
3. **Doc Type**: `brief`, `prd`, `ux`, `architecture`, `database`, `api`, `adr`, `security-audit`, `code-review`, `qa-evidence`, `test-plan`

## Cross-Linking Requirements
- Architecture page → links to DB Schema, API Contracts, UX Spec
- PRD → links to Architecture, UX Spec
- DB Schema → links to Architecture, API Contracts
- Test Plan → links to story in Jira
- QA Evidence → links to Test Plan, story in Jira

## Version Comments
Every page creation/update includes a version comment:
`Published by Stagix {Agent Name} | Planning Iteration {N} | {ISO-8601 timestamp}`
