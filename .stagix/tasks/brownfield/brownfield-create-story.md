# Task: brownfield-create-story

## Purpose

Creates Jira stories with brownfield-specific fields that standard greenfield stories don't have. Used by the Scrum Master when project mode is brownfield.

## Additional Fields (Beyond Standard Story Template)

Every brownfield story MUST include these four additional sections:

### 1. Existing Code Affected
List every file that will be modified:
```
Files Modified:
- src/api/routes/users.py (adding new endpoint)
- src/models/user.py (adding team_id field)
- src/services/auth.py (updating permission check)

Patterns to Follow:
- Error handling: Use existing AppError class (see src/utils/errors.py)
- Validation: Use existing Pydantic models pattern (see src/schemas/)
- Testing: Follow existing conftest.py fixtures
```

### 2. Regression Risk
Rate as High / Medium / Low with justification:
```
Regression Risk: MEDIUM
Justification: Modifying auth.py permission check affects all protected
endpoints. Existing test coverage on auth module is 72% (from discovery
report §6). The change is additive (new permission, not modifying existing
ones) which limits blast radius.
```

### 3. Rollback Procedure
How to revert this change safely:
```
Rollback:
1. Revert commit {hash} — removes new endpoint and schema changes
2. Run migration rollback: alembic downgrade -1
3. No data migration needed (new column only, nullable)
4. No feature flag cleanup needed
```

### 4. Feature Flag Recommendation
Whether this change should be behind a feature flag:
```
Feature Flag: RECOMMENDED
Reason: New team management feature changes navigation for all users.
Flag name: ENABLE_TEAM_MANAGEMENT
Rollout: Internal first, then 10% → 50% → 100%
```

Or:
```
Feature Flag: NOT NEEDED
Reason: Backend-only change to an internal API. No user-visible impact.
```

## When to Use

- Always use when `core-config.yaml` → `project.mode` is `brownfield`
- Scrum Master automatically selects this template over standard story template
