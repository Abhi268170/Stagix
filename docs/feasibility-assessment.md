# Stagix Feasibility & Viability Assessment

**Date**: 2026-03-18
**Assessor**: Claude Code (Opus 4.6)
**Scope**: Full 58-page blueprint analysis + external tool research

---

## Overall Verdict

| Dimension | Rating | Comment |
|---|---|---|
| Technical Feasibility | 9/10 | Every primitive used exists and works as described. No speculative features. |
| Architectural Soundness | 9/10 | File-based state, hook enforcement, sharded context, one-level subagents — all correct decisions. |
| External Tool Readiness | 8/10 | All three MCP servers are mature and cover required operations. |
| Build Complexity | 7/10 | 186 files is significant but phases are independently testable with smoke tests. |
| Production Viability | 8/10 | Token cost and context window limits are the main operational constraints. Both mitigated. |
| **Overall** | **8.5/10** | Buildable. Well-architected. Author demonstrates deep platform understanding. |

---

## Primitive-by-Primitive Feasibility

| Blueprint Requirement | Claude Code Primitive | Status | Notes |
|---|---|---|---|
| 14 agent persona files (.md) | Agent tool + CLAUDE.md devLoadAlwaysFiles | GREEN | Standard pattern |
| Planning Lead as Agent Team LEAD | Agent tool with delegate mode / TeamCreate | GREEN | Agent Teams supported |
| Engineering Lead spawning subagents | Agent tool (Task spawn) | GREEN | Core Claude Code pattern |
| Tool allowlists per agent | Agent .md `tools` field | YELLOW | Advisory not sandboxed — validate-file-scope.py hook is real enforcement (correct design) |
| 12 skill domains + SKILL.md loaders | .claude/skills/ or symlinked | GREEN | Documented Claude Code feature |
| 5 hook scripts | settings.json hooks{} | GREEN | All 5 hook events are real. Python handlers standard. |
| Gate file system | File-based state + hooks | GREEN | Elegant filesystem-as-state-machine. No exotic deps. |
| 7 slash commands | .claude/commands/ or .stagix/commands/ | GREEN | Standard skill invocations |
| core-config.yaml | YAML file read by agents | GREEN | Straightforward structured config |
| detect-stack task | Glob/Read on signal files | GREEN | Reads package.json, go.mod, etc. |
| Self-populating knowledge | Architect generates skill overlay | YELLOW | Quality depends on Claude training knowledge for niche frameworks. Human gate mitigates. |

---

## External Tool Assessment

### MCP Atlassian (Jira + Confluence)
- **Version**: v0.21.0 (March 2026)
- **Stars**: 4.6k, 118 contributors, 72 tools
- **Coverage**: Every operation Stagix needs is available
- **Risk**: Atlassian Cloud rate limits (~100 req/min)
- **Mitigation**: Batch operations + 30-second pauses + retry logic
- **Status**: GREEN

### Playwright MCP (Microsoft)
- **Stars**: 29.2k, backed by Microsoft
- **Coverage**: All browser_* tools used by QA Engineer are real
- **Risk**: Requires dev server running locally
- **Mitigation**: Health check + startup_dependencies in core-config.yaml
- **Status**: GREEN

### UI UX Pro Max Skill
- **Version**: v2.0
- **Stars**: 44.8k, npm package `uipro-cli`
- **Coverage**: 161 industry rules, 67 styles, 161 palettes — matches blueprint claims
- **Risk**: Requires Python 3.x for reasoning engine
- **Mitigation**: Installed as Phase 4 build step
- **Status**: GREEN

---

## Architecture Strengths

1. **File-system-as-state-machine**: Gates, pipeline-log.json, active-agent.json — all persistent, session-independent, crash-recoverable
2. **Sharded architecture documents**: Respects context window limits while ensuring developers always have constraints loaded via devLoadAlwaysFiles
3. **Hook enforcement > prompt enforcement**: PreToolUse hooks block actions structurally. Prompts can be ignored; hooks cannot.
4. **Base + stack overlay skill composition**: SKILL.md loader reads core-config.yaml → loads base.md → loads detected stack overlay → presents unified context
5. **Brownfield Archaeologist**: Read-only discovery before planning — correct for legacy codebases

---

## Identified Risks

| Risk | Severity | Mitigation Quality | Notes |
|---|---|---|---|
| Context window on 500k+ LOC brownfield | HIGH | GOOD | Sharded discovery, scoped Glob patterns, source-tree.md limits |
| Token cost (14 agents × multiple turns, Agent Teams 7x) | HIGH | MODERATE | Subagent-over-team decision correct, but full pipeline = significant tokens |
| Atlassian rate limits on 50+ story batches | MEDIUM | GOOD | Batch creation + 30s pauses + retry |
| Dev server dependency for QA | MEDIUM | GOOD | Health check + startup_dependencies |
| Session interruption mid-pipeline | MEDIUM | EXCELLENT | File-based state = any agent re-activatable from gate files |
| Security Specialist false negatives | MEDIUM | GOOD | Positioned as first-pass filter, not pentest replacement |
| 3-strike escalation on complex stories | LOW | GOOD | Counter resets on human-approved rework |
| Unknown stack skill generation quality | MEDIUM | GOOD | Human gate at Architect stage, 'Review required' header on generated overlays |

---

## Critical Implementation Items

### validate-file-scope.py
The real security boundary. Reads active-agent.json, cross-references agent's permitted file scope. If buggy, agents write outside domain. **Needs thorough unit testing.**

### handoff-gate.py
The orchestration backbone. Must correctly determine completing agent, extract output files, format pending.json. **Any edge case breaks the pipeline.**

### SKILL.md loader multi-stack handling
When project has both Python backend + Next.js frontend, loader must compose overlays from both stacks and annotate which applies where. **Trickiest skill composition scenario.**

### Scrum Master batch story creation
Creating 22+ fully-detailed Jira stories in one session pushes context window limits. Batch approach with jira_batch_create_issues helps but prompt for each story is substantial.

---

## Build Effort (Realistic)

| Phase | Blueprint Estimate | Realistic Estimate | Reason |
|---|---|---|---|
| 1. Foundation | Day 1 AM | Day 1 AM | 8 files, straightforward config |
| 2. Planning Agents | Day 1 PM | Day 1 PM - Day 2 AM | 22 files; agent prompts need iteration |
| 3. Engineering Agents | Day 2 AM | Day 2 | 17 files; implement-story.md is complex |
| 4. Skills Layer | Day 2 PM | Day 2-3 | ~55 files; stack overlays need domain verification |
| 5. Hook System | Day 3 AM | Day 3 | 9 Python scripts; block-git-commit.py most complex |
| 6. Templates & Checklists | Day 3 AM | Day 3 PM | 26 files; must match agent expectations |
| 7. Slash Commands | Day 3 PM | Day 3 PM | 7 files, thin wrappers |
| 8. Workflow Definitions | Day 3 PM | Day 3 PM | 6 YAML files |
| 9. Integration Testing | Day 4 AM | Day 4-5 | Full pipeline test surfaces interaction bugs |
| 10. Brownfield Testing | Day 4 PM | Day 5-6 | Legacy codebase testing always surprises |
| **Total** | **3-4 days** | **5-7 days** | Realistic for deep Claude Code expertise |
