"""
W20 Card News Generator  (2026-05-11 ~ 05-15)
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
  <div class="badge-week">W20 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">종가 보합<br>내부는 <span class="accent">거대한</span><br>재가격</div>
  <div class="lead">
    달러 +1.41%, 유가 +10%, 미국 단기금리 +19bp.<br>
    그리고 금요일, 코스피 8,046에서 절벽 추락.
  </div>
  <div class="meta">2026-05-11 · 05-12 · 05-13 · 05-14 · 05-15</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">지수 보합, 내부 격변<br>4가지 동시 재가격</h1>
  <p class="lede">코스피 −0.06%, S&P +0.13% — 하지만<br>달러·유가·금리·귀금속이 크게 흔들렸습니다.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷</div>
      <div class="rname">한국</div>
      <div class="verdict down">8,046 돌파 → -6.12% 폭락</div>
      <div class="num-row"><span class="nm">KOSPI WTD</span><span class="vl down">−0.06%</span></div>
      <div class="num-row"><span class="nm">KOSDAQ WTD</span><span class="vl down">−6.45%</span></div>
      <div class="num-row"><span class="nm">USD/KRW</span><span class="vl down">1,498 (+2.47%)</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict flat">대형주 보합 · 소형주 약세</div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl up">+0.13%</span></div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl down">−0.08%</span></div>
      <div class="num-row"><span class="nm">Russell2K</span><span class="vl down">−2.37%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--down)">
      <div class="flag">🌏</div>
      <div class="rname">아시아</div>
      <div class="verdict down">일제 약세</div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl down">−2.08%</span></div>
      <div class="num-row"><span class="nm">HSI</span><span class="vl down">−1.63%</span></div>
      <div class="num-row"><span class="nm">상하이</span><span class="vl down">−1.07%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--up)">
      <div class="flag">🛢️</div>
      <div class="rname">원자재 · FX</div>
      <div class="verdict up">에너지만 강세</div>
      <div class="num-row"><span class="nm">WTI WTD</span><span class="vl up">+10.48%</span></div>
      <div class="num-row"><span class="nm">Gold WTD</span><span class="vl down">−3.57%</span></div>
      <div class="num-row"><span class="nm">DXY WTD</span><span class="vl up">+1.41%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W20", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 5/11</div>
  <h1 class="day-headline">Hormuz 봉쇄 장기화<br>코스피 <span style="color:var(--orange)">+4.32%</span> 급등</h1>
  <p class="day-summary">
    Hormuz 해협 봉쇄 장기화 보도가 다시 부각되며<br>
    <strong>Brent +3.35% · WTI +3%+</strong> 유가 폭등으로 출발.<br><br>
    코스피는 단일일 <strong>+4.32%(7,822)</strong> 급등하며<br>
    8,000선이 처음 시야에 들어왔습니다.
  </p>
  <ul class="detail-list">
    <li>Brent +3.35% · WTI +3%+ — Hormuz 봉쇄 위험 재부각</li>
    <li>코스피 7,822 (+4.32%) — 8,000선 임박</li>
    <li>달러 강세·원화 약세 기조 본격화</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">7,822</div><div class="chg up">+4.32%</div></div>
    <div class="kpi"><div class="lbl">Brent</div><div class="val up">+3.35%</div><div class="chg up">Hormuz 급등</div></div>
    <div class="kpi"><div class="lbl">WTI</div><div class="val up">+3%+</div><div class="chg up">에너지 폭등</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 5/12</div>
  <h1 class="day-headline">차익실현 매도<br>코스피 <span style="color:var(--down)">−2.29%</span></h1>
  <p class="day-summary">
    월요일 급등에 대한 차익실현 압력이 작용.<br>
    코스피 <strong>−2.29%</strong>, 유럽도 STOXX50 −1.48%·DAX −1.62% 동반 약세.<br><br>
    유가는 Brent <strong>+2.84%</strong> 상승세를 이어갔고,<br>
    USD/KRW <strong>+1.22%</strong> 절하로 원화 약세가 두드러졌습니다.
  </p>
  <ul class="detail-list">
    <li>코스피 −2.29% — 월요일 급등 반납</li>
    <li>STOXX50 −1.48% · DAX −1.62% — 유럽 동반 약세</li>
    <li>Brent +2.84% 상승 지속 · USD/KRW +1.22% 원화 절하</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val down">−2.29%</div><div class="chg down">차익실현</div></div>
    <div class="kpi"><div class="lbl">Brent</div><div class="val up">+2.84%</div><div class="chg up">2일 연속 상승</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val down">+1.22%</div><div class="chg down">원화 약세</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "04 / 10"))
)

# 05 WEDNESDAY
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 5/13</div>
  <h1 class="day-headline">위험자산 동반 반등<br>NASDAQ <span style="color:var(--up)">+1.2%</span></h1>
  <p class="day-summary">
    화요일 하락에서 회복하며 위험자산 동반 반등.<br>
    코스피 <strong>+2.63%</strong> · NASDAQ <strong>+1.2%</strong> · 상하이 <strong>+0.67%</strong>.<br><br>
    트럼프-시진핑 정상회담 개막 기대 심리가 살아나며<br>
    글로벌 리스크온 분위기를 지지했습니다.
  </p>
  <ul class="detail-list">
    <li>코스피 +2.63% · NASDAQ +1.2% · 상하이 +0.67% 동반 반등</li>
    <li>트럼프-시진핑 정상회담 개막 — 기대 심리 부상</li>
    <li>위험회피 일시 완화 · 기술주 중심 회복</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+2.63%</div><div class="chg up">반등</div></div>
    <div class="kpi"><div class="lbl">NASDAQ</div><div class="val up">+1.2%</div><div class="chg up">기술주 회복</div></div>
    <div class="kpi"><div class="lbl">상하이</div><div class="val up">+0.67%</div><div class="chg up">정상회담 기대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "05 / 10"))
)

# 06 THURSDAY
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 5/14</div>
  <h1 class="day-headline">코스피 7,981<br>8,000선 재근접</h1>
  <p class="day-summary">
    코스피 <strong>+1.75%(7,981)</strong> — 8,000선에 다시 근접.<br>
    미국 2년물이 <strong>−9.78bp</strong> 단일일 급락하며<br>
    일시적 dovish 신호가 위험자산 반등을 지지했습니다.<br><br>
    트럼프-시진핑 정상회담 진행 중.
  </p>
  <ul class="detail-list">
    <li>코스피 7,981 (+1.75%) — 8,000선 재접근</li>
    <li>미국 2Y −9.78bp 일시 dovish — 금리 단기 완화</li>
    <li>트럼프-시진핑 정상회담 진행 — 합의 기대 유지</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">7,981</div><div class="chg up">+1.75%</div></div>
    <div class="kpi"><div class="lbl">US 2Y 단일일</div><div class="val up">−9.78bp</div><div class="chg up">일시 dovish</div></div>
    <div class="kpi"><div class="lbl">S&P500</div><div class="val up">+0.77%</div><div class="chg up">회복세</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "06 / 10"))
)

# 07 FRIDAY
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 5/15</div>
  <h1 class="day-headline">8,046 돌파 환희<br><span style="color:var(--down)">−6.12%</span> 절벽 추락</h1>
  <p class="day-summary">
    장중 사상 첫 <strong>8,046</strong> 돌파 환희가<br>
    한국 정부 고위 인사의 <strong>'AI 이익 재분배' 구상 시사</strong> 발언으로 뒤집혔습니다.<br><br>
    코스피 <strong>−6.12%</strong>(03-23 이후 최대 일일 낙폭).<br>
    삼성전자 <strong>−8.61%</strong> · SK하이닉스 <strong>−7.66%</strong> 동반 폭락.
  </p>
  <ul class="detail-list">
    <li>코스피 사상 첫 8,046 돌파 → 'AI 이익 재분배' 발언 하나로 반전</li>
    <li>삼성전자 −8.61% · SK하이닉스 −7.66% — 시총 40%+ 두 종목 폭락</li>
    <li>미국 2Y +13.82bp 재반전 — 목요일 dovish 완전 뒤집기</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val down">−6.12%</div><div class="chg down">03-23 이후 최대</div></div>
    <div class="kpi"><div class="lbl">삼성전자</div><div class="val down">−8.61%</div><div class="chg down">정책 직격</div></div>
    <div class="kpi"><div class="lbl">SK하이닉스</div><div class="val down">−7.66%</div><div class="chg down">정책 직격</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "07 / 10"))
)

# 08 INSIGHT 1 — 종가 보합 vs 내부 재가격
WEEKLY.append(("08_insight_policy", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 시장 구조</div>
  <h1 class="head">종가 보합 ≠ 시장 안정<br>내부는 완전히 달라졌다</h1>
  <p class="lede">코스피 −0.06%, S&P +0.13%가 말해주지 않는 것들</p>

  <div class="insight-box">
    <div class="qa">결과론적 환상을 깬 4가지 재가격</div>
    <p>
      ① <strong>DXY +1.41%</strong> — 광범위 달러 강세 재가속<br>
      ② <strong>WTI +10.48% · Brent +7.87%</strong> — Hormuz발 에너지 폭등<br>
      ③ <strong>US 2Y +19.10bp · 10Y +23.10bp</strong> — 채권금리 베어플랫<br>
      ④ <strong>금 −3.57% · 은 −4.10%</strong> — 귀금속 안전자산 균열<br><br>
      주간 종가만 보면 시장은 제자리처럼 보이지만,<br>
      인플레·금리·FX 전반의 레짐이 흔들린 한 주입니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">코스피 WTD</div><div class="val down">−0.06%</div><div class="chg">겉으로는 보합</div></div>
    <div class="kpi"><div class="lbl">DXY WTD</div><div class="val up">+1.41%</div><div class="chg down">달러 강세</div></div>
    <div class="kpi"><div class="lbl">US 2Y WTD</div><div class="val down">+19bp</div><div class="chg down">금리 급등</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "08 / 10"))
)

# 09 INSIGHT 2 — 정책 발언의 파급력
WEEKLY.append(("09_insight_concentration", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 지수 구조</div>
  <h1 class="head">발언 한 줄이<br>시총 40%를 흔들었다</h1>
  <p class="lede">코스피 −6.12%의 구조적 원인을 알아야 합니다</p>

  <div class="insight-box" style="border-left-color:var(--down)">
    <div class="qa" style="color:var(--down)">삼성전자 + SK하이닉스 = 코스피의 40%+</div>
    <p>
      코스피 지수의 시가총액 40% 이상을 삼성전자·SK하이닉스<br>
      두 종목이 차지합니다.<br><br>
      'AI 이익 재분배' 같은 <strong>단일 정책 신호</strong>가<br>
      이 두 종목에 직접 전이되면, 지수 전체가 절벽 추락하는<br>
      <span class="hl">구조적 취약성</span>이 다시 한번 확인됐습니다.<br><br>
      5/15 −6.12%는 2026-03-23 이후 최대 일일 낙폭입니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">5/15 코스피</div><div class="val down">−6.12%</div><div class="chg down">최대 일일 낙폭</div></div>
    <div class="kpi"><div class="lbl">삼성+하이닉스</div><div class="val down">40%+</div><div class="chg down">지수 비중</div></div>
    <div class="kpi"><div class="lbl">삼성전자</div><div class="val down">−8.61%</div><div class="chg down">SK하닉 −7.66%</div></div>
  </div>
</div>
""", "WEEKLY STORY · W20", "09 / 10"))
)

# 10 CLOSING / NEXT WEEK
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W21</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>정책·실적·지정학 — 세 변수 중 하나라도 부정적이면<br>코스피 7,300 지지선 테스트와 변동성 레짐 상향이 부상합니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">한국 'AI 이익 재분배' 정책 디테일</h4>
      <p style="color:#cfe0f3">단일 발언으로 −6.12% 폭락. 구체 정책 공개 시 코스피 추가 −5~7% 변동 가능. 삼성·하이닉스 직접 직격.</p>
    </div>
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">5/20(수) NVDA 실적 + FOMC 의사록</h4>
      <p style="color:#cfe0f3">NVDA 가이던스 하향 시 NASDAQ −2% 가능. FOMC 의사록 매파 시 US 2Y 4.2% 돌파 우려.</p>
    </div>
    <div class="risk-item med" style="background:rgba(203,96,21,.12);border-left-color:var(--warn)">
      <span class="tag" style="background:var(--warn)">MED</span>
      <h4 style="color:#fff">Hormuz 군사적 충돌 격화</h4>
      <p style="color:#cfe0f3">Brent $115+ 시 ECB·연준 매파 재가속. US 10Y 4.80%+, 신흥국 추가 압박.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-05-18 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W20</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W21 시나리오·포지셔닝 가이드
  </div>
  <div class="meta">2026-05-11 ~ 2026-05-15 · 5/5 영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">8,046 돌파 후<br>정책 충격 절벽 폭락</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">7,493</span>
    <span class="ch down">−0.06%</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD −0.06%</strong> · MTD +13.55% · YTD +73.87% — 주중 사상 첫 8,046 돌파 후 5/15 절벽 폭락</li>
    <li>5/15 단일일 <span class="down">−6.12%</span> — 'AI 이익 재분배' 정책 신호, 03-23 이후 최대 일일 낙폭</li>
    <li>KOSDAQ 1,129.82 · WTD <span class="down">−6.45%</span> — 대형주 폭락 동조</li>
    <li>USD/KRW 1,497.88 · WTD <span class="down">+2.47%</span> — 1,500선 임박, 광범위 달러 강세 직격</li>
    <li>KR 3Y <strong>3.766%</strong> · WTD +19.70bp, KR 10Y <strong>4.016%</strong> · WTD +26.80bp — 베어스팁닝</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">4.016%</div><div class="chg down">+26.80bp</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val">1,498</div><div class="chg down">+2.47% WTD</div></div>
    <div class="kpi"><div class="lbl">5/15 낙폭</div><div class="val down">−6.12%</div><div class="chg down">최대 일일</div></div>
  </div>
</div>
""", "PM STORY · W20", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">대형주 보합<br>소형주·반도체 약세</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">MTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,408.50</td><td class="vl up">+0.13%</td><td class="vl up">+2.77%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">26,225</td><td class="vl down">−0.08%</td><td class="vl up">+5.35%</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">2,793.30</td><td class="vl down">−2.37%</td><td class="vl down">−0.24%</td></tr>
    <tr><td class="nm">VIX</td><td class="vl">18.43</td><td class="vl down">+7.21%</td><td class="vl">5월 첫 18선</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일별 리듬: 목 5/14 S&amp;P +0.77%(2Y −9.78bp dovish) → 금 5/15 NASDAQ −1.54%(NVDA −3%)</li>
    <li>섹터 최강: <span class="up">SPDR Energy +6.71%</span> WTD 1위 / 최하위: <span class="down">SPDR REIT −2.66%</span></li>
    <li>MSFT <span class="up">+3.6%</span> (애크먼 지분 공개) — 시장 역행, 빅테크 내부 분화</li>
    <li>섹터 회전: 에너지·방어주 ↑ / 반도체·REIT ↓ — 인플레-금리 레짐 반영</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    5/20(수) NVDA 실적(EPS 컨센 $1.76) + FOMC 의사록이 W21 핵심
  </div>
</div>
""", "PM STORY · W20", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 및 중국</div>
  <h1 class="head">아시아 일제 약세<br>중국 반도체만 역행</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">MTD</th></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">61,409</td><td class="vl down">−2.08%</td><td class="vl up">+3.58%</td></tr>
    <tr><td class="nm">상하이</td><td class="vl">4,135</td><td class="vl down">−1.07%</td><td class="vl">—</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">25,963</td><td class="vl down">−1.63%</td><td class="vl">—</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">41,172</td><td class="vl down">−1.04%</td><td class="vl up">+5.77%</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>5/15 도미노: 한국발 매도 + 중국 정상회담 합의 부재 → 아시아 전 지수 동반 약세</li>
    <li><strong style="color:var(--blue)">중국 반도체 국산화 역행 강세</strong>: 5/15 AMEC <span class="up">+11.81%</span>, 피오테크 <span class="up">+7.49%</span>, 화창 <span class="up">+6.79%</span></li>
    <li>USD/JPY 158.77 · WTD <span class="down">+1.34%</span> — 엔 약세 재가속, 일본 정책 부담 누적</li>
    <li>트럼프-시진핑 정상회담: 2일 차까지 구체 합의 미공개 — 불확실성 유지</li>
  </ul>
</div>
""", "PM STORY · W20", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">달러 강세·유가 폭등<br>유럽 전 지수 약세</h1>

  <div class="region-grid">
    <div class="region-card europe">
      <div class="rname">유럽 전 지수 약세</div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl down">−1.42%</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl down">−1.59%</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl down">−1.97%</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">−0.37% (선방)</span></div>
    </div>
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl up">99.284 (+1.41%)</span></div>
      <div class="num-row"><span class="nm">Brent</span><span class="vl up">$109.26 (+7.87%)</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">$4,562 (−3.57%)</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl down">18.43 (+7.21%)</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:22px">
    <li>ECB 카자크스(5/14): "유가 상승이 기대인플레에 반영되면 다시 긴축 가능" — 매파 회귀 신호</li>
    <li>FTSE 선방: 에너지 비중이 유가 강세를 완충 · EUR/USD 1.163 (WTD −1.36%)</li>
    <li>UK 스타머 총리 리더십 도전 변수 — 유럽 위험회피 일부 기여</li>
  </ul>
</div>
""", "PM STORY · W20", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">글로벌 베어플랫<br>US 2Y 4% 위 안착</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">4.084%</div><div class="chg down">+19.10bp</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val">4.595%</div><div class="chg down">+23.10bp</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val">5.128%</div><div class="chg down">베어스팁</div></div>
  </div>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">KR 3Y</div><div class="val">3.766%</div><div class="chg down">+19.70bp</div></div>
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">4.016%</div><div class="chg down">+26.80bp</div></div>
    <div class="kpi"><div class="lbl">10Y-2Y</div><div class="val">51.1bp</div><div class="chg up">+8.49bp</div></div>
  </div>

  <ul class="detail-list">
    <li>5/14 2Y −9.78bp (일시 dovish) → 5/15 +13.82bp 재반전 — 하루 만에 뒤집기</li>
    <li>크레딧: TLT <span class="down">−2.81%</span> · AGG <span class="down">−1.17%</span> · HYG <span class="down">−0.85%</span> · EMB <span class="down">−1.50%</span> — 전 섹터 약세</li>
    <li>한국·미국 동시 베어스팁닝 — 듀레이션 자산 한 주 내내 압박</li>
  </ul>

  <div class="big-quote" style="margin-top:12px">
    US 2Y 4% 위 안착 + FOMC 의사록 톤 = W21 채권 핵심 변수
  </div>
</div>
""", "PM STORY · W20", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W21 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>5/18 ~ 5/22</h1>
  <p class="lede">한국 정책·NVDA 실적·Hormuz가 결정합니다</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL</div>
      <h4>정책 철회 + dovish 실적</h4>
      <div class="pp">확률: 낮음</div>
      <p>'AI 이익 재분배' 구상 철회 또는 제한적 형태 정리. FOMC 의사록 dovish + NVDA 컨센 상회. Hormuz 일부 해소 → 유가 $100↓. 코스피 7,700+, USD/KRW 1,470↓.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE (유력)</div>
      <h4>디테일 점진 공개 + 중립 실적</h4>
      <div class="pp">확률: 가장 유력</div>
      <p>정책 디테일 시행 시점 미정 유지. FOMC 중립, NVDA 컨센 부합. Brent $105~$112 박스. 코스피 7,300~7,700 박스, USD/KRW 1,490~1,510, US 2Y 4.0~4.15%.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR</div>
      <h4>정책 구체화 + 실적 미달</h4>
      <div class="pp">확률: 낮음~중간</div>
      <p>구체 AI 세금 정책 발표로 삼성·하이닉스 직격. NVDA 가이던스 하향. Hormuz 군사충돌 → Brent $115+. 코스피 7,000↓, US 10Y 4.80%+, VIX 22+.</p>
    </div>
  </div>
</div>
""", "PM STORY · W20", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W21 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li><strong>'AI 이익 재분배'</strong> 정책 디테일 공개 여부</li>
        <li>코스피 7,300 지지선 · USD/KRW 1,500 라인</li>
        <li>삼성 260,000원 · 하이닉스 1,700,000원 하방</li>
        <li>BOK 5/30(금) 금통위 사전 점검</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li><strong>5/20(수) FOMC 의사록</strong> — Warsh 의장 첫 신호</li>
        <li>5/22(금) Philadelphia Fed · S&amp;P PMI</li>
        <li>Brent $105 vs $112 · DXY 99 vs 100.5</li>
        <li>미국 실질금리 2.0%+ 안착 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아 및 중국</h4>
      <ul>
        <li>트럼프-시진핑 합의 윤곽 — 관세·반도체 제재 디테일</li>
        <li>일본 5/22(금) CPI + BOJ 정책 톤</li>
        <li>닛케이 61,000 지지 · HSI 25,800 · 상하이 4,100</li>
        <li>중국 반도체 국산화 모멘텀 지속 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 실적</h4>
      <ul>
        <li><strong>5/20(수) NVDA 실적</strong> — EPS 컨센 $1.76</li>
        <li>데이터센터 가이던스가 1차 변수</li>
        <li>Walmart · Home Depot — 소비 동향</li>
        <li>S&amp;P 7,350 · NASDAQ 26,000 · VIX 20 돌파 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>ECB 위원 추가 발언 — 카자크스 매파 확인</li>
        <li>UK 5/21(목) Initial Claims · 5/22(금) PMI</li>
        <li>STOXX50 5,800 지지 · DAX 23,800 · EUR/USD 1.16</li>
        <li>ECB 매파 재확인 시 유럽 채권 +30bp 가속 위험</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권</h4>
      <ul>
        <li>US 2Y 4.0~4.2% 안착 vs 이탈</li>
        <li>10Y-2Y 51bp → 60bp 스팁 vs 30bp 플랫</li>
        <li>US 10Y 4.70% 이탈 시 주식 멀티플 압박</li>
        <li>HY 스프레드 +20bp · TLT $82 이탈 모니터링</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W20", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W21 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>한국 'AI 이익 재분배' 정책 구체화</h4>
      <p>단일 발언으로 −6% 폭락을 유발한 만큼, 구체 정책 발표 시 코스피 단일일 −5~7% 추가 변동 가능. <strong>삼성·SK하이닉스 시총 40%+ 구조가 직접 전달 통로</strong>. USD/KRW 1,500 돌파 시 외국인 패닉 매도 재진입 위험.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>NVDA 실적 가이던스 하향 (5/20 장후)</h4>
      <p>데이터센터 가이던스 하향 시 NASDAQ 단일일 −2% 가능, 글로벌 반도체·기술주 동반 매도. <strong>한국 하이닉스·삼성전자에도 추가 충격</strong>. VIX 22+ 진입 시 방어자산 우위 모드 전환.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>Hormuz 군사적 충돌 격화</h4>
      <p>Brent $115+ 진입 시 ECB·연준 매파 재가속, US 10Y 4.80%+, 신흥국 자산 추가 압박. <strong>유가→기대인플레→정책 경로</strong>가 5월 들어 재작동 중임을 유의.</p>
    </div>
  </div>
</div>
""", "PM STORY · W20", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W21 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell uw"><div class="lbl">한국 주식</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">미국 주식</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">아시아·중국</div><div class="vl">N→UW</div></div>
    <div class="pos-cell uw"><div class="lbl">유럽 주식</div><div class="vl">UW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell uw"><div class="lbl">듀레이션채권</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">미국 단기채</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">에너지</div><div class="vl">OW</div></div>
    <div class="pos-cell n"><div class="lbl">귀금속</div><div class="vl">N→UW</div></div>
  </div>

  <div style="margin-top:30px;background:var(--bg-soft);border-radius:14px;padding:22px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:21px;color:var(--text);line-height:1.6;font-weight:500">
      한국·유럽 UW 유지 · 에너지 OW ·<br>USD 강세 대응 · NVDA 실적 확인 후 미국 판단
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W20", "10 / 10"))
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
