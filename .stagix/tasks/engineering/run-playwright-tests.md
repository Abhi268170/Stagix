# Task: run-playwright-tests

## Purpose

QA Engineer's browser testing protocol with dev server management. Verifies each acceptance criterion against a running application via Playwright MCP.

## Protocol

### 1. Dev Server Management

```
Read core-config.yaml:
  dev_server.startup_dependencies → run each command
  dev_server.command → start the server
  dev_server.port → note the port
  dev_server.health_check → poll until responsive (max 30 seconds)

If health check fails:
  STOP. Gate file error: "Dev server failed to start."
  Include: command used, error output, suggested fix.
```

### 2. Per-AC Testing Loop

For each acceptance criterion in the story:

```
1. browser_navigate → relevant URL for this AC
2. browser_snapshot → capture accessibility tree (primary verification method)
3. Execute interactions:
   - browser_fill_form for inputs
   - browser_click for buttons/links
4. Verify outcomes:
   - browser_verify_text_visible
   - browser_verify_element_visible
   - browser_verify_value
5. browser_take_screenshot → evidence capture
6. Record: PASS or FAIL with notes
```

### 3. Edge Case Testing

For each edge case in the story:
- Same navigate → interact → verify → screenshot cycle
- Use edge case inputs (empty, invalid, boundary)
- Verify error handling is user-friendly

### 4. Regression Testing

Test core user journeys from previous stories:
- Login/logout flow (if auth exists)
- Main navigation paths
- Primary CRUD operations
- Any journey flagged in previous QA reports

### 5. Evidence Collection

```
browser_console_messages → capture all console errors/warnings
browser_network_requests → verify API calls match expectations
```

All evidence saved to `.stagix/qa/evidence/`:
- Screenshots: `{story-key}-{ac-number}-{step}.png`
- Traces: Playwright trace files (auto-saved by MCP config)

### 6. Report Assembly

Write `.stagix/qa/reports/{story-key}-qa-report.md` with:
- Test environment details
- PASS/FAIL per AC with evidence links
- Edge case results
- Regression results
- Console errors
- Network request anomalies
- Overall PASS/FAIL determination

### 7. Publish & Update

- Create Confluence page: `QA Evidence: {story-key}`
- Add Jira comment with evidence links
- If all AC pass: update Jira status to QA Passed
