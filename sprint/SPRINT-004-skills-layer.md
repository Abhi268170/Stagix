# SPRINT-004: Phase 4 — Skills Layer

**Status**: DONE
**Priority**: P1 — Agents work without skills (degraded) but need them for stack-specific quality
**Estimate**: ~55 files
**Dependencies**: SPRINT-001 (Foundation — core-config.yaml for detect-stack)

---

## Objective

Build all 12 skill domains with base.md universal principles and stack-specific overlays. Install UI UX Pro Max. After this phase, agents load correct domain knowledge dynamically based on detected tech stack.

---

## Tickets

### STGX-030: SKILL.md Loader Pattern (Reference Implementation)
**Status**: TODO
**File**: Template pattern used by all 12 skills
**Description**: Define the standard SKILL.md frontmatter and loader algorithm that every skill follows.

**Loader Algorithm**:
1. Read .stagix/core-config.yaml → extract detected_stack.{relevant_key}
2. Load base.md — universal principles always apply
3. Check stacks/{detected_framework}.md exists → load if found
4. If not found → load stacks/_generic.md + flag for Architect to generate overlay
5. Present unified context: 'Universal rules apply everywhere. Stack-specific rules apply to {framework} components.'
6. If multi-stack (e.g., Python backend + Next.js frontend) → load both overlays, annotate which applies where

**Acceptance Criteria**:
- [ ] SKILL.md frontmatter pattern documented
- [ ] Loader algorithm implemented consistently across all 12 skills
- [ ] Multi-stack composition works correctly
- [ ] Missing overlay triggers _generic.md fallback + flag

---

### STGX-031: backend-standards Skill
**Status**: TODO
**Files** (12 total):
- `skills/backend-standards/SKILL.md` — loader
- `skills/backend-standards/base.md` — SOLID, error handling, logging, API contracts, service patterns, DI, config management, graceful shutdown
- `skills/backend-standards/stacks/python-fastapi.md`
- `skills/backend-standards/stacks/python-django.md`
- `skills/backend-standards/stacks/node-express.md`
- `skills/backend-standards/stacks/node-nestjs.md`
- `skills/backend-standards/stacks/rails.md`
- `skills/backend-standards/stacks/go-gin.md`
- `skills/backend-standards/stacks/java-spring.md`
- `skills/backend-standards/stacks/dotnet-aspnet.md`
- `skills/backend-standards/stacks/php-laravel.md`
- `skills/backend-standards/stacks/rust-actix.md`
- `skills/backend-standards/stacks/_generic.md`

**Auto-loads for**: Backend Developer, Solution Architect

**Acceptance Criteria**:
- [ ] base.md covers universal backend principles
- [ ] Each overlay has framework-specific patterns, project structure, error handling, testing conventions
- [ ] _generic.md provides reasonable fallback

---

### STGX-032: frontend-standards Skill
**Status**: TODO
**Files** (10 total):
- `skills/frontend-standards/SKILL.md`
- `skills/frontend-standards/base.md` — accessibility WCAG 2.1 AA, performance budgets, state management, component design
- `skills/frontend-standards/stacks/react-next.md`
- `skills/frontend-standards/stacks/react-vite.md`
- `skills/frontend-standards/stacks/vue-nuxt.md`
- `skills/frontend-standards/stacks/sveltekit.md`
- `skills/frontend-standards/stacks/angular.md`
- `skills/frontend-standards/stacks/astro.md`
- `skills/frontend-standards/stacks/html-tailwind.md`
- `skills/frontend-standards/stacks/_generic.md`

**Auto-loads for**: Frontend Developer, UX Designer (read-only)

---

### STGX-033: testing-standards Skill
**Status**: TODO
**Files** (11 total):
- `skills/testing-standards/SKILL.md`
- `skills/testing-standards/base.md` — test pyramid, AAA pattern, coverage philosophy, what to test vs what not to test
- `skills/testing-standards/stacks/jest-rtl.md`
- `skills/testing-standards/stacks/vitest.md`
- `skills/testing-standards/stacks/pytest.md`
- `skills/testing-standards/stacks/rspec.md`
- `skills/testing-standards/stacks/go-testing.md`
- `skills/testing-standards/stacks/junit5.md`
- `skills/testing-standards/stacks/xunit.md`
- `skills/testing-standards/stacks/playwright.md`
- `skills/testing-standards/stacks/_generic.md`

**Auto-loads for**: Test Case Specialist, Backend Dev, Frontend Dev
**BMAD Reuse**: Seed base.md from test-levels-framework.md + test-priorities-matrix.md (~70%)

---

### STGX-034: db-design Skill
**Status**: TODO
**Files** (10 total):
- `skills/db-design/SKILL.md`
- `skills/db-design/base.md` — normalisation, ACID, indexing principles, N+1 avoidance, migration safety
- `skills/db-design/stacks/postgresql.md`, `mysql.md`, `mongodb.md`, `sqlite.md`, `redis.md`, `dynamodb.md`, `cockroachdb.md`, `_generic.md`

**Auto-loads for**: Database Designer

---

### STGX-035: security-review Skill
**Status**: TODO
**Files** (9 total):
- `skills/security-review/SKILL.md` (context: fork — runs as Explore subagent)
- `skills/security-review/base.md` — OWASP Top 10, secrets detection, auth patterns, input validation
- `skills/security-review/stacks/python.md`, `node.md`, `rails.md`, `java.md`, `php.md`, `go.md`, `_generic.md`

**Auto-loads for**: Security Specialist (auto-loaded), Tech Lead Reviewer (cross-reference)

---

### STGX-036: api-design Skill
**Status**: TODO
**Files** (6 total):
- `skills/api-design/SKILL.md`
- `skills/api-design/base.md` — REST principles, versioning, error contracts, pagination
- `skills/api-design/stacks/rest-openapi.md`, `graphql.md`, `grpc-protobuf.md`, `websocket.md`, `_generic.md`

**Auto-loads for**: Solution Architect

---

### STGX-037: scalability-patterns Skill
**Status**: TODO
**Files** (6 total):
- `skills/scalability-patterns/SKILL.md`
- `skills/scalability-patterns/base.md` — caching strategy, async patterns, load balancing, database scaling
- `skills/scalability-patterns/stacks/aws.md`, `gcp.md`, `kubernetes.md`, `_generic.md`

**Auto-loads for**: Solution Architect, Tech Lead Reviewer, Backend Dev (on demand)

---

### STGX-038: migrations Skill
**Status**: TODO
**Files** (10 total):
- `skills/migrations/SKILL.md`
- `skills/migrations/base.md` — zero-downtime principles, rollback safety, idempotency
- `skills/migrations/stacks/alembic.md`, `flyway.md`, `liquibase.md`, `rails-activerecord.md`, `prisma.md`, `typeorm.md`, `gorm.md`, `goose.md`, `_generic.md`

**Auto-loads for**: Database Designer, Backend Developer (on demand for brownfield)

---

### STGX-039: infrastructure Skill
**Status**: TODO
**Files** (9 total):
- `skills/infrastructure/SKILL.md`
- `skills/infrastructure/base.md` — IaC principles, environment separation, secret management, observability
- `skills/infrastructure/stacks/docker-compose.md`, `kubernetes.md`, `terraform-aws.md`, `terraform-gcp.md`, `github-actions.md`, `gitlab-ci.md`, `circleci.md`, `_generic.md`

**Auto-loads for**: DevOps Engineer

---

### STGX-040: confluence-structure-guide Skill
**Status**: TODO
**Files** (2 total):
- `skills/confluence-structure-guide/SKILL.md`
- `skills/confluence-structure-guide/base.md` — space structure, page naming, cross-linking, label taxonomy

**Auto-loads for**: Technical Writer

---

### STGX-041: elicitation-methods Skill
**Status**: TODO
**Files** (2 total):
- `skills/elicitation-methods/SKILL.md`
- `skills/elicitation-methods/base.md` — 5-phase elicitation, question patterns, technique selection

**Auto-loads for**: Business Analyst
**BMAD Reuse**: base.md from data/elicitation-methods.md (~95% verbatim)

---

### STGX-042: UI UX Pro Max Installation
**Status**: TODO
**Description**: Install the external ui-ux-pro-max skill and wire it into the skills directory.

**Steps**:
1. `npm install -g uipro-cli`
2. `uipro init --ai claude`
3. Verify skill files appear in skills directory
4. Verify SKILL.md references scripts/search.py and data/ directory

**Auto-loads for**: UX Designer (auto-activates), Frontend Developer (read-only reference)

**Acceptance Criteria**:
- [ ] uipro-cli installed globally
- [ ] Skill files present in skills/ui-ux-pro-max/
- [ ] Python search engine runs successfully
- [ ] SKILL.md loader references correct paths

---

## Smoke Test (Phase 4 Complete)

1. Activate backend-dev agent on a Python FastAPI project
2. Verify it loads python-fastapi.md overlay (not generic)
3. Activate on a Go project — verify go-gin.md loads
4. Activate on unknown framework — verify _generic.md loads + flag set

## Definition of Done

- [ ] All 13 tickets completed (STGX-030 through STGX-042)
- [ ] Every SKILL.md follows the standard loader pattern
- [ ] Every skill has base.md + at least _generic.md overlay
- [ ] Multi-stack composition tested
- [ ] ui-ux-pro-max installed and functional
