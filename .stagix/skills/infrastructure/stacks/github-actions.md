# GitHub Actions

## Conventions
- Workflow per concern: ci.yml, deploy.yml, release.yml
- Reusable workflows for shared steps
- Branch protection: require CI pass before merge
- Secrets via GitHub Secrets (not hardcoded)
- Matrix builds for multiple versions/platforms
