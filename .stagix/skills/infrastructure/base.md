# Infrastructure Standards — Universal Principles

## IaC Principles
- All infrastructure defined in code (Terraform, CloudFormation, Pulumi)
- No manual changes in cloud consoles — drift detection enabled
- State stored remotely with locking (S3 + DynamoDB, GCS + Cloud Storage)
- Modules for reusable patterns

## Container Best Practices
- Multi-stage builds (separate build and runtime images)
- Non-root user in production containers
- Minimal base images (alpine, distroless)
- Health check endpoints defined in Dockerfile
- .dockerignore excludes node_modules, .git, tests, docs

## Environment Separation
- Dev, staging, production as separate environments
- Same Docker image across all environments (config via env vars)
- Staging mirrors production (same resources, same config, smaller scale)

## Secret Management
- Secrets in environment variables or secret managers (AWS Secrets Manager, Vault)
- Never in code, config files, or Docker images
- Rotate secrets on a schedule
- Separate secrets per environment

## CI/CD Pipeline Structure
- Lint → Test → Build → Deploy (in order, fail fast)
- Tests run in parallel where possible
- Deploy to staging automatically, production manually (or with approval)
- Rollback procedure documented and tested

## Observability
- Structured logging (JSON) to centralised log system
- Metrics: request rate, error rate, latency (RED method)
- Health check endpoints: `/health` (basic) and `/ready` (dependencies)
- Alerting on error rate spikes and latency thresholds
