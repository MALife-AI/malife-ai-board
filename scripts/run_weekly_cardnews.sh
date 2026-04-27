#!/bin/zsh
# ────────────────────────────────────────────────────────────────────
# malife-weekly-cardnews 자동 실행 wrapper
#
# 트리거 (체이닝):
#   일요일 18:50 KST → com.lifesailor.market-summary
#   → auto_market.py main() 마지막 단계에서 이 wrapper 호출
#
# 인자:
#   $1 = "chained"  — auto_market.py 에서 직접 호출 (정상 경로)
#   $1 = "manual"   — 수동 실행 (테스트)
#   인자 없음        — 동일하게 동작
#
# 가드:
#   - 양쪽 입력 HTML 존재 확인
#   - 주차별 done 마커 → 한 주 한 번만 발행
#   - mkdir 기반 락 → 동시 실행 방지
# ────────────────────────────────────────────────────────────────────
set -euo pipefail

export PATH="/Users/lifesailor/.nvm/versions/node/v24.14.0/bin:/usr/local/bin:/usr/bin:/bin:/opt/homebrew/bin:/usr/sbin:/sbin"
export HOME="/Users/lifesailor"
export LANG="ko_KR.UTF-8"

# ── 주차 계산: 어제 기준 ISO 주차 ─────────────────────────────────
# 일요일 밤 트리거 → 어제(토) = 그 주
# 월요일 새벽 트리거 → 어제(일) = 직전 주
WEEK=$(date -v-1d +%V)
YEAR=$(date -v-1d +%G)
WTAG="${YEAR}-W${WEEK}"

REPO="/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board"
SUMMARY_DIR="/Users/lifesailor/Desktop/kosmos/ai/investment/market_summary/output/summary/weekly"
PM_HTML="${SUMMARY_DIR}/${WTAG}_pm.html"
STORY_HTML="${SUMMARY_DIR}/${WTAG}_story.html"

LOG_DIR="${REPO}/scripts/logs"
STATE_DIR="${REPO}/scripts/state"
mkdir -p "$LOG_DIR" "$STATE_DIR"
LOG="${LOG_DIR}/cardnews-$(date +%Y%m%d).log"

LOCK_DIR="${STATE_DIR}/.lock_${WTAG}"
DONE_FILE="${STATE_DIR}/.done_${WTAG}"

log() { echo "[$(date '+%F %T %Z')] $*" >> "$LOG"; }

# ── 가드 1: 이미 발행 완료 ────────────────────────────────────────
if [[ -f "$DONE_FILE" ]]; then
  log "[skip] ${WTAG} already published — done marker present"
  exit 0
fi

# ── 가드 2: 입력 HTML 양쪽 모두 존재 ──────────────────────────────
if [[ ! -f "$PM_HTML" || ! -f "$STORY_HTML" ]]; then
  log "[skip] ${WTAG} HTML not ready (pm=$([[ -f "$PM_HTML" ]] && echo OK || echo missing), story=$([[ -f "$STORY_HTML" ]] && echo OK || echo missing))"
  exit 0
fi

TRIGGER_KIND="${1:-manual}"

# ── 가드 3: mkdir 락 (동시 실행 방지) ─────────────────────────────
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  log "[skip] ${WTAG} another run in progress (lock=${LOCK_DIR})"
  exit 0
fi
trap "rmdir '$LOCK_DIR' 2>/dev/null || true" EXIT

# ── 본 작업 ───────────────────────────────────────────────────────
log "=========================================="
log "${WTAG} 카드뉴스 자동 생성 시작 (trigger=${TRIGGER_KIND})"
log "=========================================="

cd "$REPO"
git pull --ff-only origin main >> "$LOG" 2>&1 || log "[warn] git pull 실패 — 계속 진행"

PROMPT="이번 주차(${WTAG})의 미래에셋생명 AI Board 주간 시장 카드뉴스를 자동 생성해줘.

[자동 실행 모드 — 사용자 확인 없이 진행]

워크플로우 (.claude/skills/malife-weekly-cardnews/SKILL.md 참고):

1. 입력 HTML:
   ${PM_HTML}
   ${STORY_HTML}
   존재 확인 완료 (wrapper에서 검증). Read로 콘텐츠 추출.

2. SKILL.md 워크플로우대로 카드뉴스 PNG 20장 + AI Board 게시글 markdown 생성.
   - writings/${WTAG}-card-news/{weekly_story,pm_story}/*.png (각 10장)
   - writings/${WTAG}_AI_Board_*.md
   기준 레퍼런스는 writings/2026-W17-card-news/ 와 writings/2026-W17_AI_Board_첫게시글.md.

3. 카드 검수: 01_cover, 10_closing, 06_bonds(PM), 08_watch(PM)을 Read 도구로 시각 확인.
   텍스트 짤림/오버플로우 있으면 _base.css/template 수정 후 재렌더.

4. git add → commit ('feat: ${WTAG} AI Board 주간 카드뉴스 자동 생성') → push origin main.

5. 마지막 줄에 한 줄 결과 요약: '✓ ${WTAG} 발행 완료: 카드뉴스 20장 + 게시글'."

set +e
claude \
  --print \
  --permission-mode bypassPermissions \
  --model claude-sonnet-4-6 \
  "$PROMPT" >> "$LOG" 2>&1
EXIT=$?
set -e

log "claude CLI 종료 코드: $EXIT"

if [[ $EXIT -eq 0 ]]; then
  touch "$DONE_FILE"
  log "✓ ${WTAG} 발행 완료 — done 마커 생성"
else
  log "✗ ${WTAG} 발행 실패 (exit=$EXIT) — 다음 트리거에서 재시도"
fi

exit $EXIT
