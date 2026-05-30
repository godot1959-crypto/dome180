#!/bin/bash
# ============================================================
# run_newsletter.sh
# Genera e invia "Il Mio Quotidiano Personale" via Claude Code
# Uso: bash run_newsletter.sh
# Cron domenicale (es. ogni domenica alle 8:00):
#   0 8 * * 0 /percorso/run_newsletter.sh >> /percorso/newsletter.log 2>&1
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TASK_FILE="$SCRIPT_DIR/task_newsletter.md"
LOG_FILE="$SCRIPT_DIR/newsletter.log"

echo "========================================"
echo " Il Mio Quotidiano Personale"
echo " Avvio: $(date '+%A %d %B %Y — %H:%M')"
echo "========================================"

# Verifica che claude sia installato
if ! command -v claude &> /dev/null; then
  echo "ERRORE: Claude Code CLI non trovato."
  echo "Installalo con: npm install -g @anthropic-ai/claude-code"
  exit 1
fi

# Esegui il task in modalità non interattiva
claude \
  --print \
  --allowedTools "WebSearch,WebFetch,Bash,mcp__gmail" \
  "$(cat "$TASK_FILE")"

echo ""
echo "✅ Newsletter completata — $(date '+%H:%M:%S')"
