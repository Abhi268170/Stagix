# BMAD → Stagix Reuse Map

**BMAD Source**: `reference/.bmad-core/` (75 files, v4.44.3)
**Stagix Target**: `.stagix/` (~186 files)

The core philosophical shift: BMAD is a **conversational framework** (agents = personas you switch between, quality = advisory). Stagix is an **automated orchestration system** (agents = subprocesses, quality = structural enforcement via hooks).

**Content is highly reusable. Delivery mechanism is completely different.**

---

## Agents: Reuse Persona, Change Container

| BMAD Agent | Stagix Agent(s) | Reuse Level | What to Keep | What to Change |
|---|---|---|---|---|
| `analyst.md` (Mary) | `business-analyst.md` | 70% | Persona, curiosity-driven inquiry, 5-phase elicitation, brainstorming techniques | Strip `*command` syntax. Add tool allowlist (Read, Write project-brief.md only, Confluence MCP). Add skill refs (elicitation-methods). Add output format (project-brief.md → Confluence). |
| `pm.md` (John) | `product-manager.md` | 70% | Investigative strategist persona, user-champion principles, ruthless prioritisation | Remove code access. Add Confluence MCP permissions. Add PRD template reference. Add brownfield-discovery.md as input in brownfield mode. |
| `architect.md` (Winston) | `solution-architect.md` | 75% | Holistic thinking principles (verbatim — they're excellent), pragmatic tech selection, progressive complexity | Add sharded output (coding-standards.md, tech-stack.md, source-tree.md, api-contracts.md). Add stack overlay composition. Add research-stack-best-practices sub-task for unknown stacks. Add Confluence MCP. |
| `ux-expert.md` (Sally) | `ux-designer.md` | 50% | User-centric principles, edge case awareness, micro-interaction focus | Remove Lovable/V0 prompt generation. Add ui-ux-pro-max skill integration (auto-activates). Add design-system/MASTER.md output. Add Confluence MCP for UX Spec page. |
| `sm.md` (Bob) | `scrum-master.md` | 60% | Story preparation focus, crystal-clear developer handoffs, sequential identification | Replace local file output with Jira MCP (jira_create_issue, jira_batch_create_issues, jira_add_comment). Add brownfield-story-tmpl.yaml awareness. Add rate limit handling (batches of 10, 30s pauses). |
| `dev.md` (James) | `backend-dev.md` + `frontend-dev.md` | 60% | Implementation discipline, story-driven protocol, task-by-task execution, strict story file permissions | Split into two agents. Add devLoadAlwaysFiles constraint (coding-standards.md, tech-stack.md, source-tree.md). Add stack-specific skill loading. Backend: no MCP. Frontend: read-only ui-ux-pro-max reference. |
| `qa.md` (Quinn) | Split into 4 agents | 40% | Risk profiling concepts, test design, Given-When-Then, NFR assessment, gate decisions | **test-case-specialist.md**: Reuse test-design + trace capabilities. Add Playwright locator generation. **security-specialist.md**: Reuse risk-profile concepts. Focus on OWASP Top 10. Read-only, no code modification. **tech-lead-reviewer.md**: New 5-dimension review (code quality, security conformance, test coverage, architecture conformance, performance). **qa-engineer.md**: Entirely new — Playwright browser automation. |
| `po.md` (Sarah) | No direct equivalent | 30% | Validation logic, cross-document consistency checks | Role absorbed by gate system + Planning Lead + checklists. Reuse po-master-checklist.md validation logic in planning-gate-check.md task. |
| `bmad-orchestrator.md` | `planning-lead.md` | 20% | Concept of agent coordination | Completely different mechanism — Agent Team LEAD mode vs *agent transformation. |
| `bmad-master.md` | No equivalent | 0% | — | Stagix doesn't have a single-agent-does-everything mode. |

---

## Templates: High Reuse with Enhancement

| BMAD Template | Stagix Template | Reuse % | Key Enhancements |
|---|---|---|---|
| `project-brief-tmpl.yaml` | `project-brief-tmpl.yaml` | 80% | Add success metrics section, MoSCoW prioritisation, target users section |
| `prd-tmpl.yaml` | `prd-tmpl.yaml` | 75% | Add user personas, P1/P2/P3 priority per epic, explicit out-of-scope, assumptions and dependencies |
| `brownfield-prd-tmpl.yaml` | `brownfield-prd-tmpl.yaml` | 85% | Add regression risk estimation per change |
| `architecture-tmpl.yaml` | `architecture-tmpl.yaml` | 70% | Remove front-end sections (separate UX spec in Stagix). Add API contracts sharding, ADR log, sharded sub-files output |
| `fullstack-architecture-tmpl.yaml` | `fullstack-architecture-tmpl.yaml` | 75% | Add sharding output paths for devLoadAlwaysFiles |
| `brownfield-architecture-tmpl.yaml` | `brownfield-architecture-tmpl.yaml` | 85% | Excellent existing/new tech separation — reuse directly. Add migration strategy emphasis |
| `front-end-spec-tmpl.yaml` | `ux-spec-tmpl.yaml` | 60% | Enhance with design system output (MASTER.md format), component inventory from ui-ux-pro-max |
| `front-end-architecture-tmpl.yaml` | `front-end-architecture-tmpl.yaml` | 70% | Sync with ui-ux-pro-max output format |
| `story-tmpl.yaml` | `story-tmpl.yaml` | 65% | **Biggest enhancement**: Add API contract refs, DB schema refs, edge cases (min 3), security notes, testing notes (unit/integration/E2E), implementation subtasks with complexity estimates |
| `qa-gate-tmpl.yaml` | `qa-report-tmpl.yaml` | 40% | Expand to AC-level PASS/FAIL with evidence links, Playwright screenshots, console errors |
| `brainstorming-output-tmpl.yaml` | Not included | 0% | Brainstorming is handled within BA elicitation |
| `competitor-analysis-tmpl.yaml` | Not included | 0% | Out of scope for Stagix |
| `market-research-tmpl.yaml` | Not included | 0% | Out of scope for Stagix |
| — | `db-schema-tmpl.yaml` | New | ERD, tables, indexes, migrations, query patterns |
| — | `api-contract-tmpl.yaml` | New | OpenAPI 3.0 per endpoint |
| — | `adr-tmpl.yaml` | New | Architecture Decision Record |
| — | `brownfield-discovery-tmpl.yaml` | New | 12-section discovery report |
| — | `test-plan-tmpl.yaml` | New | Given-When-Then + Playwright locators + traceability matrix |
| — | `test-case-tmpl.yaml` | New | Individual test case with edge case slots |
| — | `security-report-tmpl.yaml` | New | OWASP mapping, CRITICAL/HIGH/MEDIUM/LOW |
| — | `code-review-report-tmpl.yaml` | New | 5-dimension PASS/FAIL |

---

## Tasks: Reuse Logic, Change Interface

| BMAD Task | Stagix Task | Reuse % | Adaptation |
|---|---|---|---|
| `create-doc.md` | Pattern across all `create-*.md` | 50% | Reuse step-by-step elicitation workflow pattern. Each Stagix task is more specialized. |
| `create-next-story.md` | `create-story.md` | 60% | Reuse sequential identification and architecture-reading strategy. Replace local output with Jira MCP. |
| `advanced-elicitation.md` | `elicit-requirements.md` | 75% | Reuse 5-phase structure and method selection. Maps to BA's elicitation skill. |
| `shard-doc.md` | N/A (inline in Architect) | 30% | Stagix does sharding as part of Architect's output, not separate step. |
| `review-story.md` | `code-review.md` | 40% | Reuse multi-dimension approach. Expand to 5 explicit dimensions. |
| `qa-gate.md` | Gate system + handoff-gate.py | 30% | Reuse gate decision concepts. Change from manual to automated hook. |
| `risk-profile.md` | `security-audit.md` | 40% | Reuse probability × impact scoring. Apply to OWASP categories. |
| `test-design.md` | `write-test-cases.md` | 50% | Reuse test level recommendations and Given-When-Then format. Add Playwright locators. |
| `validate-next-story.md` | `story-ready-checklist.md` | 60% | Reuse validation criteria. Add Stagix-specific fields. |
| `brownfield-create-story.md` | `brownfield-create-story.md` | 70% | Reuse directly. Add rollback procedure and regression risk. |
| `execute-checklist.md` | `enforce-dod.py` hook | 40% | Reuse checklist execution logic in hook enforcement. |
| `document-project.md` | `discover-brownfield.md` | 30% | Concept reuse. Stagix Archaeologist is read-only, automated, produces structured 12-section report. |
| `trace-requirements.md` | Part of test-case-specialist | 50% | Reuse Given-When-Then traceability matrix concept. |
| `nfr-assess.md` | Part of tech-lead-reviewer | 40% | Reuse NFR validation. Embedded in performance/scalability dimension. |
| `facilitate-brainstorming-session.md` | Not included | 0% | Out of scope. |
| `create-deep-research-prompt.md` | Not included | 0% | Replaced by skill self-populating mechanism. |

---

## Checklists: Reuse and Expand

| BMAD Checklist | Stagix Checklist | Reuse % | Adaptation |
|---|---|---|---|
| `story-dod-checklist.md` | `story-dod-checklist.md` | 90% | Reuse all 7 sections directly. Enforce via enforce-dod.py hook. |
| `architect-checklist.md` | `planning-gate-checklist.md` | 60% | Reuse requirements alignment and architecture fundamentals. Expand to 10-category pre-Group-2 validation. |
| `story-draft-checklist.md` | `story-ready-checklist.md` | 70% | Reuse validation criteria. Add API refs, DB refs, security notes, edge cases. |
| `po-master-checklist.md` | Absorbed into gate system | 50% | Reuse cross-document validation logic in planning-gate-check.md. |
| `pm-checklist.md` | Part of PRD template validation | 60% | Reuse PM validation criteria. |
| `change-checklist.md` | `brownfield-impact-checklist.md` | 50% | Reuse change impact assessment. Add regression risk and rollback. |

---

## Data Files: Direct Reuse

| BMAD Data | Stagix Target | Reuse % |
|---|---|---|
| `elicitation-methods.md` | `skills/elicitation-methods/base.md` | 95% (verbatim) |
| `brainstorming-techniques.md` | Part of BA skill reference | 80% |
| `test-levels-framework.md` | `skills/testing-standards/base.md` seed | 70% |
| `test-priorities-matrix.md` | Part of testing-standards skill | 70% |
| `technical-preferences.md` | core-config.yaml preferences section | Concept only |
| `bmad-kb.md` | Not included | 0% (Stagix has no KB mode) |

---

## Workflows: Reuse Structure, Enhance

| BMAD Workflow | Stagix Workflow | Reuse % | Key Changes |
|---|---|---|---|
| `greenfield-fullstack.yaml` | `greenfield-fullstack.yaml` | 60% | Add detect-stack step, parallel UX+Architect, gate file refs, Group 1→2 sequencing |
| `greenfield-service.yaml` | `greenfield-service.yaml` | 60% | Skip UX Designer |
| `greenfield-ui.yaml` | `greenfield-ui.yaml` | 60% | Skip backend architecture |
| `brownfield-fullstack.yaml` | `brownfield-fullstack.yaml` | 55% | Add Archaeologist discovery phase before anything else |
| `brownfield-service.yaml` | `brownfield-service.yaml` | 55% | Add discovery phase |
| `brownfield-ui.yaml` | `brownfield-ui.yaml` | 55% | Add discovery phase |

---

## Summary

| Category | BMAD Files | Stagix Files | Reuse Rate | Net New |
|---|---|---|---|---|
| Agents | 9 | 17 | ~55% content | 8 new roles |
| Templates | 11 | 18 | ~65% content | 9 new templates |
| Tasks | 29 | 24 | ~45% content | 12 new tasks |
| Checklists | 6 | 8 | ~65% content | 4 new checklists |
| Data/Skills | 6 | ~77 | ~10% content | ~65 stack overlays (all new) |
| Workflows | 6 | 6 | ~58% structure | Enhanced with gates |
| Hooks | 0 | 9 | 0% | All new |
| Commands | 0 | 7 | 0% | All new |
| Config | 1 | 3 | ~30% | Mostly new |
| **Total** | **75** | **~186** | **~35% overall** | **~120 net new files** |

**BMAD accelerates Stagix build by ~35%**, primarily in agent personas, templates, checklists, and workflow structures. The novel Stagix value (hooks, gates, MCP automation, skills with stack overlays, pipeline orchestration) is all built from scratch.
