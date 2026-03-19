# Node.js Security

## Stack-Specific Risks
- Prototype pollution: freeze prototypes, validate object keys
- eval() and new Function(): never with user input
- RegExp DoS (ReDoS): avoid catastrophic backtracking
- npm supply chain: lock versions, audit regularly
- Express: helmet middleware, disable x-powered-by
- Mass assignment: whitelist allowed fields explicitly
