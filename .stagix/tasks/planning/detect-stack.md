# Task: detect-stack

## Purpose

Determine the project's tech stack and mode (greenfield/brownfield) by reading signal files. Writes results to `.stagix/core-config.yaml`. Runs as the very first step of `/start-project`, before any agent is activated.

## Execution

This task is executed by the `/start-project` command, not by an agent. It reads the filesystem and updates config.

## Signal Files to Check

| Signal File | What to Detect |
|---|---|
| `package.json` | Node.js/TypeScript. Check dependencies for: next, nuxt, svelte, react, vue, angular (frontend); express, @nestjs/core, fastify (backend). Check devDependencies for: jest, vitest (testing). |
| `requirements.txt` / `pyproject.toml` | Python. Check for: fastapi, django, flask (backend); sqlalchemy, alembic (DB); pytest (testing); celery (async). |
| `Gemfile` | Ruby. Check for: rails, sinatra (backend); rspec, sidekiq, devise. |
| `go.mod` | Go. Check for: gin-gonic, echo (backend); gorm (ORM); testify (testing). |
| `pom.xml` / `build.gradle` | Java/Kotlin. Check for: spring-boot, hibernate (backend); junit (testing). |
| `composer.json` | PHP. Check for: laravel, symfony. |
| `Cargo.toml` | Rust. Check for: actix-web, tokio, sqlx. |
| `Dockerfile` | Container stack. Read FROM line to identify base image. |
| `.github/workflows/*.yml` | CI stack. Identify GitHub Actions configuration. |
| `terraform/**` | Infrastructure stack. Check for AWS, GCP, Azure provider. |

## Mode Detection

### Greenfield Indicators
- No source files beyond config files (package.json, requirements.txt, etc.)
- Git log has 0-1 commits
- No existing test files
- No existing database migration files

### Brownfield Indicators
- Source files exist (*.py, *.js, *.ts, *.go, *.rb, *.java, *.rs, *.php)
- Git log has >1 commit
- Existing test files present
- Existing migration files present

If ambiguous, default to greenfield. The human can override by editing `core-config.yaml` before running `/start-project`.

## Output

Write results to `.stagix/core-config.yaml` under:
- `project.mode`: `greenfield` or `brownfield`
- `detected_stack.frontend.framework`: e.g., `react-next`, `vue-nuxt`
- `detected_stack.backend.framework`: e.g., `python-fastapi`, `node-express`
- `detected_stack.database.primary`: e.g., `postgresql`, `mongodb`
- `detected_stack.testing.unit`: e.g., `pytest`, `jest-rtl`
- `detected_stack.infrastructure.ci`: e.g., `github-actions`
- `detected_stack.package_managers`: e.g., `[npm, pip]`

Only set values that are definitively detected. Leave null for undetected components — agents will handle this gracefully (SKILL.md loader falls back to `_generic.md`).
