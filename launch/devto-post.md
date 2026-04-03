# How I Run 4 AI Employees with Claude Code (Free Template)

I've been running a team of AI agents as autonomous "employees" for the past month. They build code, write content, do outreach, and monitor my products while I focus on strategy. Here's how it works and a free template to try it yourself.

## The Setup

Each agent runs in its own Claude Code session with a specialized CLAUDE.md file that defines its role, responsibilities, and workflow. They coordinate through shared JSON state files.

**The agents:**
- **Manager** coordinates everyone, assigns tasks, reviews quality
- **Builder** writes code, builds features, deploys
- **Sales** handles outreach, tracks leads, follows up
- **Social** creates content, manages posting schedule
- **Operations** monitors services, tracks metrics, handles maintenance

## How They Coordinate

No database. No API. Just JSON files.

```
state/
  master-state.json        # Team priorities and task queue
  agents/
    builder/status.json    # Builder's current task and progress
    sales/status.json      # Sales pipeline status
    ...
```

The Manager agent reads everyone's status, assigns work, and reviews deliverables. Each agent reads their own status file, does the work, and updates their progress.

## Session Continuity

The key insight: Claude Code sessions end unpredictably. So every agent saves detailed handoff notes before each major step. When a new session starts, it reads those notes and continues from exactly where it left off.

This is the difference between "AI assistant" and "AI employee." An assistant helps when you ask. An employee works when you're not looking.

## The Free Template

I've open-sourced the basic Manager template. Drop this into your project as CLAUDE.md:

```markdown
# Manager Agent

You coordinate all other agents. Read master-state.json first every session.

## Session Protocol
1. Read master-state.json for priorities
2. Check each agent's status.json
3. Review completed work against quality criteria
4. Assign next tasks to idle agents
5. Update master-state.json
6. Write daily status summary

## Quality Gates
Before marking any work "done":
- Meets acceptance criteria
- No obvious errors
- Tested where applicable
```

## What I Use It For

In the last month, this system has:
- Built and deployed 3 web applications
- Written launch materials for each
- Monitored uptime and tracked metrics
- Created social media content

All while I focused on product strategy and customer conversations.

## Want the Full System?

The free template above is the Manager agent only. The full kit includes all 5 agent templates, orchestration scripts, a real-time team dashboard, quality gate system, and a setup guide that gets you running in 30 minutes.

[Get the full Multi-Agent Kit →](https://gumroad.com/l/multi-agent-kit)

---

*What's your experience with multi-agent Claude Code setups? I'd love to hear what's working for others.*
