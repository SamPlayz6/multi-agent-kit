#!/usr/bin/env python3
"""
Agent Watcher — monitors all agent status files and provides a team overview.
Run: python3 watcher.py [--interval 30]
"""

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

STATE_DIR = Path(__file__).parent.parent / "state"
AGENTS = ["manager", "builder", "sales", "social", "ops"]

STATUS_COLORS = {
    "idle": "\033[90m",      # gray
    "working": "\033[34m",   # blue
    "review": "\033[33m",    # yellow
    "blocked": "\033[31m",   # red
    "done": "\033[32m",      # green
}
RESET = "\033[0m"
BOLD = "\033[1m"


def read_status(agent: str) -> dict:
    path = STATE_DIR / "agents" / agent / "status.json"
    if not path.exists():
        return {"agent": agent, "status": "not-started", "current_task": None}
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"agent": agent, "status": "error", "current_task": None}


def read_master_state() -> dict:
    path = STATE_DIR / "master-state.json"
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def display():
    os.system("clear" if os.name != "nt" else "cls")

    print(f"{BOLD}{'='*60}{RESET}")
    print(f"{BOLD}  AI Employee Team Dashboard{RESET}")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{BOLD}{'='*60}{RESET}\n")

    master = read_master_state()
    if master.get("priority"):
        print(f"  Priority: {master['priority']}\n")

    # Agent status table
    print(f"  {'Agent':<12} {'Status':<12} {'Task':<35}")
    print(f"  {'-'*12} {'-'*12} {'-'*35}")

    active_count = 0
    for agent_name in AGENTS:
        status = read_status(agent_name)
        s = status.get("status", "unknown")
        color = STATUS_COLORS.get(s, "")
        task = status.get("current_task") or "—"
        if len(task) > 33:
            task = task[:30] + "..."

        if s in ("working", "review"):
            active_count += 1

        print(f"  {agent_name:<12} {color}{s:<12}{RESET} {task:<35}")

    print(f"\n  Active: {active_count}/{len(AGENTS)} agents")

    # Blockers
    blockers = master.get("blockers", [])
    if blockers:
        print(f"\n  {BOLD}Blockers:{RESET}")
        for b in blockers:
            print(f"  \033[31m!\033[0m {b}")

    print(f"\n{BOLD}{'='*60}{RESET}")
    print(f"  Press Ctrl+C to exit")


def main():
    interval = 30
    if "--interval" in sys.argv:
        idx = sys.argv.index("--interval")
        if idx + 1 < len(sys.argv):
            interval = int(sys.argv[idx + 1])

    # Create state dirs
    for agent in AGENTS:
        (STATE_DIR / "agents" / agent).mkdir(parents=True, exist_ok=True)

    try:
        while True:
            display()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
