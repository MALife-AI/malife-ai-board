"""
W22 Card News Generator  (2026-05-26 ~ 05-29 · 4거래일 · 5월 마감주)
- Generates 1080x1350 HTML cards for Weekly Story (10) + PM Story (10)
- Renders to PNG via Chrome headless
"""
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_DIR = ROOT / "_html"
WEEKLY_PNG = ROOT / "weekly_story"
PM_PNG = ROOT / "pm_story"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS_PATH = (HTML_DIR / "_base.css").as_uri()


def page(body_html: str, footer_left: str, page_label: str) -> str:
    return f"""<!doctype html>
<html lang="ko"><head>
<meta charset="utf-8">
<link rel="stylesheet" href="{CSS_PATH}">
</head>
<body>
{body_html}
<div class="footer-tag">
  <span class="brand">{footer_left}</span>
  <span class="page">{page_label}</span>
</div>
</body></html>
"""


# ───────────────────────────────────────────────────────
# WEEKLY STORY — 10 CARDS
# ───────────────────────────────────────────────────────

WEEKLY = []

# 01 COVER
WEEKLY.append(("01_cover", page(f"""
<div class="card cover">
  <div class="brand-bar"></div>
  <div class="badge-week">W22 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">AI 어닝 체인이<br><span class="accent">공급망</span>을 따라<br>세계를 관통하다</div>
  <div class="lead">
    Micron(+19%) → SNOW(+37%) → DELL(+33%) 3연타 어닝 폭발.<br>
    코스피 역대 신고점 <strong>8,476(+8.01%)</strong>·미국 3대 지수 동시 신고점.
  </div>
  <div class="meta">2026-05-26 · 05-27 · 05-28 · 05-29 (4거래일 · 5월 마감)</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">AI 수요가 실적으로 확인<br>글로벌 동시 신고점</h1>
  <p class="lede">AI 어닝 체인 × 삼성 파업 회피 × 이란 60일 휴전 MOU.<br>한국·미국·일본·대만이 같은 주에 모두 역대 최고가 갱신.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷</div>
      <div class="rname">한국</div>
      <div class="verdict up">코스피 역대 신고점 8,476</div>
      <div class="num-row"><span class="nm">KOSPI WTD</span><span class="vl up">+8.01%</span></div>
      <div class="num-row"><span class="nm">KOSDAQ WTD</span><span class="vl down">−7.43%</span></div>
      <div class="num-row"><span class="nm">KOSPI YTD</span><span class="vl up">+96.68%</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict up">3대 지수 동시 신고점</div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl up">+1.43% (9주연속)</span></div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl up">+2.39%</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl down">15.32</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--up)">
      <div class="flag">🌏</div>
      <div class="rname">아시아</div>
      <div class="verdict up">JP·TW 동반 신고점</div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl up">+4.72%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl up">+5.83%</span></div>
      <div class="num-row"><span class="nm">상하이</span><span class="vl down">혼조</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--down)">
      <div class="flag">🛢️</div>
      <div class="rname">원자재 · FX</div>
      <div class="verdict down">유가 급락·달러 약세</div>
      <div class="num-row"><span class="nm">WTI WTD</span><span class="vl down">−9.57%</span></div>
      <div class="num-row"><span class="nm">WTI 5월</span><span class="vl down">−16.46%</span></div>
      <div class="num-row"><span class="nm">DXY WTD</span><span class="vl down">−0.41%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W22", "02 / 10"))
)

# 03 TUESDAY (W22 첫 거래일 — 월요일 5/25 휴장)
WEEKLY.append(("03_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 5/26 — 휴장 후 첫날</div>
  <h1 class="day-headline">Micron <span style="color:var(--up)">+19.29%</span><br>코스피 신고가 8,047</h1>
  <p class="day-summary">
    부처님오신날·메모리얼데이 동시 휴장 후 첫 거래일,<br>
    <strong>Micron이 AI 메모리 Q3 가이던스 기대로 +19.29%</strong> 급등하며<br>
    글로벌 반도체 섹터에 불을 지폈습니다.<br><br>
    OPEC+ 증산·이란 휴전 지속에 Brent <strong>−6.71%</strong>,<br>
    코스피는 외국인이 12거래일 만에 순매수 전환하며<br>
    <strong>8,047.51 (+2.55%)</strong> 연내 신고가.<br>
    삼성전기 <strong>+17.31%</strong> 폭등.
  </p>
  <ul class="detail-list">
    <li>Micron +19.29% — AI HBM·D램 가이던스 기대</li>
    <li>외국인 12거래일 만에 순매수 전환 → 코스피 8,047 신고가</li>
    <li>Brent −6.71% — OPEC+ 증산 + 이란 휴전 지속</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Micron</div><div class="val up">+19.29%</div><div class="chg up">AI 가이던스</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+2.55%</div><div class="chg up">8,047 신고가</div></div>
    <div class="kpi"><div class="lbl">삼성전기</div><div class="val up">+17.31%</div><div class="chg up">실리콘 MLCC</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "03 / 10"))
)

# 04 WEDNESDAY — 삼성 협약 가결 + SK하이닉스 시총 $1.12조
WEEKLY.append(("04_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 5/27</div>
  <h1 class="day-headline">삼성 협약 가결 + SK하이닉스<br><span style="color:var(--up)">$1.12조 클럽</span></h1>
  <p class="day-summary">
    삼성전자 노조 전국노조가 임금 <strong>+6.2%</strong>·<br>
    반도체 DS 부문 <strong>10.5% 성과급</strong>으로<br>
    단체협약을 <strong>74%</strong> 찬성 가결.<br><br>
    SK하이닉스 장중 <strong>+14.9%</strong>까지 치솟아<br>
    시총 <strong>$1.12조</strong>로 메모리 빅3 모두 1조달러 클럽 진입.<br>
    코스피는 <strong>+5%</strong> 사이드카 후 <strong>8,228 (+2.25%)</strong> 신고가 재경신.
  </p>
  <ul class="detail-list">
    <li>삼성 노조 74% 찬성 — 파업 리스크 완전 해소</li>
    <li>SK하이닉스 시총 1,680조원($1.12조) — 메모리 빅3 1조달러 클럽 동시 진입</li>
    <li>이란 호르무즈 전면 재개 성명 → US 다우·S&P 신고점</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">삼성 협약</div><div class="val up">74%</div><div class="chg up">파업 회피</div></div>
    <div class="kpi"><div class="lbl">SK하이닉스 시총</div><div class="val up">$1.12조</div><div class="chg up">메모리 빅3</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+2.25%</div><div class="chg up">사이드카</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "04 / 10"))
)

# 05 THURSDAY — SNOW + 60일 MOU + PCE
WEEKLY.append(("05_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 5/28</div>
  <h1 class="day-headline">SNOW <span style="color:var(--up)">+37%</span> + 이란 60일 MOU<br>나스닥 신고점</h1>
  <p class="day-summary">
    직전일 급등 차익실현에 코스피 <strong>−0.53%</strong> 조정.<br>
    중국 AMEC <strong>−33.25%</strong> 폭락이 중화권에 충격파.<br><br>
    미-이란 <strong>60일 휴전 연장 MOU</strong> 서명.<br>
    장 후 스노우플레이크 제품 매출 <strong>+34% YoY</strong>·<br>
    AWS $6B AI 파트너십에 <strong>+37%</strong> 폭등.<br>
    4월 PCE <strong>+3.8%</strong> 경고에도 AI 매수세가 이를 압도.
  </p>
  <ul class="detail-list">
    <li>SNOW +37% — 제품 매출 +34% YoY · EPS 서프라이즈 +$0.07</li>
    <li>미-이란 60일 휴전 MOU 서명 → 에너지 안정 기대 심화</li>
    <li>4월 핵심 PCE 3.3% / 헤드라인 3.8% — AI 장세가 압도</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">SNOW</div><div class="val up">+37%</div><div class="chg up">AWS $6B</div></div>
    <div class="kpi"><div class="lbl">이란 MOU</div><div class="val">60일</div><div class="chg up">휴전 연장</div></div>
    <div class="kpi"><div class="lbl">AMEC</div><div class="val down">−33.25%</div><div class="chg down">중국 충격</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "05 / 10"))
)

# 06 FRIDAY — DELL + HBM4E + 코스피 8,476
WEEKLY.append(("06_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 5/29 — 5월 마지막 거래일</div>
  <h1 class="day-headline">DELL AI 서버 <span style="color:var(--up)">+757% YoY</span><br>코스피 신고점 8,476</h1>
  <p class="day-summary">
    DELL Q1 FY27 AI 서버 매출 <strong>+757% YoY · $16.1B</strong>가<br>
    아시아 개장과 함께 글로벌 AI 공급망을 폭발시켰습니다.<br><br>
    삼성전자 <strong>12단 HBM4E 첫 상업 납품</strong> 소식 동시 전해지자<br>
    기관이 <strong>1조 8,672억원</strong> 순매수,<br>
    코스피 <strong>8,476.15 (+3.55%)</strong> 역대 신고점.<br>
    TWSE +2.51%·닛케이 +2.53%·미국 3대 지수 동시 신고점.
  </p>
  <ul class="detail-list">
    <li>DELL +33% · AI 서버 +757% YoY → 연간 매출 $60B 전망</li>
    <li>삼성 HBM4E 첫 상업 납품 · 기관 1.87조 순매수</li>
    <li>S&P500 9주 연속 상승 — 글로벌 동시 신고점</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">DELL AI 서버</div><div class="val up">+757%</div><div class="chg up">YoY · $16.1B</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+3.55%</div><div class="chg up">8,476 신고점</div></div>
    <div class="kpi"><div class="lbl">기관 순매수</div><div class="val up">1.87조</div><div class="chg up">단일일</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "06 / 10"))
)

# 07 MAY CLOSING — 5월 결산
WEEKLY.append(("07_may_close", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">5월 결산 · 20영업일</div>
  <h1 class="day-headline">코스피 <span style="color:var(--up)">+28.45%</span><br>WTI <span style="color:var(--down)">−16.46%</span></h1>
  <p class="day-summary">
    이란 전후 에너지 정상화 + AI 반도체 슈퍼사이클이 결합한 한 달.<br>
    KOSPI는 <strong>5월 +28.45%</strong>로 역대 최강 월간 상승,<br>
    NASDAQ도 <strong>+8.36%</strong>로 최근 5년 최강 5월을 기록.<br><br>
    WTI는 <strong>5월 −16.46%</strong>로 코로나 이후 최대 월간 낙폭.<br>
    반면 KOSDAQ은 <strong>−9.86%</strong>로 대형주에 자금이 쏠리는<br>
    구조적 양극화가 한 달 내내 이어졌습니다.
  </p>
  <ul class="detail-list">
    <li>KOSPI MTD +28.45% / KOSDAQ MTD −9.86% — 양극화 고착</li>
    <li>NASDAQ MTD +8.36% · S&P500 +5.15% — AI 슈퍼사이클</li>
    <li>WTI MTD −16.46% (코로나 이후 최대) · 구리 +6.39%</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI 5월</div><div class="val up">+28.45%</div><div class="chg up">역대급</div></div>
    <div class="kpi"><div class="lbl">NASDAQ 5월</div><div class="val up">+8.36%</div><div class="chg up">5년 최강</div></div>
    <div class="kpi"><div class="lbl">WTI 5월</div><div class="val down">−16.46%</div><div class="chg down">코로나 이후 최대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "07 / 10"))
)

# 08 INSIGHT 1 — AI 어닝 체인
WEEKLY.append(("08_insight_chain", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · AI 어닝 체인</div>
  <h1 class="head">Micron → SNOW → DELL<br>3연타가 증명한 것</h1>
  <p class="lede">"AI 투자는 거품" 회의론을 데이터로 정면 반박한 한 주</p>

  <div class="insight-box" style="border-left-color:var(--up)">
    <div class="qa" style="color:var(--up)">한 주 안에 공급망 3개 층이 동시에 실적으로 확인됐다</div>
    <p>
      <strong>화 Micron +19%</strong> — 메모리(HBM/D램) 수요 가이던스<br>
      <strong>목 SNOW +37%</strong> — 클라우드 소프트웨어 가속<br>
      <strong>금 DELL +33%</strong> — 엔터프라이즈 AI 서버 +757% YoY ($16.1B)<br><br>
      공급망 <strong>최하단(HBM·MLCC)부터 최상단(AI 서버 ODM)</strong>까지<br>
      수혜가 같은 주에 동시 실적으로 확인된 사례는 이례적입니다.<br>
      DELL의 연간 매출 전망 <span class="hl">$60B 상향</span>은 단순 어닝 모멘텀을 넘어<br>
      <strong>AI 인프라 투자 사이클이 구조적 성장 단계에 진입</strong>했음을 시사합니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">DELL AI 서버</div><div class="val up">+757%</div><div class="chg up">YoY</div></div>
    <div class="kpi"><div class="lbl">SNOW EPS 서프</div><div class="val up">+21.9%</div><div class="chg up">컨센 대비</div></div>
    <div class="kpi"><div class="lbl">Micron(화)</div><div class="val up">+19.29%</div><div class="chg up">HBM 기대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "08 / 10"))
)

# 09 INSIGHT 2 — 코스피·코스닥 극단 디커플링
WEEKLY.append(("09_insight_decoupling", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 양극화</div>
  <h1 class="head">코스피 +8.01%<br>코스닥 <span style="color:var(--down)">−7.43%</span></h1>
  <p class="lede">한 주 15.4%p 격차 — AI 반도체 수급 독점의 결과</p>

  <div class="insight-box">
    <div class="qa">왜 같은 시장 안에서 정반대 방향이 나오는가</div>
    <p>
      삼성전자·SK하이닉스 두 종목이<br>
      코스피 시가총액의 <strong>50%+</strong>를 차지하는 구조에서,<br>
      AI HBM 수급이 대형 반도체주에 집중 유입되며<br>
      <strong>코스닥 중소형주 자금이 대거 이탈</strong>했습니다.<br><br>
      5월 누적으로도 <strong>코스피 +28.45% vs 코스닥 −9.86%</strong>로<br>
      전례 없는 양 지수 방향성 분기가 지속되고 있습니다.<br>
      코스닥 바이오·중소형 성장주 투자자는<br>
      <span class="hl">수급 구조가 근본적으로 변화</span>했음을 인지할 필요가 있습니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">코스피 WTD</div><div class="val up">+8.01%</div><div class="chg up">신고점</div></div>
    <div class="kpi"><div class="lbl">코스닥 WTD</div><div class="val down">−7.43%</div><div class="chg down">자금 이탈</div></div>
    <div class="kpi"><div class="lbl">격차</div><div class="val down">15.4%p</div><div class="chg down">단주간</div></div>
  </div>
</div>
""", "WEEKLY STORY · W22", "09 / 10"))
)

# 10 CLOSING — W23 변수
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W23</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>이란 MOU 서명·미국 NFP/ISM 고용 지표·ECB 회의(6/5).<br>코스피 +96% YTD 후 기술적 소화 구간 진입 가능성.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">코스피 밸류에이션 과열·외국인 수급 반전</h4>
      <p style="color:#cfe0f3">YTD +96.68%·5월 MTD +28.45% 급등 후 차익실현 압력. 외국인 재순매도 전환 시 코스피 7,800 단기 조정 위험.</p>
    </div>
    <div class="risk-item med" style="background:rgba(203,96,21,.12);border-left-color:var(--warn)">
      <span class="tag" style="background:var(--warn)">MED</span>
      <h4 style="color:#fff">이란 MOU 트럼프 서명 불확실성</h4>
      <p style="color:#cfe0f3">60일 MOU는 '대략 합의' 단계. 서명 지연·결렬 시 WTI $95+ 급반등, 5월 −16% 낙폭 되돌림 위험.</p>
    </div>
    <div class="risk-item med" style="background:rgba(203,96,21,.12);border-left-color:var(--warn)">
      <span class="tag" style="background:var(--warn)">MED</span>
      <h4 style="color:#fff">PCE 3.3% 추세 → Fed 동결 연장</h4>
      <p style="color:#cfe0f3">4월 핵심 PCE 3.3%(전월 3.2%) 상승 반전. NFP·ISM 과열 시 US 30Y 5%+ 재진입 → 성장주 압박 가능.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-06-01 발행</span>
  </div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "10 / 10"))
)


# ───────────────────────────────────────────────────────
# PM STORY — 10 CARDS
# ───────────────────────────────────────────────────────

PM = []

# 01 COVER
PM.append(("01_cover", page(f"""
<div class="card cover">
  <div class="brand-bar"></div>
  <div class="badge-week" style="background:var(--orange)">PM · W22</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W23 시나리오·포지셔닝 가이드<br>
    (5월 마감주, 4거래일)
  </div>
  <div class="meta">2026-05-26 ~ 2026-05-29 · 4/4 영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">코스피 역대 신고점<br>WTD +8.01% · YTD +96.68%</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">8,476.15</span>
    <span class="ch up">+3.55% (금)</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD +8.01%</strong> · MTD <span class="up">+28.45%</span> · YTD <span class="up">+96.68%</span> — 5/26 8,047 → 5/27 8,228 → 5/29 8,476 단계적 신고점</li>
    <li>주도주: 삼성전자 317,000 <span class="up">+5.84%</span>(금, HBM4E 첫 출하), SK하이닉스 2,333,000 <span class="up">+1.92%</span>(금, 시총 $1.12조)</li>
    <li>대형주 견인: LG전자 293,000 <span class="up">+29.93%</span>, 삼성전기 2,127,000 <span class="up">+15.04%</span> WTD</li>
    <li>KOSDAQ 1,074.80 · WTD <span class="down">−7.43%</span> · MTD <span class="down">−9.86%</span> — 대형주 쏠림으로 중소형·바이오 이탈 디커플링</li>
    <li>기관 +1조 8,672억원 순매수(금) · 외국인 12거래일 만에 순매수 전환(5/26) · USD/KRW 1,507.13</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI WTD</div><div class="val up">+8.01%</div><div class="chg up">신고점</div></div>
    <div class="kpi"><div class="lbl">KOSPI YTD</div><div class="val up">+96.68%</div><div class="chg up">5월 +28.45%</div></div>
    <div class="kpi"><div class="lbl">KOSDAQ WTD</div><div class="val down">−7.43%</div><div class="chg down">디커플링</div></div>
  </div>
</div>
""", "PM STORY · W22", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">3대 지수 동시 신고점<br>S&P 9주 연속 상승</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">MTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,580.06</td><td class="vl up">+1.43%</td><td class="vl up">+5.15%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">26,972.62</td><td class="vl up">+2.39%</td><td class="vl up">+8.36%</td></tr>
    <tr><td class="nm">Dow</td><td class="vl">51,032.46</td><td class="vl up">신고점</td><td class="vl">—</td></tr>
    <tr><td class="nm">VIX</td><td class="vl">15.32</td><td class="vl down">−5.10%</td><td class="vl">저변동</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>AI 어닝 3연타: DELL <span class="up">+33%</span>(금, 서버 +757% YoY · $16.1B) · SNOW <span class="up">+37%</span>(목) · Micron <span class="up">+19.29%</span>(화)</li>
    <li>엔터프라이즈 AI: IBM <span class="up">+12.71%</span> · Oracle <span class="up">+10.84%</span> · MSFT <span class="up">+5.45%</span> · Meta <span class="up">+1.82%</span></li>
    <li>NVIDIA <span class="down">−1.45%</span>(금) — 차익실현 · Russell2K <span class="down">−0.59%</span>(금) 소형주 상대 약세</li>
    <li>4월 핵심 PCE <span class="down">3.3% YoY</span>(전월 3.2%) · 헤드라인 3.8% — AI 장세가 지표를 압도</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    DELL +757% AI 서버 매출이 "AI = 거품" 회의론을 데이터로 종결
  </div>
</div>
""", "PM STORY · W22", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 및 중국</div>
  <h1 class="head">JP·TW 동반 신고점<br>중국은 자립주 충격</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">MTD</th></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">66,329.50</td><td class="vl up">+4.72%</td><td class="vl up">+11.88%</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">44,732.94</td><td class="vl up">+5.83%</td><td class="vl up">+14.92%</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">25,182.39</td><td class="vl">반등</td><td class="vl">—</td></tr>
    <tr><td class="nm">Shanghai</td><td class="vl">4,068.57</td><td class="vl">혼조</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일본 AI 부품: SUMCO <span class="up">+19.30%</span>, Murata <span class="up">+12.73%</span>, TDK <span class="up">+8%</span>대, Keyence <span class="up">+6.56%</span></li>
    <li>대만 TSMC·ASEH 동반 강세 — AI 반도체 공급망 전체 신고점</li>
    <li>중국 충격: AMEC <span class="down">−33.25%</span>(목), SMIC <span class="down">−7.54%</span>, Hygon <span class="down">−6.51%</span> — 반도체 자립주 차익실현</li>
    <li>NIFTY 23,547.75 <span class="down">−1.50%</span>(금) — 인도, 아시아 AI 3각(KR·JP·TW) 대비 소외</li>
  </ul>
</div>
""", "PM STORY · W22", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">유가 5월 −16.46%<br>이란 60일 MOU 서명</h1>

  <div class="region-grid">
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">WTI</span><span class="vl down">$87.36 (−9.57% WTD)</span></div>
      <div class="num-row"><span class="nm">Brent</span><span class="vl down">$92.05</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl up">$4,560 (+0.87%)</span></div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl down">98.91 (−0.41%)</span></div>
    </div>
    <div class="region-card europe">
      <div class="rname">유럽 (관망)</div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl up">25,104.70 (+0.87%)</span></div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl">6,050.54</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl">8,183.34</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl">10,409.30</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:22px">
    <li>이란 5/27 호르무즈 재개 성명 → 5/28 60일 휴전 MOU 서명 — 트럼프 최종 서명 잔존</li>
    <li>WTI MTD <span class="down">−16.46%</span> 코로나 이후 최대 월간 낙폭 + OPEC+ 증산</li>
    <li>EUR/USD 1.166(+0.09% 금) · GBP/USD 1.344 — 유럽 통화 소폭 강세</li>
    <li>유럽은 AI 어닝 직접 수혜 없이 관망 — MTD DAX +3.87% 선방</li>
  </ul>
</div>
""", "PM STORY · W22", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">US 10Y −10.5bp<br>에너지 디스인플레 효과</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">3.588%</div><div class="chg">단기 안정</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val up">4.453%</div><div class="chg up">−10.5bp WTD</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val">4.993%</div><div class="chg">5% 하향</div></div>
  </div>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">10Y-2Y</div><div class="val">86.5bp</div><div class="chg">플래트닝</div></div>
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val up">3.924%</div><div class="chg up">−6.8bp</div></div>
    <div class="kpi"><div class="lbl">KR 3Y</div><div class="val up">3.731%</div><div class="chg up">−3.5bp</div></div>
  </div>

  <ul class="detail-list">
    <li>주간 흐름: 화·수 유가 급락 → 10Y 하락 → 목 PCE 3.3% 반전 → 금 DELL 어닝 → 리스크온 재강화</li>
    <li>크레딧 ETF 동반 강세: TLT 85.76 · HYG 80.31 · LQD 109.36 · EMB 96.43</li>
    <li>한국 장기물 강세 — 리스크온 환경에서도 KR 10Y −6.8bp 수요 견조</li>
  </ul>

  <div class="big-quote" style="margin-top:12px">
    PCE 3.3% 반등 vs 에너지 디스인플레 — Fed 경로 W23 NFP·ISM가 결정
  </div>
</div>
""", "PM STORY · W22", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W23 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>6/1 ~ 6/5</h1>
  <p class="lede">이란 서명·NFP·ISM·ECB(6/5)가 핵심 변수</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL (낮음)</div>
      <h4>이란 서명 + Fed 인하 기대</h4>
      <div class="pp">W22 모멘텀 연장</div>
      <p>트럼프 이란 MOU 서명 → WTI $80 하회. NFP 강세 + PCE 안정 → Fed 조기 인하 기대. KOSPI 8,600+, S&P 7,700 재도전, USD/KRW 1,480 하향.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE (유력)</div>
      <h4>기술적 소화 + 박스 횡보</h4>
      <div class="pp">가장 유력</div>
      <p>W22 +8.01% 급등 후 코스피 8,100~8,400 소화. 이란 MOU 서명 지연 · 유가 $87~93 박스. NFP/ISM 혼조 → Fed 경로 불변. S&P 7,450~7,600, VIX 14~17.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR (낮음)</div>
      <h4>이란 거부 + NFP 과열</h4>
      <div class="pp">복합 충격</div>
      <p>이란 MOU 거부 → WTI $95+ 재급등. NFP 과열·ISM 급락 → 스태그플레이션 우려. US 30Y 5.2%+, 코스피 7,800 이하 단기 조정, VIX 20 돌파.</p>
    </div>
  </div>
</div>
""", "PM STORY · W22", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W23 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li><strong>코스피 8,000 지지</strong> 여부 — 급등 후 저항</li>
        <li>삼성 HBM4E 납품 규모 공시</li>
        <li>외국인 순매수 지속 vs 3조+ 재순매도 반전</li>
        <li>KOSDAQ 바이오·중소형 자금 이동 신호</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li><strong>트럼프 이란 MOU 서명</strong>(수시)</li>
        <li>ISM 제조업 6/1 · ADP 6/3 · ISM 서비스 6/3</li>
        <li><strong>NFP 6/5(금)</strong> — Fed 경로 핵심</li>
        <li>WTI $93+ 복귀 → 인플레 재점화 위험</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아 및 중국</h4>
      <ul>
        <li>KR·JP·TW 3각 신고점 소화 여부</li>
        <li>일본 춘계 임금 교섭 최종치 · USD/JPY 160</li>
        <li>중국 부양책 발표 시 HSI 반등</li>
        <li>중국 반도체 자립주(AMEC·SMIC) 추가 조정</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 실적·지표</h4>
      <ul>
        <li><strong>Salesforce·CrowdStrike</strong> 6/4 실적</li>
        <li>S&P500 9주 연속 상승 모멘텀 지속</li>
        <li>VIX 14~17 저변동 유지 여부</li>
        <li>NFP 25만+ 과열 → 금리 재상승 위험</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li><strong>ECB 통화정책 6/5</strong> — 25bp 인하 컨센</li>
        <li>인하 시 유럽 채권·배당주 호재</li>
        <li>DAX 25,000 지지 · EUR/USD 1.16 유지</li>
        <li>ECB 동결 서프라이즈 → EUR 강세 단기 조정</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권</h4>
      <ul>
        <li>US 30Y 5% 재진입 여부</li>
        <li>10Y-2Y 86.5bp 추가 플래트닝</li>
        <li>US 10Y 4.60%+ → 성장주 압박 재개</li>
        <li>EU-US 금리 스프레드 확대 (ECB 인하)</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W22", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W23 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 1 / MED 2</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>코스피 밸류에이션 과열·외국인 수급 반전</h4>
      <p>W22 +8.01%·5월 MTD +28.45%로 <strong>YTD +96.68%</strong>. PER 과열권에서 차익실현 + 외국인 재순매도 전환 시 급조정 가능. KOSDAQ −7.43% 동반 약세 구도 고착화 리스크.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>이란 MOU 서명 지연/결렬</h4>
      <p>트럼프 최종 서명 미이행 시 <strong>WTI $95+ 급반등</strong>. 5월 −16.46% 낙폭을 단시간에 되돌리며 인플레 재점화·성장주 압박. 이란 내부 강경파 반발도 변수.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>미국 PCE 3.3% 상승 추세 → Fed 동결 연장</h4>
      <p>핵심 PCE 3.3%(전월 3.2%) 상승 반전이 다음 CPI·PCE에서 지속 확인되면 <strong>2026년 내 금리인하 기대 소멸</strong>. US 30Y 5%+ 재진입 시 성장주·EM 동반 조정.</p>
    </div>
  </div>
</div>
""", "PM STORY · W22", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W23 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell n"><div class="lbl">한국 대형 반도체</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">미국 AI 인프라</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">JP·TW AI 부품</div><div class="vl">OW</div></div>
    <div class="pos-cell n"><div class="lbl">유럽 (ECB 인하)</div><div class="vl">N→OW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell n"><div class="lbl">미국 대형기술</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">미국 장기채</div><div class="vl">N</div></div>
    <div class="pos-cell uw"><div class="lbl">에너지 섹터</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">한국 중소형</div><div class="vl">N→관심</div></div>
  </div>

  <div style="margin-top:30px;background:var(--bg-soft);border-radius:14px;padding:22px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:21px;color:var(--text);line-height:1.6;font-weight:500">
      AI 인프라 OW · JP·TW 부품 OW ·<br>한국 대형 반도체 N 소화 · 에너지 UW
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W22", "10 / 10"))
)


# ───────────────────────────────────────────────────────
# RENDER
# ───────────────────────────────────────────────────────

def write_html(deck, out_html_dir):
    files = []
    for slug, html in deck:
        p = out_html_dir / f"{slug}.html"
        p.write_text(html, encoding="utf-8")
        files.append(p)
    return files


def render_png(html_path: Path, out_png: Path):
    """Use Chrome headless to screenshot a 1080x1350 page."""
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--default-background-color=00000000",
        f"--window-size=1080,1350",
        f"--screenshot={out_png}",
        "--virtual-time-budget=5000",
        f"file://{html_path}",
    ]
    subprocess.run(cmd, check=True, capture_output=True)


def main():
    weekly_html_dir = HTML_DIR / "weekly"
    pm_html_dir = HTML_DIR / "pm"
    weekly_html_dir.mkdir(exist_ok=True)
    pm_html_dir.mkdir(exist_ok=True)
    WEEKLY_PNG.mkdir(exist_ok=True)
    PM_PNG.mkdir(exist_ok=True)

    print("Writing Weekly HTML...")
    weekly_files = write_html(WEEKLY, weekly_html_dir)
    print("Writing PM HTML...")
    pm_files = write_html(PM, pm_html_dir)

    print("Rendering Weekly PNGs...")
    for f in weekly_files:
        out = WEEKLY_PNG / f"{f.stem}.png"
        render_png(f, out)
        print(f"  ✓ {out.name}")

    print("Rendering PM PNGs...")
    for f in pm_files:
        out = PM_PNG / f"{f.stem}.png"
        render_png(f, out)
        print(f"  ✓ {out.name}")

    print("Done.")


if __name__ == "__main__":
    main()
