#!/usr/bin/env bash
# Open a Claude Code agent "employee" in a new terminal
# Usage: ./open-employee.sh <agent-name> [working-directory]
#
# Examples:
#   ./open-employee.sh builder ./my-project
#   ./open-employee.sh sales ./my-business
#   ./open-employee.sh social ./content

set -euo pipefail

AGENT_NAME="${1:-}"
WORK_DIR="${2:-.}"

if [ -z "$AGENT_NAME" ]; then
    echo "Usage: ./open-employee.sh <agent-name> [working-directory]"
    echo ""
    echo "Available agents:"
    echo "  manager    - Coordinates all agents, assigns tasks"
    echo "  builder    - Writes code, builds features, deploys"
    echo "  sales      - Outreach, leads, customer communication"
    echo "  social     - Content creation, social media"
    echo "  ops        - Monitoring, metrics, maintenance"
    exit 1
fi

# Resolve paths
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
KIT_DIR="$(dirname "$SCRIPT_DIR")"
TEMPLATE_DIR="$KIT_DIR/templates"
STATE_DIR="$KIT_DIR/state"

# Map short names to template files
declare -A TEMPLATES=(
    [manager]="Manager.md"
    [builder]="Builder.md"
    [sales]="Sales.md"
    [social]="Social.md"
    [ops]="Operations.md"
)

TEMPLATE_FILE="${TEMPLATES[$AGENT_NAME]:-}"
if [ -z "$TEMPLATE_FILE" ]; then
    echo "Error: Unknown agent '$AGENT_NAME'"
    echo "Available: manager, builder, sales, social, ops"
    exit 1
fi

# Ensure state directory exists
mkdir -p "$STATE_DIR/agents/$AGENT_NAME"

# Create status file if it doesn't exist
STATUS_FILE="$STATE_DIR/agents/$AGENT_NAME/status.json"
if [ ! -f "$STATUS_FILE" ]; then
    cat > "$STATUS_FILE" << JSONEOF
{
  "agent": "$AGENT_NAME",
  "status": "idle",
  "current_task": null,
  "last_updated": null
}
JSONEOF
fi

# Copy template to working directory if not already there
CLAUDE_MD="$WORK_DIR/CLAUDE.md"
if [ ! -f "$CLAUDE_MD" ]; then
    cp "$TEMPLATE_DIR/$TEMPLATE_FILE" "$CLAUDE_MD"
    echo "Created CLAUDE.md from $TEMPLATE_FILE template"
fi

echo "Starting $AGENT_NAME agent in $WORK_DIR..."
echo "Template: $TEMPLATE_FILE"
echo "State: $STATUS_FILE"
echo ""

# Open Claude Code in the working directory
cd "$WORK_DIR"
claude --resume
