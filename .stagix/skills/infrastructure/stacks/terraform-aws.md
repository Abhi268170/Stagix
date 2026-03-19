# Terraform + AWS

## Conventions
- Modules: vpc, ecs/eks, rds, elasticache, s3
- Remote state in S3 + DynamoDB locking
- Workspaces or directories per environment
- Data sources for existing resources
- Tagging: Name, Environment, Project, ManagedBy=terraform
