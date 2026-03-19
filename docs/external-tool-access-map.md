# External Tool Access Map

Every point where Stagix agents interact with Jira, Confluence, Playwright, or UI UX Pro Max.

---

## Atlassian MCP — Jira

### Tool: `jira_create_issue`
| Used By | When | Purpose | Volume |
|---|---|---|---|
| Scrum Master | Planning Phase, Gate 7 | Create Jira epics (one per PRD epic) | ~4 per project |

### Tool: `jira_batch_create_issues`
| Used By | When | Purpose | Volume |
|---|---|---|---|
| Scrum Master | Planning Phase, Gate 7 | Create all stories for an epic in one operation. Batches of 10 with 30-second pauses for rate limits. | ~22 per project (varies with PRD) |

### Tool: `jira_get_issue`
| Used By | When | Purpose |
|---|---|---|
| Engineering Lead | At `/implement-story PROJ-123` time | Fetch complete story detail to validate story-ready checklist |

### Tool: `jira_get_transitions`
| Used By | When | Purpose |
|---|---|---|
| Engineering Lead | After story fetch | Get available status transitions for current story state |

### Tool: `jira_search` (JQL)
| Used By | When | Purpose |
|---|---|---|
| Engineering Lead | Pipeline management | Query stories by status, assignee, sprint |
| `/status` command | Any time | Show all in-progress stories for current sprint status view |

### Tool: `jira_update_issue`
| Used By | When | Purpose |
|---|---|---|
| Hooks (status transitions) | on-story-start, on-dev-complete, on-review-failed | Transition story status: Planned → In Dev → In Review → Done |
| QA Engineer | After QA passes | Update story status to QA Passed |
| Scrum Master | During story creation | Update issue fields if needed |

### Tool: `jira_add_comment`
| Used By | When | Purpose |
|---|---|---|
| Security Specialist | After security audit | Add security audit summary + Confluence link as story comment |
| Tech Lead Reviewer | After code review | Add review summary + Confluence link as story comment |
| QA Engineer | After QA | Add QA evidence links as story comment |
| Scrum Master | During story creation | Add supplementary detail to stories |

### Tool: `jira_get_sprint_issues`
| Used By | When | Purpose |
|---|---|---|
| `/status` command | Any time | Show all stories in current sprint with their statuses |

---

## Atlassian MCP — Confluence

### Tool: `confluence_create_page`
| Used By | When | Page Created | Parent Page |
|---|---|---|---|
| Business Analyst | After elicitation complete | 'Project Brief' | Project Home |
| Product Manager | After PRD creation | 'Product Requirements Document' | Project Home |
| UX Designer | After UX spec + design system | 'UX Specification' | Project Home |
| Solution Architect | After architecture design | 'System Architecture' + 'ADR Log' | Project Home |
| Database Designer | After schema design | 'Database Design' | Project Home |
| Technical Writer | Publishing phase | 'Project Home' (root) + 6 child pages | Space root |
| Test Case Specialist | After test case writing | 'Test Plan: PROJ-123' | Project Home / Stories |
| Security Specialist | After security audit | 'Security Audit: PROJ-123' | Project Home / Reviews |
| Tech Lead Reviewer | After code review | 'Code Review: PROJ-123' | Project Home / Reviews |
| QA Engineer | After browser QA | 'QA Evidence: PROJ-123' | Project Home / QA |
| Hooks (escalation) | On 3-strike escalation | 'Escalation: PROJ-123' | Project Home / Reviews |

### Tool: `confluence_update_page`
| Used By | When | Purpose |
|---|---|---|
| Product Manager | PRD refinement | Update existing PRD page |
| Technical Writer | Re-publishing | Update existing pages with version comments |
| Hooks (update-confluence-status.py) | On agent stop | Update 'Last Updated' metadata on agent's page |
| QA Engineer | After regression re-test | Append QA results to existing Test Plan page |

### Tool: `confluence_add_label`
| Used By | When | Labels Applied |
|---|---|---|
| Technical Writer | Publishing phase | project-name, phase (planning/engineering), doc-type (prd/architecture/ux-spec/db-schema/etc.) per page |

### Tool: `confluence_move_page`
| Used By | When | Purpose |
|---|---|---|
| Technical Writer | Publishing phase | Organise pages into correct space structure after creation |

### Tool: `confluence_search`
| Used By | When | Purpose |
|---|---|---|
| All planning agents (brownfield) | Brownfield mode | Search existing Confluence content to avoid duplicating docs |

### Tool: `confluence_get_page`
| Used By | When | Purpose |
|---|---|---|
| Codebase Archaeologist | Brownfield discovery | Read existing architectural docs in Confluence |

### Tool: `confluence_get_page_children`
| Used By | When | Purpose |
|---|---|---|
| `/status` command | Any time | Navigate space structure to verify all docs present |

---

## Playwright MCP — Browser QA

All Playwright tools are used exclusively by the **QA Engineer** agent, except `browser_generate_locator` which is also used by the **Test Case Specialist**.

### Playwright Configuration (settings.json)
```json
{
  "playwright": {
    "command": "npx",
    "args": ["@playwright/mcp@latest", "--headless", "--save-trace",
             "--save-video=1280x720", "--output-dir", ".stagix/qa/evidence/",
             "--test-id-attribute", "data-testid"]
  }
}
```

### QA Engineer — Full Browser Testing Sequence

| Step | Tool | Purpose |
|---|---|---|
| 1 | `Bash` (dev server start) | Start dev server using command from core-config.yaml (e.g., `uvicorn main:app --reload on port 8000`) |
| 2 | `Bash` (health check) | Wait for health check endpoint to respond. If fails, gate flagged with specific error. |
| 3 | `browser_navigate` | Navigate to dev server URL to start each test |
| 4 | `browser_snapshot` | Capture accessibility tree snapshot — primary testing mechanism (token-efficient vs screenshots) |
| 5 | `browser_fill_form` | Fill form fields with test data from test plan |
| 6 | `browser_click` | Click buttons, links, interactive elements per test plan |
| 7 | `browser_verify_text_visible` | Verify expected text appears after actions |
| 8 | `browser_verify_element_visible` | Verify UI elements are present per AC |
| 9 | `browser_verify_value` | Verify form field values, checkbox states |
| 10 | `browser_take_screenshot` | Capture evidence screenshots at key test points |
| 11 | `browser_console_messages` | Capture browser console errors as part of QA evidence |
| 12 | `browser_network_requests` | Verify API calls were made with expected parameters |

### QA Process Per Story
1. Start dev server, wait for health check
2. For each AC item: navigate → interact per test plan → capture accessibility snapshot → verify expected state → take evidence screenshot
3. For each edge case: repeat with edge case inputs
4. Run regression: verify core user journeys from previous stories still work
5. Produce QA report with PASS/FAIL per AC item, evidence links, browser console errors
6. Publish to Confluence 'QA Evidence: PROJ-123'
7. Update Jira status → QA Passed

### Test Case Specialist — Locator Generation Only

| Tool | Purpose |
|---|---|
| `browser_generate_locator` | Generate Playwright locators for UI interaction hints. Included in test plan so developers and QA know exact selectors. Only used if dev server is running during test planning phase. |

---

## UI UX Pro Max Skill

### Active Generation (UX Designer Agent)

| When | What Happens |
|---|---|
| UX Designer activated (after PM gate approved) | SKILL.md auto-activates the ui-ux-pro-max skill |
| Skill activation | Analyses PRD to detect product category (SaaS, e-commerce, healthcare, etc.) |
| Python reasoning engine | Runs search.py against 161 industry rules, 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, 99 UX guidelines |
| Output | Complete design system: recommended style (e.g., Trust & Authority), colour palette, typography pairing (e.g., Inter/DM Sans), key effects, anti-patterns to avoid |
| Files written | `ux-spec.md` + `design-system/MASTER.md` |
| Pre-delivery checklist | Enforces: no emoji icons, cursor-pointer on all clickables, hover states, contrast ratios, focus states, prefers-reduced-motion, responsive breakpoints |

### Read-Only Reference (Frontend Developer Agent)

| When | What Happens |
|---|---|
| Frontend Dev activated | Reads `design-system/MASTER.md` as immutable constraint |
| Before writing any component | Cross-references MASTER.md for colours, typography, spacing, component patterns |
| If UI decision deviates from MASTER.md | Flags to human for approval — does NOT deviate unilaterally |
| Before marking frontend tasks complete | Runs ui-ux-pro-max pre-delivery checklist |
| Page-specific overrides | Reads `design-system/pages/{page-name}.md` if exists |

---

## MCP Tool Allowlist Per Agent (Complete)

| Agent | Permitted MCP Tools |
|---|---|
| Business Analyst | `confluence_create_page`, `confluence_update_page` |
| Product Manager | `confluence_create_page`, `confluence_update_page` |
| UX Designer | `confluence_create_page` |
| Solution Architect | `confluence_create_page`, `confluence_update_page` |
| DB Designer | `confluence_create_page` |
| Technical Writer | `confluence_create_page`, `confluence_update_page`, `confluence_add_label`, `confluence_move_page` |
| Scrum Master | `jira_create_issue`, `jira_batch_create_issues`, `jira_update_issue`, `jira_add_comment` |
| Engineering Lead | `jira_get_issue`, `jira_get_transitions`, `jira_search` |
| Backend Dev | **None** (MCP access via hooks only) |
| Frontend Dev | **None** (MCP access via hooks only) |
| DevOps | **None** (MCP access via hooks only) |
| Test Case Specialist | `confluence_create_page`, `playwright_browser_generate_locator` |
| Security Specialist | `confluence_create_page`, `jira_add_comment` |
| Tech Lead Reviewer | `confluence_create_page`, `jira_add_comment` |
| QA Engineer | All `playwright_browser_*` tools, `confluence_create_page`, `jira_update_issue`, `jira_add_comment` |

---

## Confluence Space Structure (Created by Technical Writer)

```
{PROJECT_NAME} Space
└── Project Home
    ├── Project Brief
    ├── Product Requirements Document
    ├── UX Specification
    ├── System Architecture
    │   └── ADR Log
    ├── Database Design
    ├── API Contracts
    └── Stories/
        ├── Test Plan: PROJ-1
        ├── Test Plan: PROJ-2
        ├── Security Audit: PROJ-1
        ├── Code Review: PROJ-1
        ├── QA Evidence: PROJ-1
        └── ...
```

All pages labelled with: `{project-name}`, `{phase}`, `{doc-type}`
All pages cross-linked (Architecture → DB Schema, API Contracts → UX Spec)
Version comments note which planning iteration produced the document.
