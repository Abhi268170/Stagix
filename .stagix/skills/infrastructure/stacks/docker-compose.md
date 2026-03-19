# Docker Compose

## Conventions
- Services: app, db, cache, worker (as needed)
- Named volumes for persistent data
- Health checks on all services
- .env file for environment-specific config
- Override files: docker-compose.override.yml for dev
