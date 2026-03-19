#!/usr/bin/env node

import { execSync, spawnSync } from "child_process";
import { existsSync, cpSync, mkdirSync, writeFileSync, readFileSync, chmodSync } from "fs";
import { join, dirname, resolve } from "path";
import { fileURLToPath } from "url";
import { createInterface } from "readline";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const STAGIX_SOURCE = join(__dirname, "..", ".stagix");
const VERSION = "1.0.0";

const CYAN = "\x1b[36m";
const GREEN = "\x1b[32m";
const YELLOW = "\x1b[33m";
const RED = "\x1b[31m";
const NC = "\x1b[0m";

function ask(question) {
  const rl = createInterface({ input: process.stdin, output: process.stdout });
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer.trim());
    });
  });
}

async function install(targetDir) {
  const target = resolve(targetDir || ".");

  console.log(`${CYAN}`);
  console.log("  ╔═══════════════════════════════════════════╗");
  console.log(`  ║         STAGIX Installer v${VERSION}          ║`);
  console.log("  ║   AI-Native Agile Development System      ║");
  console.log("  ╚═══════════════════════════════════════════╝");
  console.log(`${NC}`);

  // Check prerequisites
  console.log("Checking prerequisites...");
  for (const cmd of ["node", "python3", "git"]) {
    try {
      execSync(`which ${cmd}`, { stdio: "pipe" });
    } catch {
      console.error(`${RED}Error: ${cmd} is required but not installed.${NC}`);
      process.exit(1);
    }
  }
  console.log(`${GREEN}All prerequisites met.${NC}\n`);

  // Project config
  console.log(`${YELLOW}── Project Configuration ──${NC}`);
  const projectName = await ask("Project name: ");
  const jiraKey = await ask("Jira project key (e.g., PROJ): ");
  const confluenceSpace = await ask("Confluence space key: ");

  // Copy .stagix/
  console.log("\nCopying .stagix/ directory...");
  const destStagix = join(target, ".stagix");
  if (existsSync(destStagix)) {
    console.log(`${YELLOW}Warning: .stagix/ already exists. Skipping copy.${NC}`);
  } else {
    cpSync(STAGIX_SOURCE, destStagix, { recursive: true });
  }

  // Write .env template (user fills in credentials)
  const envPath = join(destStagix, ".env");
  if (!existsSync(envPath)) {
    const envTemplate = [
      "# Stagix Atlassian Credentials",
      "# Fill in your values below. DO NOT COMMIT this file.",
      "#",
      "# To get an API token: https://id.atlassian.com/manage-profile/security/api-tokens",
      "#",
      "JIRA_URL=https://yourorg.atlassian.net",
      "JIRA_EMAIL=your-email@example.com",
      "JIRA_API_TOKEN=your-api-token-here",
      "CONFLUENCE_URL=https://yourorg.atlassian.net",
      "CONFLUENCE_EMAIL=your-email@example.com",
      "CONFLUENCE_API_TOKEN=your-api-token-here",
    ].join("\n");

    writeFileSync(envPath, envTemplate, { mode: 0o600 });
  }

  // Update .gitignore
  const gitignorePath = join(target, ".gitignore");
  const gitignoreEntries = "\n# Stagix\n.stagix/.env\n.stagix/qa/evidence/\n.stagix/state/\n.stagix/security-events.log\n";
  if (existsSync(gitignorePath)) {
    const content = readFileSync(gitignorePath, "utf-8");
    if (!content.includes(".stagix/.env")) {
      writeFileSync(gitignorePath, content + gitignoreEntries);
    }
  } else {
    writeFileSync(gitignorePath, gitignoreEntries);
  }

  // Substitute placeholders
  console.log("Substituting project placeholders...");
  for (const file of ["CLAUDE.md", "core-config.yaml"]) {
    const filePath = join(destStagix, file);
    if (existsSync(filePath)) {
      let content = readFileSync(filePath, "utf-8");
      content = content.replace(/{PROJECT_NAME}/g, projectName);
      content = content.replace(/{JIRA_KEY}/g, jiraKey);
      content = content.replace(/{CONFLUENCE_SPACE}/g, confluenceSpace);
      writeFileSync(filePath, content);
    }
  }

  // Copy CLAUDE.md to project root
  cpSync(join(destStagix, "CLAUDE.md"), join(target, "CLAUDE.md"));

  // Initialize state files
  writeFileSync(
    join(destStagix, "state", "pipeline-log.json"),
    JSON.stringify({ project: projectName, mode: null, events: [] }, null, 2)
  );
  writeFileSync(
    join(destStagix, "state", "active-agent.json"),
    JSON.stringify({ agent: null, agent_file: null, group: null, started_at: null, story_key: null }, null, 2)
  );

  // Make hooks executable
  const hooksDir = join(destStagix, "hooks");
  for (const sub of ["pre-tool-use", "post-tool-use", "stop", "task-completed", "subagent-stop"]) {
    const subDir = join(hooksDir, sub);
    if (existsSync(subDir)) {
      const files = execSync(`find "${subDir}" -name "*.py"`, { encoding: "utf-8" }).trim().split("\n");
      for (const f of files) {
        if (f) chmodSync(f, 0o755);
      }
    }
  }

  console.log(`\n${GREEN}╔═══════════════════════════════════════════╗${NC}`);
  console.log(`${GREEN}║       Stagix installed successfully!      ║${NC}`);
  console.log(`${GREEN}╚═══════════════════════════════════════════╝${NC}`);
  console.log(`
${YELLOW}Step 1:${NC} Add your Atlassian credentials:

  ${CYAN}Edit ${join(destStagix, ".env")}${NC}

  Fill in JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN
  (Get a token at: https://id.atlassian.com/manage-profile/security/api-tokens)

${YELLOW}Step 2:${NC} Launch Claude Code with Stagix:

  ${CYAN}cd ${target}${NC}
  ${CYAN}claude --plugin-dir .stagix${NC}

${YELLOW}Step 3:${NC} Start building:

  ${CYAN}/start-project "your project idea"${NC}

  Or for an existing codebase:
  ${CYAN}/discover-brownfield${NC}
`);
}

function usage() {
  console.log(`
${CYAN}stagix${NC} — AI-Native Agile Development Orchestration System

${YELLOW}Usage:${NC}
  stagix install [target-dir]   Install .stagix/ into a project
  stagix run                    Launch Claude Code with Stagix plugin loaded
  stagix --help                 Show this help

${YELLOW}Quick start:${NC}
  npx stagix install .          Install into current directory
  npx stagix run                Launch Claude Code with --plugin-dir .stagix

${YELLOW}What you get:${NC}
  14 specialist agents (BA, PM, UX, Architect, DB, Writer, SM, + 7 engineering)
  7 slash commands (/start-project, /implement-story, /approve, /reject, etc.)
  12 skill domains with 65+ tech stack overlays
  8 enforcement hooks (git commit blocking, file scope, linting, gates)
  Full Jira + Confluence + Playwright integration
`);
}

// Parse args
const args = process.argv.slice(2);
const command = args[0];

switch (command) {
  case "install":
    install(args[1]).catch((err) => {
      console.error(`${RED}Error: ${err.message}${NC}`);
      process.exit(1);
    });
    break;

  case "run":
    console.log("Launching Claude Code with Stagix plugin...\n");
    const result = spawnSync("claude", ["--plugin-dir", ".stagix"], {
      stdio: "inherit",
      cwd: process.cwd(),
    });
    process.exit(result.status || 0);
    break;

  case "--help":
  case "-h":
  case "help":
  case undefined:
    usage();
    break;

  default:
    console.error(`${RED}Unknown command: ${command}${NC}`);
    usage();
    process.exit(1);
}
