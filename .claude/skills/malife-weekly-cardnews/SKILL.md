---
name: malife-weekly-cardnews
description: "미래에셋생명 AI Board 전사 게시판용 주간 시장 카드뉴스 자동 생성 스킬. Weekly Market Summary HTML 리포트(`PM Story` + `Weekly Story` 탭)를 입력받아 1080×1350 카드뉴스 이미지 20장 + AI Board 게시글 markdown을 생성한다. 미래에셋 브랜드 컬러(#F58220 / #043B72), Spoqa Han Sans 적용. Use when: 사용자가 'AI Board 게시글 만들어줘', 'W## 카드뉴스 생성', '주간 시장 카드뉴스', 'malife weekly cardnews', '/malife-weekly-cardnews'를 요청할 때."
argument-hint: "주차 번호 (예: W18, 2026-W18) 또는 입력 HTML 경로"
license: MIT
metadata:
  author: lifesailor
  version: "1.0.0"
---

# 미래에셋생명 주간 시장 카드뉴스 생성 스킬

매주 발행되는 글로벌 시장 주간 리포트(`Weekly Market Summary`)를 사내 AI Board 게시판용 카드뉴스로 변환한다.
같은 데이터를 **두 시선** — 일반 임직원용 `Weekly Story`, 운용·기획용 `PM Story` — 으로 정리해 게시한다.

## When to Use

- "W## 카드뉴스 만들어줘", "이번 주 AI Board 게시글 만들어줘"
- 사용자가 `2026-W##.html` 또는 `_pm.html` / `_story.html` 경로를 제시하며 변환을 요청할 때
- 첫 게시글 레퍼런스 확인 요청 ("저번 W17처럼 이번 주도 만들어줘")

---

## 입력 / 출력 경로

### 입력 (Source Data)

```
/Users/lifesailor/Desktop/kosmos/ai/investment/market_summary/output/summary/weekly/
├── 2026-W##.html         ← 메인 (CSS 스타일 참조용)
├── 2026-W##_pm.html      ← PM Story 탭 본체 (필수)
└── 2026-W##_story.html   ← Weekly Story 탭 본체 (필수)
```

`_pm.html`이 회고 7섹션 + W##+1 Outlook(시나리오 / Watch / 리스크 / 포지셔닝) 구조를 갖고,
`_story.html`이 일자별 5일 + 인사이트 + 리스크 구조를 갖는다는 점을 가정한다.

### 출력 (AI Board)

```
/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/writings/
├── 2026-W##_AI_Board_*.md          ← 게시글 본문 (markdown)
└── 2026-W##-card-news/
    ├── weekly_story/                ← 10장 PNG (1080×1350)
    │   ├── 01_cover.png
    │   ├── 02_keyframe.png
    │   ├── 03_monday.png ~ 07_friday.png
    │   ├── 08_insight_kospi.png (또는 주차별 핵심)
    │   ├── 09_insight_oil.png (또는 주차별 핵심)
    │   └── 10_closing.png
    ├── pm_story/                    ← 10장 PNG (1080×1350)
    │   ├── 01_cover.png
    │   ├── 02_korea.png
    │   ├── 03_usa.png
    │   ├── 04_asia.png
    │   ├── 05_macro.png
    │   ├── 06_bonds.png
    │   ├── 07_scenarios.png
    │   ├── 08_watch.png
    │   ├── 09_risks.png
    │   └── 10_positioning.png
    └── _html/                       ← 카드 HTML 원본 + 생성 스크립트
        ├── _base.css
        ├── _template.py
        ├── weekly/*.html
        └── pm/*.html
```

---

## 디자인 토큰 (필수 준수)

| 토큰 | 값 |
|------|-----|
| Brand Orange | `#F58220` |
| Brand Blue | `#043B72` |
| Up (상승) | `#0d9b6a` |
| Down (하락) | `#d9304f` |
| Warn | `#CB6015` |
| Background | `#ffffff` (cover/closing 외) |
| Soft BG | `#f7f8fc` |
| Body Font | Spoqa Han Sans Neo |
| Mono Font | JetBrains Mono (수치) |
| 카드 사이즈 | **1080 × 1350** (4:5) |
| 카드 패딩 | `80px 72px 72px 72px` |

상세 컴포넌트 스타일은 `assets/cardnews.css` 참조.

---

## 카드 구성 (정형)

### Weekly Story 10장 (일반 임직원 — 이야기 중심)

| # | 카드 | 내용 |
|---|------|------|
| 01 | Cover | "{주제 한 줄} W## · {연도}" + 리드 |
| 02 | Keyframe | 한 주 요약 + 4개 지역 KPI 그리드 |
| 03 | Monday | 첫째 영업일 헤드라인 + 본문 + 3 KPI |
| 04 | Tuesday | 둘째 영업일 |
| 05 | Wednesday | 셋째 영업일 |
| 06 | Thursday | 넷째 영업일 |
| 07 | Friday | 다섯째 영업일 |
| 08 | Insight 1 | 주차별 핵심 교훈 ① (예: KOSPI ATH 배경) |
| 09 | Insight 2 | 주차별 핵심 교훈 ② (예: 정전·유가 패러독스) |
| 10 | Closing | 다음 주 W##+1 리스크 3가지 + 발행 정보 (`.closing` 다크 그라데이션) |

### PM Story 10장 (운용·기획 — 수치 중심)

| # | 카드 | 내용 |
|---|------|------|
| 01 | Cover | PM Story + Outlook 표지 |
| 02 | 🇰🇷 한국 | KOSPI 종가 / WTD·MTD·YTD / 섹터 / 외국인 / PER·PBR |
| 03 | 🇺🇸 미국 | S&P500·NASDAQ 표 + 일별 리듬 + 빅테크 EPS |
| 04 | 🌏 아시아 | TWSE·Nikkei·HSI·NIFTY 표 + FX |
| 05 | 매크로·🇪🇺 유럽 | DXY·금리·VIX·Gold + 유럽 약세 요인 |
| 06 | 💵 채권 | US/KR 주요 만기 + 크레딧 + TIPS |
| 07 | W##+1 시나리오 | Bull / Base / Bear 3분할 + 확률 |
| 08 | W##+1 Watch Points | 6개 영역 (한국·매크로·아시아·미국실적·유럽·원자재) |
| 09 | W##+1 리스크 | HIGH×2 + MED×1 |
| 10 | 포지셔닝 | OW/N/UW 8셀 + 면책 문구 |

---

## 실행 절차

### 1단계: 입력 검증

```bash
# 주차 번호 확인 (예: W18 → 2026-W18)
SRC=/Users/lifesailor/Desktop/kosmos/ai/investment/market_summary/output/summary/weekly
ls "$SRC" | grep "2026-W18"
```

`_pm.html` + `_story.html`이 모두 있어야 한다. 없으면 사용자에게 알린다.

### 2단계: 작업 폴더 생성

```bash
TARGET=/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/writings
mkdir -p "$TARGET/2026-W##-card-news"/{weekly_story,pm_story,_html/weekly,_html/pm}
```

### 3단계: 자산 복사

`assets/cardnews.css` → `$TARGET/2026-W##-card-news/_html/_base.css`로 복사.
`assets/render_cards.py` → `$TARGET/2026-W##-card-news/_html/render_cards.py`로 복사 (선택).

### 4단계: 콘텐츠 추출 (가장 중요)

`_pm.html` + `_story.html`을 Read하여 다음 데이터를 추출:

**Weekly Story에서:**
- Hero text (한 줄 요약 + 5일 일자별 단락)
- Causal chain (5개 일자별 노드)
- Session grid (아시아·유럽·미국 5일별 리듬 + WTD KPI)
- Insight grid (4개 교훈 카드 → 카드뉴스용 2개 선별)
- Risk section (다음 주 리스크)

**PM Story에서:**
- 섹터별 7 블록 (한국/매크로/아시아/미국/유럽/채권 + Outlook 헤더)
- Scenario grid (Bull/Base/Bear, 확률 포함)
- Watch grid (6개 영역)
- Risk OL (HIGH/HIGH/MED 3개)
- Positioning grid (8 자산)

### 5단계: 카드별 HTML 생성

`references/W17_template_example.py`를 참고하여 `_template.py` 작성.
구조:

```python
WEEKLY = []
WEEKLY.append(("01_cover", page(html_body, "MIRAE ASSET LIFE · AI BOARD", "01 / 10")))
# ... 10개
PM = []
PM.append(("01_cover", page(html_body, "MIRAE ASSET LIFE · AI BOARD", "01 / 10")))
# ... 10개
```

각 카드 HTML은 `<div class="card">` 또는 `<div class="card cover">` / `<div class="card closing">` 래퍼로 시작하며 `_base.css` 클래스 사용.

### 6단계: PNG 렌더

```bash
cd $TARGET/2026-W##-card-news
python3 _html/_template.py
```

내부적으로 Chrome headless가 호출된다 (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --headless=new --window-size=1080,1350 --screenshot=...`).

### 7단계: 카드 검수 (필수)

생성된 PNG를 Read 도구로 최소 다음 카드를 시각 확인:
- `01_cover.png` (양 덱)
- `10_closing.png` (텍스트 짤림 검증)
- `08_watch.png` (PM, 정보 가장 많은 카드)

**텍스트 오버플로우가 있으면** `_base.css`의 해당 컴포넌트 패딩/폰트를 줄이거나 콘텐츠를 압축한다.

### 8단계: 게시글 markdown 생성

`writings/2026-W##_AI_Board_*.md` 작성. 표준 구조:

```markdown
# [AI 사례] {제목} (W##, YYYY-MM-DD ~ MM-DD)

**작성: AI 혁신팀 최정윤**
**발행: YYYY-MM-DD**

---

안녕하세요, AI 혁신팀 최정윤입니다.

{2~3 문장 인트로 — 이번 주 핵심을 두괄식으로}

| 카드 | 대상 | 핵심 |
| ... |

> 본 자료는 시장 데이터 기반 정보 공유용이며, 매수·매도 직접 권유가 아닙니다.

## 🗞️ Weekly Story — {부제}

{한 줄 요약 + 2 문단 본문}

![01 표지](2026-W##-card-news/weekly_story/01_cover.png)
... (10장 모두 임베드, 짧은 alt 텍스트)

## 💼 PM Story + Outlook — {부제}

{2 문단 본문}

![01 표지](2026-W##-card-news/pm_story/01_cover.png)
... (10장 모두 임베드)

## 📌 W##+1에 꼭 보셔야 할 3가지 (핵심 요약)

1. **🔴 ...**
2. **🔴 ...**
3. **🟡 ...**

## 💬 (선택) AI 혁신팀 코멘트

---

**문의 / 의견**: AI 혁신팀 최정윤 (내선 4874)
**다음 발행 예정**: YYYY-MM-DD (월) — W##+1 리뷰 + W##+2 Outlook
```

---

## 톤 & 스타일 가드

- **두괄식**: 모든 카드 헤드라인은 결론부터. 예) "KOSPI 사상 최고치 랠리" (X "한 주의 시장 흐름")
- **숫자는 항상 단위 명시**: WTD, MTD, YTD, bp, % 등
- **컬러 코드는 일관**: 상승 초록(`.up`), 하락 빨강(`.down`), 중립 회색(`.flat`)
- **이모지는 카테고리 표식만**: 🇰🇷·🇺🇸·🌏·🇪🇺·💵·🛢️·⚠·📊 등. 본문에는 사용 자제.
- **금지어**: "추천한다", "사야 한다", "팔아야 한다" — 반드시 면책 문구로 대체.
- **사내 톤**: "공유드립니다", "참고하세요" 등 격식 + 친근. AI Studio 오픈 공지 톤 유지.

---

## 흔한 실수 (W17에서 학습)

1. ❌ `closing` 카드의 `.sign`과 `.footer-tag`를 동시에 `position:absolute`로 두면 하단에서 겹쳐 텍스트가 잘려 보인다.
   ✅ `.sign`은 normal flow + `margin-top`, `.footer-tag`는 `display:none`으로 처리.
2. ❌ Spoqa 웹폰트가 Chrome headless에서 첫 로드 시 fallback 될 수 있다.
   ✅ `--virtual-time-budget=4000` 이상 두면 안정. 부족하면 5000으로 증가.
3. ❌ 일자별 카드의 `.kpi-row`에 `margin-bottom:120px`가 너무 크면 footer가 가려진다.
   ✅ `auto`로 두거나 `60px` 정도로 조정.
4. ❌ 시나리오 카드를 3분할 했을 때 한 장에 너무 많은 글자 → 가독성 저하.
   ✅ 시나리오당 최대 2~3 문장으로 압축.

---

## 자주 쓰는 명령

```bash
# 한 번에 W## 카드뉴스 + 게시글까지 (수동 워크플로우)
WEEK=W18
SRC=/Users/lifesailor/Desktop/kosmos/ai/investment/market_summary/output/summary/weekly
TARGET=/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/writings/2026-${WEEK}-card-news

# 1) 폴더 + 자산 복사
mkdir -p $TARGET/{weekly_story,pm_story,_html/weekly,_html/pm}
cp ~/.claude/skills/malife-weekly-cardnews/assets/cardnews.css $TARGET/_html/_base.css

# 2) 데이터 읽기 → _template.py 작성 (에이전트가 수행)
# 3) 렌더
cd $TARGET && python3 _html/_template.py

# 4) 검수
open $TARGET/weekly_story/01_cover.png
open $TARGET/weekly_story/10_closing.png
open $TARGET/pm_story/01_cover.png
```

---

## 참고 파일

- `assets/cardnews.css` — 1080×1350 카드뉴스 CSS 토큰·컴포넌트
- `assets/render_cards.py` — Chrome headless 렌더 헬퍼
- `references/W17_template_example.py` — W17 완성본 (구조 레퍼런스 — 수정 금지)
- 첫 게시글 예시: `/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/writings/2026-W17_AI_Board_첫게시글.md`
- 프로젝트 컨벤션: `/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/CLAUDE.md`
