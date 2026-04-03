# Multi-Agent Orchestration Kit for Claude Code

Run multiple Claude Code agents as autonomous "AI employees" that coordinate through shared state files, work in parallel, and report progress to you.

## What's Inside

### Agent Templates (CLAUDE.md files)
| Agent | Role |
|-------|------|
| **Manager** | Coordinates the team, assigns tasks, reviews quality |
| **Builder** | Writes code, builds features, deploys |
| **Sales** | Outreach, lead tracking, customer communication |
| **Social** | Content creation, social media management |
| **Operations** | Monitoring, metrics, maintenance |

### Scripts
- `open-employee.sh` — Launch any agent in a new terminal
- `watcher.py` — Real-time team dashboard showing all agent statuses

### Guide
- Zero to AI Employees in 30 Minutes — step-by-step setup

## Quick Start

```bash
git clone https://github.com/SamPlayz6/multi-agent-kit.git
cd multi-agent-kit
chmod +x scripts/open-employee.sh

# Launch the Manager agent
./scripts/open-employee.sh manager ./my-project

# In another terminal, launch the Builder
./scripts/open-employee.sh builder ./my-project

# Monitor your team
python3 scripts/watcher.py
```

## How It Works

1. Each agent runs in its own Claude Code session with a specialized CLAUDE.md
2. Agents coordinate through JSON state files (no database needed)
3. Manager assigns tasks, reviews work, and maintains quality gates
4. Sessions save handoff notes so work continues across restarts
5. You check in when you want — the team runs without you

## Customization

Edit each template in `templates/` to match your business:
- Set your tech stack in Builder.md
- Add your product details in Sales.md
- Define your brand voice in Social.md
- List your services in Operations.md

## License

MIT — use it however you want.

## Full Version

This repo contains the core templates. The full kit ($79-149) includes additional templates, the team dashboard, quality gate scoring system, and video walkthrough.
