#!/usr/bin/env bash
set -euo pipefail

# Stagix Installer
# Copies .stagix/ into a target project, configures credentials, and runs detect-stack.

STAGIX_VERSION="1.0.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}"
echo "  ╔═══════════════════════════════════════════╗"
echo "  ║         STAGIX Installer v${STAGIX_VERSION}          ║"
echo "  ║   AI-Native Agile Development System      ║"
echo "  ╚═══════════════════════════════════════════╝"
echo -e "${NC}"

# ─── Prerequisites ─────────────────────────────────────────────────────────────

check_prereq() {
  if ! command -v "$1" &> /dev/null; then
    echo -e "${RED}Error: $1 is required but not installed.${NC}"
    echo "  Install it and re-run this script."
    exit 1
  fi
}

echo "Checking prerequisites..."
check_prereq "node"
check_prereq "python3"
check_prereq "git"
check_prereq "jq"

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
  echo -e "${RED}Error: Node.js >= 18 required. Found: $(node -v)${NC}"
  exit 1
fi

echo -e "${GREEN}All prerequisites met.${NC}"

# ─── Target Directory ──────────────────────────────────────────────────────────

TARGET_DIR="${1:-.}"
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

if [ ! -d "$TARGET_DIR" ]; then
  echo -e "${RED}Error: Target directory '$TARGET_DIR' does not exist.${NC}"
  exit 1
fi

echo ""
echo -e "Installing Stagix into: ${CYAN}${TARGET_DIR}${NC}"

# ─── Project Configuration ─────────────────────────────────────────────────────

echo ""
echo -e "${YELLOW}── Project Configuration ──${NC}"

read -rp "Project name: " PROJECT_NAME
read -rp "Jira project key (e.g., PROJ): " JIRA_KEY
read -rp "Confluence space key (e.g., PROJ): " CONFLUENCE_SPACE

# ─── Copy .stagix/ Directory ───────────────────────────────────────────────────

echo ""
echo "Copying .stagix/ directory..."

if [ -d "$TARGET_DIR/.stagix" ]; then
  echo -e "${YELLOW}Warning: .stagix/ already exists. Merging (existing files preserved).${NC}"
  cp -rn "$SCRIPT_DIR/" "$TARGET_DIR/.stagix/" 2>/dev/null || true
else
  cp -r "$SCRIPT_DIR" "$TARGET_DIR/.stagix"
fi

# ─── Write .env Template ──────────────────────────────────────────────────────

ENV_FILE="$TARGET_DIR/.stagix/.env"
if [ ! -f "$ENV_FILE" ]; then
  echo "Creating .env template..."
  cat > "$ENV_FILE" << 'ENVEOF'
# Stagix Atlassian Credentials
# Fill in your values below. DO NOT COMMIT this file.
#
# To get an API token: https://id.atlassian.com/manage-profile/security/api-tokens
#
JIRA_URL=https://yourorg.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token-here
CONFLUENCE_URL=https://yourorg.atlassian.net
CONFLUENCE_EMAIL=your-email@example.com
CONFLUENCE_API_TOKEN=your-api-token-here
ENVEOF
  chmod 600 "$ENV_FILE"
else
  echo -e "${YELLOW}.env already exists — skipping.${NC}"
fi

# ─── Update .gitignore ─────────────────────────────────────────────────────────

GITIGNORE="$TARGET_DIR/.gitignore"
if [ -f "$GITIGNORE" ]; then
  if ! grep -q ".stagix/.env" "$GITIGNORE" 2>/dev/null; then
    echo "" >> "$GITIGNORE"
    echo "# Stagix credentials" >> "$GITIGNORE"
    echo ".stagix/.env" >> "$GITIGNORE"
    echo ".stagix/qa/evidence/" >> "$GITIGNORE"
    echo ".stagix/state/" >> "$GITIGNORE"
  fi
else
  cat > "$GITIGNORE" << GIEOF
# Stagix credentials
.stagix/.env
.stagix/qa/evidence/
.stagix/state/
GIEOF
fi

# ─── Substitute Placeholders ───────────────────────────────────────────────────

echo "Substituting project placeholders..."

# CLAUDE.md
sed -i "s/{PROJECT_NAME}/${PROJECT_NAME}/g" "$TARGET_DIR/.stagix/CLAUDE.md"
sed -i "s/{JIRA_KEY}/${JIRA_KEY}/g" "$TARGET_DIR/.stagix/CLAUDE.md"
sed -i "s/{CONFLUENCE_SPACE}/${CONFLUENCE_SPACE}/g" "$TARGET_DIR/.stagix/CLAUDE.md"

# core-config.yaml
sed -i "s/{PROJECT_NAME}/${PROJECT_NAME}/g" "$TARGET_DIR/.stagix/core-config.yaml"
sed -i "s/{JIRA_KEY}/${JIRA_KEY}/g" "$TARGET_DIR/.stagix/core-config.yaml"
sed -i "s/{CONFLUENCE_SPACE}/${CONFLUENCE_SPACE}/g" "$TARGET_DIR/.stagix/core-config.yaml"

# plugin.json — replace env var placeholders for MCP servers
# The plugin system uses ${CLAUDE_PLUGIN_ROOT} at runtime for hook paths (no substitution needed)
# But MCP server env vars need actual values in .env (loaded by the shell)
# plugin.json references ${JIRA_URL} etc. which are resolved from the environment at runtime

# ─── Copy CLAUDE.md to Project Root ────────────────────────────────────────────

echo "Copying CLAUDE.md to project root..."
cp "$TARGET_DIR/.stagix/CLAUDE.md" "$TARGET_DIR/CLAUDE.md"

# ─── Create Directory Structure ────────────────────────────────────────────────

echo "Creating directory structure..."

directories=(
  ".stagix/agents/planning"
  ".stagix/agents/engineering"
  ".stagix/tasks/planning"
  ".stagix/tasks/engineering"
  ".stagix/tasks/brownfield"
  ".stagix/templates"
  ".stagix/checklists"
  ".stagix/skills"
  ".stagix/hooks/pre-tool-use"
  ".stagix/hooks/post-tool-use"
  ".stagix/hooks/stop"
  ".stagix/hooks/task-completed"
  ".stagix/hooks/subagent-stop"
  ".stagix/commands/start-project"
  ".stagix/commands/implement-story"
  ".stagix/commands/approve"
  ".stagix/commands/reject"
  ".stagix/commands/review-handoff"
  ".stagix/commands/status"
  ".stagix/commands/discover-brownfield"
  ".stagix/workflows"
  ".stagix/modes"
  ".stagix/gates"
  ".stagix/state"
  ".stagix/baselines"
  ".stagix/tests"
  ".stagix/qa/evidence"
  ".stagix/qa/reports"
  ".stagix/docs"
  ".stagix/docs/architecture"
  ".stagix/design-system"
  ".stagix/design-system/pages"
)

for dir in "${directories[@]}"; do
  mkdir -p "$TARGET_DIR/$dir"
done

# ─── Initialize State Files ────────────────────────────────────────────────────

echo "Initializing state files..."

cat > "$TARGET_DIR/.stagix/state/active-agent.json" << 'STATEEOF'
{
  "agent": null,
  "group": null,
  "started_at": null,
  "story_key": null
}
STATEEOF

cat > "$TARGET_DIR/.stagix/state/pipeline-log.json" << 'LOGEOF'
{
  "project": null,
  "mode": null,
  "events": []
}
LOGEOF

# Update pipeline-log with project name
python3 -c "
import json
with open('$TARGET_DIR/.stagix/state/pipeline-log.json', 'r') as f:
    data = json.load(f)
data['project'] = '$PROJECT_NAME'
with open('$TARGET_DIR/.stagix/state/pipeline-log.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# ─── Add .gitkeep to Empty Directories ─────────────────────────────────────────

for dir in gates baselines "qa/evidence" "qa/reports" tests; do
  touch "$TARGET_DIR/.stagix/$dir/.gitkeep"
done

# ─── Detect Stack ──────────────────────────────────────────────────────────────

echo ""
echo -e "${YELLOW}── Detecting Tech Stack ──${NC}"

# This is a simplified detect-stack. The full task file (tasks/planning/detect-stack.md)
# provides the comprehensive protocol for the agent.

detect_stack() {
  local dir="$1"
  local mode="greenfield"
  local backend_framework=""
  local frontend_framework=""
  local database=""
  local test_framework=""

  # Check for existing source files → brownfield
  local source_count
  source_count=$(find "$dir" -maxdepth 3 -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.go" -o -name "*.rb" -o -name "*.java" -o -name "*.rs" -o -name "*.php" 2>/dev/null | head -20 | wc -l)
  if [ "$source_count" -gt 5 ]; then
    mode="brownfield"
  fi

  # package.json
  if [ -f "$dir/package.json" ]; then
    local pkg
    pkg=$(cat "$dir/package.json")
    if echo "$pkg" | jq -e '.dependencies["next"]' &>/dev/null; then frontend_framework="react-next"
    elif echo "$pkg" | jq -e '.dependencies["nuxt"]' &>/dev/null; then frontend_framework="vue-nuxt"
    elif echo "$pkg" | jq -e '.dependencies["svelte"]' &>/dev/null; then frontend_framework="sveltekit"
    elif echo "$pkg" | jq -e '.dependencies["react"]' &>/dev/null; then frontend_framework="react-vite"
    elif echo "$pkg" | jq -e '.dependencies["vue"]' &>/dev/null; then frontend_framework="vue-nuxt"
    elif echo "$pkg" | jq -e '.dependencies["angular"]' &>/dev/null; then frontend_framework="angular"
    fi

    if echo "$pkg" | jq -e '.dependencies["express"]' &>/dev/null; then backend_framework="node-express"
    elif echo "$pkg" | jq -e '.dependencies["@nestjs/core"]' &>/dev/null; then backend_framework="node-nestjs"
    elif echo "$pkg" | jq -e '.dependencies["fastify"]' &>/dev/null; then backend_framework="node-fastify"
    fi

    if echo "$pkg" | jq -e '.devDependencies["jest"]' &>/dev/null; then test_framework="jest-rtl"
    elif echo "$pkg" | jq -e '.devDependencies["vitest"]' &>/dev/null; then test_framework="vitest"
    fi
  fi

  # requirements.txt / pyproject.toml
  if [ -f "$dir/requirements.txt" ] || [ -f "$dir/pyproject.toml" ]; then
    local pyfiles="${dir}/requirements.txt ${dir}/pyproject.toml"
    if grep -ql "fastapi" $pyfiles 2>/dev/null; then backend_framework="python-fastapi"
    elif grep -ql "django" $pyfiles 2>/dev/null; then backend_framework="python-django"
    elif grep -ql "flask" $pyfiles 2>/dev/null; then backend_framework="python-flask"
    fi
    if grep -ql "pytest" $pyfiles 2>/dev/null; then test_framework="pytest"; fi
    if grep -ql "sqlalchemy\|psycopg" $pyfiles 2>/dev/null; then database="postgresql"; fi
  fi

  # go.mod
  if [ -f "$dir/go.mod" ]; then
    if grep -q "gin-gonic" "$dir/go.mod"; then backend_framework="go-gin"
    elif grep -q "echo" "$dir/go.mod"; then backend_framework="go-echo"
    fi
    test_framework="go-testing"
  fi

  # Gemfile
  if [ -f "$dir/Gemfile" ]; then
    if grep -q "rails" "$dir/Gemfile"; then backend_framework="rails"; fi
    if grep -q "rspec" "$dir/Gemfile"; then test_framework="rspec"; fi
  fi

  echo "  Mode: $mode"
  echo "  Backend: ${backend_framework:-not detected}"
  echo "  Frontend: ${frontend_framework:-not detected}"
  echo "  Database: ${database:-not detected}"
  echo "  Testing: ${test_framework:-not detected}"

  # Write to core-config.yaml using python for safe YAML manipulation
  python3 -c "
import re

with open('$TARGET_DIR/.stagix/core-config.yaml', 'r') as f:
    content = f.read()

replacements = {
    '  mode: null': '  mode: $mode',
}

backend = '$backend_framework'
frontend = '$frontend_framework'
db = '$database'
testing = '$test_framework'

if backend:
    content = re.sub(r'(backend:\n\s+framework:) null', r'\1 ' + backend, content)
if frontend:
    content = re.sub(r'(frontend:\n\s+framework:) null', r'\1 ' + frontend, content)
if db:
    content = re.sub(r'(database:\n\s+primary:) null', r'\1 ' + db, content)
if testing:
    content = re.sub(r'(testing:\n\s+unit:) null', r'\1 ' + testing, content)

content = content.replace('  mode: null', '  mode: $mode')

with open('$TARGET_DIR/.stagix/core-config.yaml', 'w') as f:
    f.write(content)
"
}

detect_stack "$TARGET_DIR"

# ─── Done ──────────────────────────────────────────────────────────────────────

echo ""
echo -e "${GREEN}╔═══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║         Stagix installed successfully!    ║${NC}"
echo -e "${GREEN}╚═══════════════════════════════════════════╝${NC}"
echo ""
echo -e "Next steps:"
echo ""
echo -e "  ${YELLOW}Step 1:${NC} Add your Atlassian credentials:"
echo -e "    ${CYAN}Edit $TARGET_DIR/.stagix/.env${NC}"
echo "    Fill in JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN"
echo "    Get a token at: https://id.atlassian.com/manage-profile/security/api-tokens"
echo ""
echo -e "  ${YELLOW}Step 2:${NC} Launch Claude Code with Stagix:"
echo -e "    ${CYAN}cd $TARGET_DIR${NC}"
echo -e "    ${CYAN}claude --plugin-dir .stagix${NC}"
echo ""
echo -e "  ${YELLOW}Step 3:${NC} Start building:"
echo -e "    ${CYAN}/start-project \"your project idea\"${NC}"
echo ""
echo "    Or for an existing codebase:"
echo -e "    ${CYAN}/discover-brownfield${NC}"
echo ""
