---
name: status
description: Show current Stagix pipeline state, pending gates, and Jira sprint status
---

# /status

Shows the full pipeline state at a glance.

## Usage
```
/status
```

## What It Shows
1. **Active Agent**: Who is currently running (from active-agent.json)
2. **Pipeline Progress**: Which agents have completed (from pipeline-log.json)
3. **Pending Gates**: Which gates await human review (from gates/*.pending.json)
4. **Approved Gates**: Which gates have been approved (from gates/*.approved)
5. **Jira Sprint Status**: Current sprint story statuses (via jira_search if configured)
6. **Escalations**: Any 3-strike escalations pending

## Data Sources
- `.stagix/state/active-agent.json`
- `.stagix/state/pipeline-log.json`
- `.stagix/gates/*.pending.json`, `*.approved`, `*.rejected`
- Jira MCP (if available)
