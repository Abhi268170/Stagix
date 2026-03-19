# Kubernetes Patterns

## Specifics
- HPA (Horizontal Pod Autoscaler) based on CPU/memory/custom metrics
- Resource requests and limits on all containers
- PodDisruptionBudgets for availability during rollouts
- Readiness and liveness probes
- Service mesh (Istio/Linkerd) for observability and traffic management
