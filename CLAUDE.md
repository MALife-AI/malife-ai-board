# malife_ai_board

미래에셋생명 사내 인트라넷 **AI Board / AI Studio** 운영 프로젝트.
AI 혁신팀이 임직원 대상으로 발행하는 게시글, 카드뉴스, 공지문을 생성·관리한다.

---

## 프로젝트 컨텍스트

- **운영 주체**: AI 혁신팀 (담당: 최정윤 / 내선 4874)
- **대상 게시판**: 사내 인트라넷 Mi-SQUARE 의 **AI Studio** + **AI Board**
- **AI Studio 분류**: AI 뉴스 / AI 사례 / FAQ / AI 자유게시
- **운영 톤**: 격식보다 친근한 사내 채팅 톤. "이거 알고 계세요?" 정도의 가벼운 어투. 거창한 학습 자료가 아닌 **짧고 실용적인** 콘텐츠.

자세한 게시판 목적·정책은 [AI_Studio_오픈공지글.md](AI_Studio_오픈공지글.md) 참고.

---

## 폴더 구조

```
malife_ai_board/
├── .claude/
│   └── skills/
│       └── malife-weekly-cardnews/   ← 프로젝트 로컬 스킬 (~/.claude/와 동기화)
├── AI_Studio_오픈공지글.md      ← 게시판 오픈 공지(원본)
├── AI_Studio_보고.md            ← AX 협의체 보고용 요약
├── archive/                     ← 인터랙티브 목업 HTML, 과거 자료
└── writings/                    ← 발행 콘텐츠 (현재 작업 폴더)
    ├── 2026-W17_AI_Board_첫게시글.md
    └── 2026-W17-card-news/
        ├── weekly_story/        ← 일반 임직원용 카드 10장 (PNG)
        ├── pm_story/            ← 운용·기획용 카드 10장 (PNG)
        └── _html/               ← 카드 HTML 원본 + 생성 스크립트
```

게시글은 `writings/` 아래에 `YYYY-W##_*.md` 형식으로 저장하고, 첨부되는 카드뉴스 이미지는 같은 주차의 폴더(`YYYY-W##-card-news/`)에 둔다.

---

## 정기 콘텐츠

### Weekly Market Story (매주 월요일 발행)

**입력**: `/Users/lifesailor/Desktop/kosmos/ai/investment/market_summary/output/summary/weekly/YYYY-W##_pm.html` + `..._story.html`

**출력**:
- `writings/YYYY-W##-card-news/weekly_story/` (10장 PNG, 1080×1350)
- `writings/YYYY-W##-card-news/pm_story/` (10장 PNG, 1080×1350)
- `writings/YYYY-W##_AI_Board_*.md` (게시글 본문)

**생성 방법**: `malife-weekly-cardnews` 스킬을 호출한다.

스킬은 두 곳에 동일 사본으로 설치되어 있다:
- 사용자 레벨: `~/.claude/skills/malife-weekly-cardnews/` (모든 디렉터리에서 사용 가능)
- 프로젝트 레벨: `.claude/skills/malife-weekly-cardnews/` (이 프로젝트에서 직접 열람·수정 가능)

수정 시 두 사본이 어긋나지 않도록 한쪽을 업데이트한 뒤 `cp -R` 으로 동기화한다.

---

## 디자인 가이드

- **컬러**: Mirae Asset Orange `#F58220` / Brand Blue `#043B72`
- **서체**: Spoqa Han Sans Neo (한글) + JetBrains Mono (수치)
- **카드뉴스 규격**: 1080×1350 (4:5) — 인스타·인트라넷 게시 모두 호환
- 자세한 브랜드 가이드는 사용자 스킬 `mirae-asset-design` 참고

---

## 글쓰기 톤 (게시글)

1. 첫 줄은 **"안녕하세요, AI 혁신팀 최정윤입니다."** 인사로 시작
2. 본문은 **두괄식** — "오늘은 ~를 공유합니다" 한 문장 먼저
3. 어려운 용어는 한 줄 풀어서 설명. PM·일반 임직원 모두 읽을 수 있게.
4. "거창하게 잘 알아야만 참여할 수 있는 곳이 아닙니다" 톤 유지 — 댓글·의견 환영 문구로 마무리
5. 끝에 **문의: AI 혁신팀 최정윤 (내선 4874)** 명시

---

## 하지 말 것

- 게시글에 직접적인 매수·매도 권유 표현. 항상 **"방향성 참고용 / 매수·매도 권유 아님"** 면책 문구 포함.
- 리포트 원본 PDF/HTML을 그대로 첨부 — 카드뉴스 이미지로 가공해서 올린다.
- 외부 공개. 본 프로젝트의 자료는 **사내 한정**.

---

## 자주 쓰는 명령

```bash
# 카드뉴스 생성 (이번 주차 W## 변수 치환)
cd "/Users/lifesailor/Desktop/kosmos/미래에셋생명/project/main/malife_ai_board/writings/YYYY-W##-card-news"
python3 _html/_template.py
```

또는 스킬로:

```
/skill malife-weekly-cardnews W18
```
