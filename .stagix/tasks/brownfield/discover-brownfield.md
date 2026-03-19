# Task: discover-brownfield

## Purpose

Comprehensive codebase analysis protocol for the Codebase Archaeologist. Produces a 12-section discovery report that all subsequent planning agents read as their first input.

## Prerequisites

- Project mode set to `brownfield` in core-config.yaml
- Codebase exists with source files

## Protocol

### Step 1: Initial Scan
- Use Glob to inventory all file types and directory structure
- Count files by extension to understand project composition
- Identify entry points (main files, index files, app files)

### Step 2: Dependency Analysis
- Read lock files (package-lock.json, poetry.lock, Gemfile.lock, go.sum)
- Identify exact versions in use (not just declared ranges)
- Flag deprecated or known-vulnerable dependencies

### Step 3: Architecture Discovery
- Read entry points and trace the application structure
- Identify layers (routes → controllers → services → repositories → models)
- Map module boundaries and inter-module dependencies
- Use Grep to find import patterns and dependency chains

### Step 4: Pattern Extraction
- Use Grep to find error handling patterns across the codebase
- Identify auth implementation (search for auth, jwt, session, cookie)
- Document naming conventions (observe, don't assume)
- Find configuration patterns (env vars, config files)

### Step 5: Tech Debt Assessment
- Find large files (>500 lines) using Glob + Read to check line counts
- Use Grep for TODO, FIXME, HACK, WORKAROUND comments
- Identify code duplication patterns
- Check for missing validation (search for unvalidated user inputs)
- Look for security anti-patterns (hardcoded strings that look like secrets)

### Step 6: Test Coverage Assessment
- Find all test files using Glob (test_*, *_test.*, *.spec.*, *.test.*)
- Map which source files have corresponding test files
- Identify modules with zero test coverage
- Read test configuration (jest.config, pytest.ini, etc.)

### Step 7: External Integration Map
- Grep for HTTP client calls (fetch, axios, requests, http.Get)
- Grep for database connection strings and ORM configurations
- Find environment variable usage (process.env, os.environ, os.Getenv)
- Identify webhook endpoints (both consumed and produced)

### Step 8: Database Schema Extraction
- Read ORM model definitions or migration files
- Map actual schema from code (not from docs that may be outdated)
- Identify schema drift between migrations and model definitions

### Step 9: Deployment Discovery
- Read Dockerfile, docker-compose.yml
- Read CI/CD configuration (.github/workflows/, .gitlab-ci.yml)
- Identify environment configuration patterns

### Step 10: Report Assembly
Write the complete 12-section report to `.stagix/docs/brownfield-discovery.md` following the structure defined in the Codebase Archaeologist agent definition.

## Output

`.stagix/docs/brownfield-discovery.md` — the 12-section discovery report.

## Quality Criteria

- Every claim cites specific files or patterns
- Tech debt is categorised (Critical/High/Medium/Accepted)
- No recommendations — just facts (planning agents will recommend)
- Completeness: all 12 sections substantive, no placeholders
