# SPRINT-002: Phase 2 — Planning Group Agents & Tasks

**Status**: DONE
**Priority**: P0 — Blocks Group 1 execution
**Estimate**: ~22 files
**Dependencies**: SPRINT-001 (Foundation)

---

## Objective

Build all 9 planning agents and their primary task files. After this phase, `/start-project` can activate the Planning Lead who spawns specialists through the full planning sequence.

---

## Tickets

### STGX-009: Planning Lead Agent
**Status**: TODO
**File**: `.stagix/agents/planning/planning-lead.md`
**Description**: Orchestrator for Group 1. Uses Agent Team LEAD mode. Spawns all planning specialists in sequence defined by mode YAML. Pauses at each gate for human approval. Cannot produce documents or call MCP tools directly.

**Tool Allowlist**: Task (spawn subagents), Message (peer coordination), Read (gate files, core-config.yaml)
**Skills Loaded**: None — reads only
**Outputs**: Gate notifications, handoff summaries, next-agent briefings

**BMAD Reuse**: Concept from bmad-orchestrator.md (~20%). Different mechanism entirely — Agent Team LEAD vs *agent transformation.

**Acceptance Criteria**:
- [ ] Agent Team LEAD configuration correct
- [ ] Reads mode YAML (greenfield.yaml or brownfield.yaml) for sequence
- [ ] Spawns agents in correct order with correct inputs
- [ ] Handles parallel spawn for UX Designer + Solution Architect
- [ ] Pauses at each gate, prints review instructions
- [ ] Handles rejection → re-spawns agent with feedback

---

### STGX-010: Business Analyst Agent (Mary)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/business-analyst.md`
- `.stagix/tasks/planning/elicit-requirements.md`
- `.stagix/tasks/planning/create-project-brief.md`

**Description**: First agent activated. Conducts interactive multi-turn elicitation with the human. 5-phase structure: goal clarification, user identification, problem validation, scope boundary, success criteria. Outputs project-brief.md + Confluence page.

**Tool Allowlist**: Read (core-config.yaml, brownfield-discovery.md if brownfield), Write (.stagix/docs/project-brief.md), `mcp__atlassian__confluence_create_page`, `mcp__atlassian__confluence_update_page`
**Skills Loaded**: elicitation-methods
**Outputs**: project-brief.md → Confluence 'Project Brief' → GATE: BA approval

**BMAD Reuse**: Heavy from analyst.md (~70%). Keep persona, curiosity-driven inquiry, brainstorming techniques. Strip *command syntax. Add tool allowlist, Confluence MCP, skill refs, output format.

**Acceptance Criteria**:
- [ ] 5-phase elicitation structure implemented
- [ ] Every question logged
- [ ] project-brief.md follows project-brief-tmpl.yaml structure
- [ ] Confluence page created with correct content
- [ ] In brownfield mode, reads discovery report as context
- [ ] Cannot write code or create Jira items

---

### STGX-011: Product Manager Agent (John)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/product-manager.md`
- `.stagix/tasks/planning/create-prd.md`

**Description**: Reads approved project-brief.md, produces PRD with epics, user personas, prioritisation, NFRs. Publishes to Confluence.

**Tool Allowlist**: Read (.stagix/docs/project-brief.md, brownfield-discovery.md), Write (.stagix/docs/prd.md), `confluence_create_page`, `confluence_update_page`
**Skills Loaded**: None — uses prd-tmpl.yaml template
**Outputs**: prd.md → Confluence 'PRD' → GATE: PM approval

**BMAD Reuse**: From pm.md (~70%). Keep investigative strategist persona, user-champion principles. Add PRD template reference with P1/P2/P3 priority, explicit out-of-scope, user personas.

**Acceptance Criteria**:
- [ ] PRD follows prd-tmpl.yaml structure
- [ ] Epics with P1/P2/P3 priority
- [ ] User personas included
- [ ] NFRs (performance, security, scalability, accessibility) complete
- [ ] Validates PRD against project brief before marking complete
- [ ] Cannot write code or create Jira items

---

### STGX-012: UX Designer Agent (Sally)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/ux-designer.md`
- `.stagix/tasks/planning/create-ux-spec.md`

**Description**: Reads PRD, auto-activates ui-ux-pro-max skill for design system generation. Produces ux-spec.md + design-system/MASTER.md. Publishes to Confluence.

**Tool Allowlist**: Read (.stagix/docs/prd.md, design-system/ if exists), Write (.stagix/docs/ux-spec.md, design-system/MASTER.md), `confluence_create_page`
**Skills Loaded**: ui-ux-pro-max (auto-activates Python reasoning engine), frontend-standards (read-only reference)
**Outputs**: ux-spec.md → design-system/MASTER.md → Confluence 'UX Specification' → GATE: UX approval

**BMAD Reuse**: From ux-expert.md (~50%). Keep user-centric principles. Replace Lovable/V0 prompt generation with ui-ux-pro-max integration.

**Acceptance Criteria**:
- [ ] ui-ux-pro-max skill auto-activates
- [ ] Design system generated with style, palette, typography, anti-patterns
- [ ] MASTER.md includes colours, typography, spacing, component patterns
- [ ] User flows documented
- [ ] Component inventory complete
- [ ] Cannot write code

---

### STGX-013: Solution Architect Agent (Winston)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/solution-architect.md`
- `.stagix/tasks/planning/create-architecture.md`
- `.stagix/tasks/planning/research-stack-best-practices.md`

**Description**: Reads PRD (and UX spec after parallel phase). Produces architecture.md + sharded sub-files. If unknown stack detected, runs research-stack-best-practices to generate new skill overlay. Publishes to Confluence.

**Tool Allowlist**: Read (prd.md, ux-spec.md, brownfield-discovery.md), Write (.stagix/docs/architecture.md, .stagix/docs/architecture/coding-standards.md, tech-stack.md, source-tree.md, api-contracts.md), `confluence_create_page`, `confluence_update_page`
**Skills Loaded**: backend-standards (stack overlay auto-selected), api-design, scalability-patterns, migrations
**Outputs**: architecture.md + sharded sub-files → Confluence 'System Architecture' + 'ADR Log' → GATE: Architect approval

**BMAD Reuse**: From architect.md (~75%). Keep holistic thinking principles verbatim. Add sharded output, stack overlay composition, research-stack-best-practices sub-task.

**Acceptance Criteria**:
- [ ] Architecture follows architecture-tmpl.yaml structure
- [ ] Sharded files produced: coding-standards.md, tech-stack.md, source-tree.md
- [ ] API contracts produced as api-contracts.md
- [ ] If unknown stack: research-stack-best-practices generates new overlay
- [ ] Reviews UX spec after parallel phase, accommodates UI requirements
- [ ] Cannot write application code

---

### STGX-014: Database Designer Agent (Rex)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/db-designer.md`
- `.stagix/tasks/planning/create-db-schema.md`

**Description**: Reads PRD + architecture.md (for chosen DB technology). Designs complete schema, indexes, migration strategy, query patterns. Publishes to Confluence.

**Tool Allowlist**: Read (prd.md, architecture.md, brownfield-discovery.md), Write (.stagix/docs/db-schema.md), `confluence_create_page`
**Skills Loaded**: db-design (base.md + stack overlay for detected DB — PostgreSQL, MySQL, MongoDB, etc.)
**Outputs**: db-schema.md → Confluence 'Database Design' → GATE: DB approval

**BMAD Reuse**: None — BMAD handles schema in architecture. Built new per blueprint Section 4.6.

**Acceptance Criteria**:
- [ ] Schema follows db-schema-tmpl.yaml structure
- [ ] ERD overview, table definitions, index strategy with justifications
- [ ] Migration plan (ordered, idempotent, zero-downtime)
- [ ] Query patterns with expected execution plans
- [ ] In brownfield: maps new tables against existing, flags conflicts
- [ ] Cannot write migration files or application code

---

### STGX-015: Technical Writer Agent (Alex)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/technical-writer.md`
- `.stagix/tasks/planning/push-to-confluence.md`

**Description**: Reads all docs/ files, publishes to Confluence with consistent structure, cross-links, and labels. Creates Project Home page as navigation hub.

**Tool Allowlist**: Read (.stagix/docs/*), `confluence_create_page`, `confluence_update_page`, `confluence_add_label`, `confluence_move_page`
**Skills Loaded**: confluence-structure-guide
**Outputs**: Structured Confluence space → GATE: TW approval

**BMAD Reuse**: None — BMAD has no Confluence automation. Built new per blueprint Section 4.7.

**Acceptance Criteria**:
- [ ] Project Home page created as root
- [ ] All design docs published as child pages
- [ ] Labels applied: project-name, phase, doc-type
- [ ] Cross-links between related pages (Architecture → DB Schema, API Contracts → UX Spec)
- [ ] Version comments on each page
- [ ] Cannot write local files or create Jira items

---

### STGX-016: Scrum Master Agent (Bob)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/scrum-master.md`
- `.stagix/tasks/planning/create-jira-epic.md`
- `.stagix/tasks/planning/create-story.md`

**Description**: Reads all design docs. Creates Jira epics (one per PRD epic) and fully-detailed stories. Last planning agent before Group 1 handoff.

**Tool Allowlist**: Read (.stagix/docs/*, architecture/*, ux-spec.md, db-schema.md), `jira_create_issue`, `jira_batch_create_issues`, `jira_update_issue`, `jira_add_comment`
**Skills Loaded**: None — reads design docs directly
**Outputs**: Jira Epics + Jira Stories → GATE: SM approval (Final Group 1 Gate)

**BMAD Reuse**: From sm.md (~60%). Keep story preparation focus. Replace local file output with Jira MCP. Add brownfield story template awareness.

**Acceptance Criteria**:
- [ ] Epics created in Jira (one per PRD epic)
- [ ] Stories created with full detail: title, user story, AC (Given-When-Then), implementation tasks, API refs, DB schema refs, edge cases (min 3), security notes, testing notes
- [ ] Batch creation with rate limit handling (batches of 10, 30s pauses)
- [ ] In brownfield: uses brownfield-story-tmpl.yaml (existing code affected, regression risk, rollback, feature flag)
- [ ] Cannot write code or local files

---

### STGX-017: Codebase Archaeologist Agent (Sam)
**Status**: TODO
**Files**:
- `.stagix/agents/planning/codebase-archaeologist.md`
- `.stagix/tasks/brownfield/discover-brownfield.md`

**Description**: Brownfield-only agent. First agent activated in brownfield mode. Read-only — scans entire codebase and produces discovery report. No human interaction needed.

**Tool Allowlist**: Read, Grep, Glob (read-only — no Write, Edit, Bash, no MCP)
**Skills Loaded**: None — reads codebase directly
**Outputs**: brownfield-discovery.md → GATE: Discovery approval

**BMAD Reuse**: Concept from document-project.md task (~30%). Stagix version is automated, read-only, produces structured 12-section report per blueprint Section 7.2-7.3.

**Acceptance Criteria**:
- [ ] 12-section discovery report: executive summary, architecture map, tech stack (confirmed), coding patterns, tech debt map, test coverage, known problem areas, external integrations, environment variables, deployment architecture, database schema (current), recommended planning constraints
- [ ] Purely read-only — no writes to codebase
- [ ] No MCP calls
- [ ] Scoped to project files only

---

### STGX-018: detect-stack Task
**Status**: TODO
**File**: `.stagix/tasks/planning/detect-stack.md`
**Description**: Runs as the very first step of /start-project. Reads signal files to determine tech stack and project mode (greenfield/brownfield).

**Signal Files**:
- package.json → Node.js/TypeScript, checks for React, Next.js, Vue, Nuxt, Svelte, Angular, Express, NestJS, Fastify
- requirements.txt / pyproject.toml → Python, checks for fastapi, django, flask, sqlalchemy, alembic, pytest, celery
- Gemfile → Ruby, checks for rails, sinatra, rspec, sidekiq, devise
- go.mod → Go, checks for gin, echo, gorm, testify
- pom.xml / build.gradle → Java/Kotlin, checks for spring-boot, hibernate, junit
- composer.json → PHP, checks for laravel, symfony
- Cargo.toml → Rust, checks for actix-web, tokio, sqlx
- Dockerfile → Container stack, reads FROM line
- .github/workflows/*.yml → CI stack
- terraform/** → Infrastructure stack

**Mode Detection**:
- Greenfield: no source files beyond config, or git log with ≤1 commit
- Brownfield: existing source files, git log >1 commit, existing tests, existing migrations

**Output**: Writes detected_stack and mode to core-config.yaml

**Acceptance Criteria**:
- [ ] All signal files from blueprint Section 6.1 checked
- [ ] Framework detection within each signal file
- [ ] Mode correctly set: greenfield or brownfield
- [ ] detected_stack written with nested keys
- [ ] Works on empty project (greenfield, empty detected_stack)

---

### STGX-019: Planning Gate Check Task
**Status**: TODO
**File**: `.stagix/tasks/planning/planning-gate-check.md`
**Description**: 10-category pre-handoff validation that runs before Scrum Master marks Group 1 complete. Ensures all planning artifacts are consistent and complete.

**10 Categories**: Requirements coverage, architecture completeness, schema alignment, UX coverage, API contract coverage, cross-document consistency, brownfield compatibility (if applicable), NFR coverage, security considerations noted, test strategy outline present

**Acceptance Criteria**:
- [ ] All 10 categories checked
- [ ] Fails if any critical category incomplete
- [ ] Reports specific missing items

---

### STGX-020: Brownfield Tasks
**Status**: TODO
**Files**:
- `.stagix/tasks/brownfield/brownfield-create-story.md`
- `.stagix/tasks/brownfield/regression-baseline.md`

**brownfield-create-story.md**: Creates stories with brownfield-specific fields (existing code affected, regression risk H/M/L, rollback procedure, feature flag recommendation).

**regression-baseline.md**: Captures existing test suite pass rate before any epic begins. Stored in .stagix/baselines/{epic-key}.json. After every story, test suite re-runs and compares against baseline.

**Acceptance Criteria**:
- [ ] Brownfield story template includes all 4 extra fields
- [ ] Regression baseline captures pass rate and stores as JSON
- [ ] Baseline comparison logic defined

---

## Smoke Test (Phase 2 Complete)

1. Activate planning-lead agent
2. Run `/start-project 'test idea'`
3. Verify detect-stack runs and writes mode
4. Verify BA activates and asks elicitation questions
5. Verify BA produces project-brief.md
6. Verify gate file written on BA completion

## Definition of Done

- [ ] All 12 tickets completed (STGX-009 through STGX-020)
- [ ] All agent files have correct tool allowlists
- [ ] All agents reference correct skill names
- [ ] Planning Lead can spawn agents in correct sequence
- [ ] At least BA → PM flow works end-to-end
