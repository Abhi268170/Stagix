# Stagix Implementation Plan

**Source**: Stagix-Blueprint.pdf Section 13 (pages 50-53)
**Estimated build**: 5-7 focused days across 10 phases

---

## Phase 1 — Foundation (Day 1 AM) ~8 files

The skeleton everything else plugs into.

### Files
- `CLAUDE.md` — project constitution (parametrised with {PROJECT_NAME}, {JIRA_KEY}, {CONFLUENCE_SPACE})
- `settings.json` — MCP server registrations (Atlassian + Playwright), all 5 hook event bindings with script paths, global permission rules
- `core-config.yaml` — all config keys with sensible defaults and inline documentation
- `install.sh` — one-command installer: copies .stagix/ into target project, installs MCPs, prompts for Jira/Confluence credentials, runs detect-stack, writes env vars
- `modes/greenfield.yaml` — greenfield sequence definition
- `modes/brownfield.yaml` — brownfield sequence definition
- `.stagix/gates/README.md` — gate file format documentation
- `.stagix/state/pipeline-log.json` — empty initial state file

### BMAD Reuse
- `core-config.yaml`: Adapt BMAD's core-config.yaml structure. Add detected_stack, coverage_threshold, gate_locations, dev_server_command, brownfield_mode_flag, linters section.
- Everything else: Build new.

### Smoke Test
Run install.sh in a blank directory. Verify settings.json is valid JSON. Verify MCP servers start.

---

## Phase 2 — Planning Group Agents & Tasks (Day 1 PM) ~22 files

All 9 planning agents + their primary task files.

### Files
- `agents/planning/planning-lead.md` — Agent Team LEAD configuration
- `agents/planning/business-analyst.md` — adapt from BMAD analyst.md
- `agents/planning/product-manager.md` — adapt from BMAD pm.md
- `agents/planning/ux-designer.md` — adapt from BMAD ux-expert.md + ui-ux-pro-max integration
- `agents/planning/solution-architect.md` — adapt from BMAD architect.md + sharded output
- `agents/planning/db-designer.md` — new (BMAD handles schema in architecture)
- `agents/planning/technical-writer.md` — new (BMAD has no Confluence automation)
- `agents/planning/scrum-master.md` — adapt from BMAD sm.md + Jira MCP
- `agents/planning/codebase-archaeologist.md` — new (brownfield only)
- `tasks/planning/detect-stack.md`
- `tasks/planning/elicit-requirements.md` — adapt from BMAD advanced-elicitation.md
- `tasks/planning/create-project-brief.md`
- `tasks/planning/create-prd.md`
- `tasks/planning/create-ux-spec.md`
- `tasks/planning/create-architecture.md` + `research-stack-best-practices.md`
- `tasks/planning/create-db-schema.md`
- `tasks/planning/create-api-contracts.md`
- `tasks/planning/push-to-confluence.md`
- `tasks/planning/create-jira-epic.md`, `create-story.md`
- `tasks/planning/planning-gate-check.md`
- `tasks/brownfield/discover-brownfield.md`, `brownfield-create-story.md`, `regression-baseline.md`

### BMAD Reuse
- **Heavy reuse**: analyst.md → business-analyst.md, pm.md → product-manager.md, architect.md → solution-architect.md, ux-expert.md → ux-designer.md, sm.md → scrum-master.md
- **Adapt format**: Strip BMAD `*command` syntax, add Stagix tool allowlists, skill references, MCP permissions, output format specs
- **New agents**: Planning Lead, DB Designer, Technical Writer, Archaeologist — build from blueprint specs

### Smoke Test
Activate planning-lead agent. Run /start-project 'test idea'. Verify BA asks elicitation questions.

---

## Phase 3 — Engineering Group Agents & Tasks (Day 2 AM) ~17 files

All 8 engineering agents + their task files.

### Files
- `agents/engineering/engineering-lead.md` — with story-ready checklist integration
- `agents/engineering/backend-dev.md` — adapt from BMAD dev.md (backend half)
- `agents/engineering/frontend-dev.md` — adapt from BMAD dev.md (frontend half)
- `agents/engineering/devops.md` — new
- `agents/engineering/test-case-specialist.md` — extract from BMAD qa.md test-design capabilities
- `agents/engineering/security-specialist.md` — extract from BMAD qa.md risk/security capabilities
- `agents/engineering/tech-lead-reviewer.md` — new (5-dimension review)
- `agents/engineering/qa-engineer.md` — new (Playwright browser QA)
- `tasks/engineering/implement-story.md` — adapt from BMAD dev workflow
- `tasks/engineering/write-test-cases.md`
- `tasks/engineering/implement-tests.md`
- `tasks/engineering/security-audit.md`
- `tasks/engineering/code-review.md`
- `tasks/engineering/run-playwright-tests.md`
- `tasks/engineering/update-jira-status.md`
- `tasks/engineering/story-dod-check.md`
- `tasks/brownfield/compatibility-check.md`, `brownfield-impact-assess.md`

### BMAD Reuse
- **dev.md** splits into backend-dev.md + frontend-dev.md (reuse implementation discipline, story-driven protocol)
- **qa.md** splits into 4 specialists (reuse risk profiling → security, test design → test-case-specialist, review → tech-lead)
- **story-dod-checklist.md** reuse verbatim in enforce-dod.py

### Smoke Test
Run /implement-story with a pre-existing Jira story. Verify Engineering Lead validates story fields.

---

## Phase 4 — Skills Layer (Day 2 PM) ~55 files

All domain knowledge files. Start with base.md files, then add stack overlays.

### Files
- `skills/backend-standards/` — SKILL.md + base.md + 10 stack overlays (python-fastapi, python-django, node-express, node-nestjs, rails, go-gin, java-spring, dotnet-aspnet, php-laravel, rust-actix, _generic)
- `skills/frontend-standards/` — SKILL.md + base.md + 8 overlays (react-next, react-vite, vue-nuxt, sveltekit, angular, astro, html-tailwind, _generic)
- `skills/testing-standards/` — SKILL.md + base.md + 9 overlays (jest-rtl, vitest, pytest, rspec, go-testing, junit5, xunit, playwright, _generic)
- `skills/db-design/` — SKILL.md + base.md + 8 overlays (postgresql, mysql, mongodb, sqlite, redis, dynamodb, cockroachdb, _generic)
- `skills/security-review/` — SKILL.md (context:fork) + base.md + 7 overlays (python, node, rails, java, php, go, _generic)
- `skills/api-design/` — SKILL.md + base.md + 4 overlays (rest-openapi, graphql, grpc-protobuf, websocket, _generic)
- `skills/scalability-patterns/` — SKILL.md + base.md + 4 overlays (aws, gcp, kubernetes, _generic)
- `skills/migrations/` — SKILL.md + base.md + 8 overlays (alembic, flyway, liquibase, rails-activerecord, prisma, typeorm, gorm, goose, _generic)
- `skills/infrastructure/` — SKILL.md + base.md + 7 overlays (docker-compose, kubernetes, terraform-aws, terraform-gcp, github-actions, gitlab-ci, circleci, _generic)
- `skills/confluence-structure-guide/` — SKILL.md + base.md
- `skills/elicitation-methods/` — SKILL.md + base.md
- Install ui-ux-pro-max: `npm install -g uipro-cli && uipro init --ai claude`

### BMAD Reuse
- `data/elicitation-methods.md` → `skills/elicitation-methods/base.md` (verbatim)
- `data/test-levels-framework.md` + `test-priorities-matrix.md` → seed content for `skills/testing-standards/base.md`
- `data/technical-preferences.md` → concept reused in core-config.yaml preferences
- All stack overlay content: Build new (no BMAD equivalent)

### Smoke Test
Activate backend-dev agent on a Python FastAPI project. Verify it loads FastAPI-specific coding standards.

---

## Phase 5 — Hook System (Day 3 AM) ~9 files

The enforcement layer.

### Files
- `hooks/pre-tool-use/block-git-commit.py` — gate check + DoD check + test run + coverage check
- `hooks/pre-tool-use/block-destructive-ops.py` — destructive command blocklist
- `hooks/pre-tool-use/validate-file-scope.py` — agent file scope enforcement
- `hooks/post-tool-use/run-linter.py` — stack-appropriate linter invocation
- `hooks/post-tool-use/log-file-changes.py` — pipeline log appender
- `hooks/stop/handoff-gate.py` — gate file writer + desktop notification
- `hooks/stop/update-confluence-status.py` — Confluence metadata updater
- `hooks/task-completed/enforce-dod.py` — DoD checklist enforcer
- `hooks/subagent-stop/collect-output.py` — output aggregator
- Wire all hooks in settings.json with correct matchers

### BMAD Reuse
- None — BMAD has zero enforcement hooks. All built new.
- Concept reuse: BMAD's story-dod-checklist.md validation logic → enforce-dod.py

### Smoke Test
Trigger a git commit without gate approval. Verify it is blocked with correct error message.

---

## Phase 6 — Templates & Checklists (Day 3 AM) ~26 files

### Template Files
- `templates/project-brief-tmpl.yaml` — adapt from BMAD project-brief-tmpl.yaml
- `templates/prd-tmpl.yaml` — adapt from BMAD prd-tmpl.yaml
- `templates/ux-spec-tmpl.yaml` — adapt from BMAD front-end-spec-tmpl.yaml
- `templates/architecture-tmpl.yaml` — adapt from BMAD architecture-tmpl.yaml
- `templates/fullstack-architecture-tmpl.yaml` — adapt from BMAD fullstack-architecture-tmpl.yaml
- `templates/front-end-architecture-tmpl.yaml` — adapt from BMAD front-end-architecture-tmpl.yaml
- `templates/brownfield-architecture-tmpl.yaml` — adapt from BMAD brownfield-architecture-tmpl.yaml
- `templates/brownfield-discovery-tmpl.yaml` — new (12-section discovery report)
- `templates/db-schema-tmpl.yaml` — new
- `templates/api-contract-tmpl.yaml` — new (OpenAPI 3.0)
- `templates/adr-tmpl.yaml` — new
- `templates/story-tmpl.yaml` — adapt from BMAD story-tmpl.yaml (add API refs, DB refs, edge cases, security notes)
- `templates/brownfield-story-tmpl.yaml` — adapt from BMAD (add rollback, regression risk, feature flag)
- `templates/test-plan-tmpl.yaml` — new (Given-When-Then + Playwright locators)
- `templates/test-case-tmpl.yaml` — new
- `templates/security-report-tmpl.yaml` — new (OWASP mapping)
- `templates/code-review-report-tmpl.yaml` — new (5-dimension PASS/FAIL)
- `templates/qa-report-tmpl.yaml` — adapt from BMAD qa-gate-tmpl.yaml

### Checklist Files
- `checklists/planning-gate-checklist.md` — adapt from BMAD po-master-checklist.md + architect-checklist.md
- `checklists/story-ready-checklist.md` — adapt from BMAD story-draft-checklist.md
- `checklists/code-review-checklist.md` — new (5-dimension)
- `checklists/security-checklist.md` — new (OWASP-based)
- `checklists/qa-checklist.md` — new (AC coverage, edge cases, regression)
- `checklists/story-dod-checklist.md` — reuse from BMAD story-dod-checklist.md
- `checklists/brownfield-impact-checklist.md` — new
- `checklists/confluence-doc-checklist.md` — new

### Smoke Test
Activate Scrum Master. Run create-story task. Verify output matches story-tmpl.yaml structure.

---

## Phase 7 — Slash Commands (Day 3 PM) ~7 files

### Files
- `commands/start-project/SKILL.md` — triggers detect-stack + planning-lead
- `commands/implement-story/SKILL.md` — validates story + triggers engineering-lead
- `commands/approve/SKILL.md` — writes gate approval file
- `commands/reject/SKILL.md` — writes rejection + feedback routing
- `commands/review-handoff/SKILL.md` — reads and formats pending gate file
- `commands/status/SKILL.md` — pipeline + Jira sprint status view
- `commands/discover-brownfield/SKILL.md` — standalone Archaeologist trigger

### Smoke Test
Run /status. Verify it reads pipeline-log.json and displays correctly.

---

## Phase 8 — Workflow Definitions (Day 3 PM) ~6 files

### Files
- `workflows/greenfield-fullstack.yaml` — adapt from BMAD greenfield-fullstack.yaml
- `workflows/greenfield-service.yaml` — adapt from BMAD greenfield-service.yaml
- `workflows/greenfield-ui.yaml` — adapt from BMAD greenfield-ui.yaml
- `workflows/brownfield-fullstack.yaml` — adapt from BMAD brownfield-fullstack.yaml (add Archaeologist phase)
- `workflows/brownfield-service.yaml` — adapt from BMAD brownfield-service.yaml
- `workflows/brownfield-ui.yaml` — adapt from BMAD brownfield-ui.yaml

### Smoke Test
Load greenfield-fullstack.yaml. Verify Planning Lead can read and follow the sequence.

---

## Phase 9 — Integration Testing (Day 4 AM) 0 new files

End-to-end test using a real test project (simple Todo List API — Python FastAPI + PostgreSQL).

### Test Plan
1. Run `/start-project 'A todo list API with user authentication'`
2. Follow all Planning Group gates — verify each agent produces correct output
3. Verify Confluence pages are created correctly
4. Verify Jira stories are created with full detail
5. Run `/implement-story` on the first story
6. Verify entire Engineering pipeline runs — security, code review, QA
7. Verify git commit is blocked until all gates pass
8. Verify Playwright QA runs against the dev server
9. Verify final approval gate works correctly
10. Document gaps, edge cases, or missing coverage

### Acceptance
Complete end-to-end run of one story with zero manual workarounds required.

---

## Phase 10 — Brownfield Integration Testing (Day 4 PM) ~5 additional files

Test brownfield mode against a real legacy codebase.

### Test Plan
1. Use an existing FastAPI project as the test brownfield codebase
2. Run `/discover-brownfield` — verify Archaeologist produces comprehensive report
3. Approve discovery report — verify constrained planning agents read it correctly
4. Run `/start-project` on a feature addition story
5. Verify regression-baseline is captured before first story
6. Verify brownfield-story-tmpl.yaml is used with rollback and regression risk fields
7. Verify compatibility-check runs before code review
8. Verify tech debt items from Archaeologist feed into Security Specialist audit

### Acceptance
Brownfield feature story completes full pipeline including regression baseline check.
