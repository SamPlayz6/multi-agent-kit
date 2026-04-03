# Zero to AI Employees in 30 Minutes

## What You'll Build
A team of AI agents running in parallel, each with a specialized role: Manager, Builder, Sales, Social, and Operations. They coordinate through shared state files, work autonomously, and report progress to you.

## Prerequisites
- Claude Code CLI installed (`npm install -g @anthropic-ai/claude-code`)
- A terminal that supports multiple tabs/panes (iTerm2, tmux, Kitty, Windows Terminal)
- 5 minutes to customize templates

## Step 1: Install the Kit (2 minutes)

```bash
git clone https://github.com/SamPlayz6/multi-agent-kit.git
cd multi-agent-kit
chmod +x scripts/open-employee.sh
```

## Step 2: Customize Templates (10 minutes)

Each template in `templates/` is a CLAUDE.md file. Open each one and customize:

1. **Manager.md** — Set your business priorities and quality standards
2. **Builder.md** — Set your tech stack and coding standards  
3. **Sales.md** — Add your product details, pricing, and target audience
4. **Social.md** — Set your brand voice and platform preferences
5. **Operations.md** — List your deployed services and metrics to track

## Step 3: Set Up Your Master State (5 minutes)

Create `state/master-state.json`:

```json
{
  "priority": "Launch v2 of the product by Friday",
  "tasks": [
    {
      "id": "build-auth",
      "assigned_to": "builder",
      "description": "Add Google OAuth login",
      "status": "pending",
      "deadline": "2026-04-05"
    },
    {
      "id": "outreach-batch-1",
      "assigned_to": "sales",
      "description": "Email 20 prospects from the lead list",
      "status": "pending"
    }
  ],
  "blockers": []
}
```

## Step 4: Launch Your Team (5 minutes)

Open 5 terminal tabs and run one agent in each:

```bash
# Tab 1: Manager
./scripts/open-employee.sh manager .

# Tab 2: Builder  
./scripts/open-employee.sh builder ./my-project

# Tab 3: Sales
./scripts/open-employee.sh sales .

# Tab 4: Social
./scripts/open-employee.sh social .

# Tab 5: Operations
./scripts/open-employee.sh ops .
```

## Step 5: Monitor with Watcher (1 minute)

In a 6th tab, run the team dashboard:

```bash
python3 scripts/watcher.py --interval 30
```

This shows all agents' status in real-time, refreshing every 30 seconds.

## How It Works

1. **Manager** reads master-state.json and assigns tasks to agents
2. Each agent reads their status.json, does the work, saves progress
3. When done, agent sets status to "review"
4. Manager reviews, approves or sends back
5. You check in when you want — the team runs without you

## Key Concepts

### State Files
All coordination happens through JSON files. No databases, no APIs, no complexity.

### Session Continuity
Claude Code sessions end. That's fine. Each agent saves handoff notes before stopping. The next session reads those notes and continues seamlessly.

### Quality Gates
Nothing goes to "done" without Manager review. This prevents agents from marking mediocre work as complete.

### The Human Loop
You're not out of the loop — you're elevated to CEO level. Review summaries, make strategic decisions, let agents handle execution.

## Troubleshooting

**Agent isn't picking up tasks:** Check if master-state.json has tasks assigned to that agent name.

**Agent keeps restarting from scratch:** Make sure status.json and handoff notes are being saved. Check the template includes the session continuity protocol.

**Quality is poor:** Tighten the acceptance criteria in task specs. Add specific examples of what "good" looks like.
