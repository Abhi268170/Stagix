# Stagix Sprint Board

## Ticket Summary

| Sprint | Phase | Tickets | Files | Status | Dependencies |
|---|---|---|---|---|---|
| [SPRINT-001](SPRINT-001-foundation.md) | Foundation | STGX-001 → STGX-008 (8 tickets) | ~8 files | DONE | None |
| [SPRINT-002](SPRINT-002-planning-agents.md) | Planning Agents & Tasks | STGX-009 → STGX-020 (12 tickets) | ~22 files | DONE | SPRINT-001 |
| [SPRINT-003](SPRINT-003-engineering-agents.md) | Engineering Agents & Tasks | STGX-021 → STGX-029 (9 tickets) | ~17 files | DONE | SPRINT-001 |
| [SPRINT-004](SPRINT-004-skills-layer.md) | Skills Layer | STGX-030 → STGX-042 (13 tickets) | ~55 files | DONE | SPRINT-001 |
| [SPRINT-005](SPRINT-005-hooks.md) | Hook System | STGX-043 → STGX-051 (9 tickets) | ~9 files | DONE | SPRINT-001 |
| [SPRINT-006](SPRINT-006-templates-checklists.md) | Templates & Checklists | STGX-052 → STGX-054 (3 tickets) | ~26 files | DONE | SPRINT-002, 003 |
| [SPRINT-007](SPRINT-007-commands-workflows.md) | Commands & Workflows | STGX-055 → STGX-062 (8 tickets) | ~13 files | DONE | SPRINT-002, 003, 005 |
| [SPRINT-008](SPRINT-008-integration-testing.md) | Integration Testing | STGX-063 → STGX-066 (4 tickets) | ~5 files | TODO | ALL |

**Total: 66 tickets, ~186 files**

## Build Order

```
SPRINT-001 (Foundation)
    ├── SPRINT-002 (Planning Agents)
    ├── SPRINT-003 (Engineering Agents)  ← can run parallel with 002
    ├── SPRINT-004 (Skills)              ← can run parallel with 002/003
    └── SPRINT-005 (Hooks)               ← can run parallel with 002/003/004
            ├── SPRINT-006 (Templates)   ← needs 002+003 done
            └── SPRINT-007 (Commands)    ← needs 002+003+005 done
                    └── SPRINT-008 (Integration Testing) ← needs ALL done
```

## Key Design Decisions Embedded in Tickets

1. **Option B for hooks**: Hooks only read/write local files. No direct API calls. Confluence updates delegated to next agent activation. (SPRINT-005, STGX-048)
2. **BMAD reuse tracked per ticket**: Each ticket notes exact BMAD source file and reuse percentage.
3. **Smoke tests per sprint**: Every sprint has a smoke test verifying the phase works before proceeding.
4. **MCP access mapped per agent**: Tool allowlists in SPRINT-002/003 match external-tool-access-map.md exactly.
