# SPRINT-006: Phase 6 — Templates & Checklists

**Status**: DONE
**Priority**: P1 — Agents produce output without templates (lower quality) but need them for consistency
**Estimate**: ~26 files
**Dependencies**: SPRINT-002, SPRINT-003 (Agents reference these templates)

---

## Objective

Build all YAML document templates and quality gate checklists. After this phase, every agent produces output in a consistent, validated format.

---

## Tickets

### STGX-052: Planning Document Templates
**Status**: TODO
**Files** (8 total):
- `templates/project-brief-tmpl.yaml` — Vision, goals, constraints, target users, success metrics, out-of-scope. **BMAD reuse ~80%** from project-brief-tmpl.yaml.
- `templates/prd-tmpl.yaml` — Epics, user stories, personas, NFRs, priorities, assumptions. **BMAD reuse ~75%** from prd-tmpl.yaml. Add user personas, P1/P2/P3 priority.
- `templates/ux-spec-tmpl.yaml` — User flows, component inventory, design system, interaction patterns, accessibility. **BMAD reuse ~60%** from front-end-spec-tmpl.yaml. Add design-system/MASTER.md output format.
- `templates/architecture-tmpl.yaml` — Tech stack, system design, coding standards, API design, source tree, infra, security. **BMAD reuse ~70%** from architecture-tmpl.yaml. Add sharding output, ADR log.
- `templates/fullstack-architecture-tmpl.yaml` — Combined backend + frontend. **BMAD reuse ~75%**.
- `templates/front-end-architecture-tmpl.yaml` — Frontend-only architecture. **BMAD reuse ~70%**.
- `templates/brownfield-architecture-tmpl.yaml` — Existing + new tech architecture. **BMAD reuse ~85%**.
- `templates/brownfield-discovery-tmpl.yaml` — 12-section discovery report. **New** — no BMAD equivalent.

**Acceptance Criteria**:
- [ ] Each template has YAML frontmatter with version, output path, required sections
- [ ] Section instructions guide agent on what to produce
- [ ] Elicitation flags on interactive sections
- [ ] All templates match what the corresponding agent task expects

---

### STGX-053: Engineering Document Templates
**Status**: TODO
**Files** (8 total):
- `templates/db-schema-tmpl.yaml` — ERD, tables, indexes, migrations, query patterns. **New**.
- `templates/api-contract-tmpl.yaml` — OpenAPI 3.0 per endpoint. **New**.
- `templates/adr-tmpl.yaml` — Architecture Decision Record. **New**.
- `templates/story-tmpl.yaml` — AC, subtasks, API refs, DB refs, edge cases, security notes, testing notes. **BMAD reuse ~65%** from story-tmpl.yaml. Biggest enhancement.
- `templates/brownfield-story-tmpl.yaml` — Story + existing code affected, regression risk, rollback, feature flag. **BMAD reuse ~70%** + new fields.
- `templates/test-plan-tmpl.yaml` — Given-When-Then cases, Playwright locators, traceability matrix. **New**.
- `templates/test-case-tmpl.yaml` — Individual test case with edge case slots. **New**.
- `templates/security-report-tmpl.yaml` — CRITICAL/HIGH/MEDIUM/LOW findings, OWASP mapping. **New**.
- `templates/code-review-report-tmpl.yaml` — 5-dimension PASS/FAIL per dimension. **New**.
- `templates/qa-report-tmpl.yaml` — AC coverage, pass/fail per item, evidence links, console errors. **BMAD reuse ~40%** from qa-gate-tmpl.yaml.

**Acceptance Criteria**:
- [ ] Each template matches what the corresponding agent task produces
- [ ] story-tmpl.yaml has all fields from blueprint Section 4.8
- [ ] qa-report-tmpl.yaml has evidence link and screenshot fields

---

### STGX-054: Quality Gate Checklists
**Status**: TODO
**Files** (8 total):
- `checklists/planning-gate-checklist.md` — 10-category pre-Group-2 validation. **BMAD reuse ~60%** from po-master-checklist.md + architect-checklist.md.
- `checklists/story-ready-checklist.md` — Engineering Lead validates story has all 12 required fields. **BMAD reuse ~70%** from story-draft-checklist.md.
- `checklists/code-review-checklist.md` — Tech Lead's 5-dimension review criteria. **New**.
- `checklists/security-checklist.md` — OWASP-based, CRITICAL/HIGH block, MEDIUM note, LOW document. **New**.
- `checklists/qa-checklist.md` — AC coverage, edge cases, regression, browser compatibility. **New**.
- `checklists/story-dod-checklist.md` — Developer self-check (7 sections). **BMAD reuse ~90%** from story-dod-checklist.md.
- `checklists/brownfield-impact-checklist.md` — API compat, schema compat, regression risk. **New**.
- `checklists/confluence-doc-checklist.md` — Technical Writer validates doc completeness. **New**.

**Acceptance Criteria**:
- [ ] Each checklist has clear pass/fail criteria per item
- [ ] story-dod-checklist.md maps to enforce-dod.py hook validation
- [ ] security-checklist.md maps to Security Specialist's audit protocol
- [ ] code-review-checklist.md covers all 5 dimensions

---

## Smoke Test

Activate Scrum Master with create-story task. Verify output matches story-tmpl.yaml structure.

## Definition of Done

- [ ] All 3 tickets completed (STGX-052 through STGX-054), ~26 files total
- [ ] Every template referenced by an agent task actually exists
- [ ] Every checklist referenced by a hook or agent actually exists
