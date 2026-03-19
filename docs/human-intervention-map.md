# Human Intervention Map

Every point where a human must act, decide, or provide input across the Stagix pipeline.

---

## Planning Collective (Group 1)

### Interactive Sessions (Human Actively Participates)

| Agent | Interaction Type | What Happens | Skippable? |
|---|---|---|---|
| **Business Analyst** | Multi-turn Q&A | 5-phase structured elicitation: (1) Goal clarification, (2) User identification, (3) Problem validation, (4) Scope boundary setting, (5) Success criteria definition. Every question logged. This is the ONLY agent with extended interactive dialogue. | No — first agent, always runs |
| **Solution Architect** | Single question | Only if greenfield with no detectable stack: "What tech stack do you want?" Human answers, Architect writes to core-config.yaml. If stack detected automatically, no interaction. | Conditional — only greenfield with no signal files |

### Gate Approvals (Human Reviews Output, Approves or Rejects)

| Gate # | After Agent | What to Review | Approve | Reject | Avg Review Time |
|---|---|---|---|---|---|
| 1 | Business Analyst | project-brief.md in .stagix/docs/ + Confluence 'Project Brief' page. Questions: Is scope correct? Missing stakeholders? Success metrics measurable? | `/approve business-analyst` | `/reject business-analyst "reason"` | 5-10 min |
| 2 | Product Manager | prd.md + Confluence 'PRD' page. Questions: Is MVP scope correct? Are epics ordered right? Are NFRs complete? | `/approve product-manager` | `/reject product-manager "reason"` | 10-15 min |
| 3 | UX Designer | ux-spec.md + design-system/MASTER.md. Questions: Does design system match brand? Are user flows complete? | `/approve ux-designer` | `/reject ux-designer "reason"` | 10-15 min |
| 4 | Solution Architect | architecture.md + sharded files (coding-standards.md, tech-stack.md, source-tree.md) + Confluence page. Questions: Is tech stack acceptable? Does architecture match infrastructure constraints? | `/approve solution-architect` | `/reject solution-architect "reason"` | 15-20 min |
| 5 | Database Designer | db-schema.md + Confluence 'Database Design' page. Questions: Is schema normalised correctly? Is migration strategy zero-downtime? | `/approve db-designer` | `/reject db-designer "reason"` | 10-15 min |
| 6 | Technical Writer | All Confluence pages published. Questions: Is space navigable? Are all docs cross-linked correctly? | `/approve technical-writer` | `/reject technical-writer "reason"` | 5-10 min |
| 7 | Scrum Master | All Jira epics + stories. Questions: Are stories detailed enough for development? Are edge cases comprehensive? **This is the final Group 1 gate — unlocks Group 2.** | `/approve scrum-master` | `/reject scrum-master "reason"` | 15-30 min (spot-check stories) |

### Rejection Flow
When human runs `/reject {stage} "reason"`:
1. `.stagix/gates/{stage}.rejected` file is written with feedback
2. Orchestrator reads rejection, re-activates the completing agent with feedback injected as context
3. Agent re-runs with specific corrections
4. New gate file written on completion
5. Human reviews again

---

## Engineering Collective (Group 2) — Per Story

### Conditional Developer Escalations (Human Asked Mid-Execution)

| Agent | Trigger | What Human Does |
|---|---|---|
| **Backend Dev** | Unapproved dependency needed | Approve or deny the dependency |
| **Backend Dev** | Ambiguity after re-reading story | Clarify the requirement |
| **Backend Dev** | 3 consecutive implementation failures | Decide: descope, redesign, or manually assist |
| **Backend Dev** | Missing config values (API keys, env vars) | Provide the values |
| **Frontend Dev** | UI decision deviates from MASTER.md | Approve deviation or insist on spec compliance |
| **Frontend Dev** | Same 4 triggers as Backend Dev | Same responses |

### Gate Approvals (Per Story)

| Gate # | After Agent | What to Review | Approve | Reject |
|---|---|---|---|---|
| 8 | DevOps | CI/CD pipeline changes, Dockerfile updates, IaC changes in .github/workflows/ and terraform/. Questions: Does pipeline cover new story's test requirements? Are environment variables documented? | `/approve devops` | `/reject devops "reason"` |
| 9 | Test Case Specialist | test-plan.md + Confluence 'Test Plan: PROJ-123'. Questions: Are test cases exhaustive? Do edge cases cover all AC variants? | `/approve test-plan` | `/reject test-plan "reason"` |
| 10 | Security Specialist | security-report.md + Confluence 'Security Audit: PROJ-123'. Questions: Are you comfortable with the security risk rating? Any findings to escalate? **CRITICAL/HIGH = must fix.** | `/approve security` | `/reject security "reason"` |
| 11 | Tech Lead Reviewer | code-review-report.md + Confluence 'Code Review: PROJ-123'. All 5 dimensions must PASS (code quality, security conformance, test coverage, architecture conformance, performance). Questions: Does implementation look production-grade? Any architectural concerns? | `/approve tech-lead` | `/reject tech-lead "reason"` |
| 12 | QA Engineer | qa-report.md + Playwright traces + screenshots in Confluence 'QA Evidence: PROJ-123'. Questions: Does feature behave as specified? Are you happy with evidence quality? | `/approve qa` | `/reject qa "reason"` |
| 13 | **FINAL** | All gate reports (security, code review, QA). **This is the merge decision.** Questions: Are you satisfied with the full engineering pipeline output for this story? | `/approve final PROJ-123` | `/reject final PROJ-123 "reason"` |

### 3-Strike Escalation (Automatic Human Notification)

If a story accumulates 3 consecutive FAIL outcomes from any single review agent (Security, Tech Lead, or QA):
1. Story status → Blocked in Jira
2. Confluence page 'Escalation: PROJ-123' created with full failure log
3. Desktop notification: 'Story PROJ-123 has failed 3 consecutive reviews. Manual intervention required.'
4. Human runs `/status` to see full log
5. Human decides: rework entirely, descope specific AC, or redesign approach
6. Engineering Lead awaits human decision before proceeding

---

## Utility Commands (Human-Initiated, No Gate)

| Command | When Used | What Happens |
|---|---|---|
| `/status` | Any time | Shows current pipeline state: active agent, pending gates, Jira story statuses for active sprint, open review items |
| `/review-handoff {stage}` | Before approving/rejecting | Shows the pending gate file contents: what agent produced, what needs review, specific questions |
| `/discover-brownfield` | Joining existing project mid-stream | Manually triggers Archaeologist in isolation |

---

## Total Human Touchpoints Per Project

### Greenfield Project (e.g., 4 epics, 22 stories)

| Category | Count | Total Time Estimate |
|---|---|---|
| BA interactive session | 1 | 20-40 min |
| Stack selection (if needed) | 0-1 | 2 min |
| Planning gates (7) | 7 | 70-115 min |
| **Planning total** | **8-9** | **~1.5-2.5 hours** |
| Engineering gates per story (6) | 6 × 22 = 132 | ~10 min each = ~22 hours |
| Final approval per story | 22 | ~5 min each = ~2 hours |
| Developer escalations | Variable (est. 0-2 per story) | Variable |
| 3-strike escalations | Rare (est. 0-2 total) | Variable |
| **Engineering total** | **~154-176** | **~24-28 hours** |
| **Grand total** | **~163-185** | **~26-30 hours of human time** |

Note: Human time is spread across the project duration. Most engineering gates can be reviewed asynchronously — the system waits for `/approve` without timeout.
