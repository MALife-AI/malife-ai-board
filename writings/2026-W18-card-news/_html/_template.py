"""
W18 Card News Generator (2026-04-27 ~ 2026-05-01)
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
  <div class="badge-week">W18 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">전쟁과 실적의<br><span class="accent">교차</span></div>
  <div class="lead">
    평화안·사상 최고·유가 쇼크·빅테크 반전.<br>
    한 주에 4개의 전혀 다른 이야기가 펼쳐졌습니다.
  </div>
  <div class="meta">2026-04-27 · 04-28 · 04-29 · 04-30 · 05-01</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">평화→최고→쇼크→반전<br>4일로 본 세계</h1>
  <p class="lede">한 주의 흐름이 하루 단위로 전환되며<br>극단적 변동성 속 플러스 마감했습니다.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷</div>
      <div class="rname">한국</div>
      <div class="verdict up">3회 ATH · 시총 세계 8위</div>
      <div class="num-row"><span class="nm">KOSPI</span><span class="vl up">+1.90%</span></div>
      <div class="num-row"><span class="nm">4월 MTD</span><span class="vl up">+30.61%</span></div>
      <div class="num-row"><span class="nm">장중 고점</span><span class="vl">6,712</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict up">4월 역대급 상승</div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl up">+0.91%</span></div>
      <div class="num-row"><span class="nm">4월 전체</span><span class="vl up">+10.42%</span></div>
      <div class="num-row"><span class="nm">Apple</span><span class="vl up">+5.4%</span></div>
    </div>
    <div class="region-card asia">
      <div class="flag">🌏</div>
      <div class="rname">아시아</div>
      <div class="verdict up">반도체 모멘텀 유지</div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl down">−0.34%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl">−0.01%</span></div>
      <div class="num-row"><span class="nm">MSCI EM</span><span class="vl up">+0.61%</span></div>
    </div>
    <div class="region-card europe" style="border-left-color:var(--gold)">
      <div class="flag">🛢️</div>
      <div class="rname">원자재</div>
      <div class="verdict" style="color:var(--gold)">유가 급등 · 금 약세</div>
      <div class="num-row"><span class="nm">Brent</span><span class="vl up">+9.12%</span></div>
      <div class="num-row"><span class="nm">WTI 장중</span><span class="vl">$122</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">−1.68%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W18", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 4/27</div>
  <h1 class="day-headline">이란 평화안 제출<br>한·일 동시 ATH</h1>
  <p class="day-summary">
    주말 이란이 미국에 평화안을 제출했다는 보도가 나오며<br>
    <strong>위험선호</strong>로 한 주가 시작됐습니다.<br><br>
    KOSPI <strong>+2.15%</strong>(6,615.03)로 사상 최고치 경신,<br>
    닛케이225도 사상 처음 <strong>60,000선 돌파</strong>(60,537, +1.38%)했습니다.
  </p>
  <ul class="detail-list">
    <li>이란 평화안: 호르무즈 재개 + 분쟁 종식 제안</li>
    <li>IT·반도체 체인 글로벌 동조 강세</li>
    <li>NVIDIA +4.00%가 미국 시장 견인</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI ATH</div><div class="val">6,615</div><div class="chg up">+2.15%</div></div>
    <div class="kpi"><div class="lbl">Nikkei</div><div class="val">60,537</div><div class="chg up">60K 첫 돌파</div></div>
    <div class="kpi"><div class="lbl">NVIDIA</div><div class="val up">+4.00%</div><div class="chg up">Tech 견인</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 4/28</div>
  <h1 class="day-headline">KOSPI 장중 <span style="color:var(--orange)">6,700</span> 돌파<br>한국, 세계 8위로</h1>
  <p class="day-summary">
    KOSPI가 장중 <strong>6,712.73</strong>까지 치솟으며<br>
    6,700을 처음 돌파했습니다. 차익실현으로 6,641에 마감.<br><br>
    Bloomberg — 한국 시총이 <strong>영국을 추월해 세계 8위</strong>로 부상.<br>
    같은 시각 UAE OPEC 탈퇴로 유가는 다시 $100 접근.
  </p>
  <ul class="detail-list">
    <li>KOSPI 6,641 (+0.39%) — 2연 ATH</li>
    <li>BOJ GDP 1.0%→0.5% 하향 → 닛케이 −1.02%</li>
    <li>OpenAI 실적 미달 보도 → 나스닥 −0.90%</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">장중 고점</div><div class="val">6,712</div><div class="chg up">6,700 첫 돌파</div></div>
    <div class="kpi"><div class="lbl">한국 시총</div><div class="val">세계 8위</div><div class="chg up">영국 추월</div></div>
    <div class="kpi"><div class="lbl">WTI</div><div class="val up">+3.53%</div><div class="chg up">$100 접근</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "04 / 10"))
)

# 05 WEDNESDAY
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 4/29</div>
  <h1 class="day-headline">유가 폭등 +7~9%<br>파월 마지막 FOMC</h1>
  <p class="day-summary">
    호르무즈 해협 통행량이 거의 제로로 확인되며<br>
    <strong>WTI +7.0%, Brent +9.0%</strong> 폭등.<br><br>
    코스피는 에너지/화학 강세에 힘입어 <strong>3일 연속 ATH</strong>(6,690.90, +0.75%).<br>
    파월 의장 마지막 FOMC는 금리 동결 + 1992년 이후 최다 반대표.
  </p>
  <ul class="detail-list">
    <li>호르무즈 봉쇄로 WTI +7%, Brent +9%</li>
    <li>한국 에너지/화학 +5.03% 급등</li>
    <li>FOMC 동결 3.50~3.75% — 반대표 최다</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">6,690</div><div class="chg up">3연 ATH</div></div>
    <div class="kpi"><div class="lbl">WTI</div><div class="val up">+7.0%</div><div class="chg up">유가 폭등</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val up">+8.4bp</div><div class="chg up">FOMC 당일</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "05 / 10"))
)

# 06 THURSDAY
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 4/30</div>
  <h1 class="day-headline">WTI $122 쇼크<br>Alphabet이 반전</h1>
  <p class="day-summary">
    이란 군사타격 브리핑 보도로 WTI가 장중 <strong>$122</strong>까지 급등.<br>
    코스피 −1.38%로 사흘 만에 하락 전환.<br><br>
    그러나 유가는 $104로 반락하고,<br>
    <strong>Alphabet 클라우드 +63%</strong> 서프라이즈로 S&P500 +1.02% — 4월 +10.42% 확정.
  </p>
  <ul class="detail-list">
    <li>WTI 장중 최고 $122 → 마감 $104로 반락</li>
    <li>Alphabet +9.96% · META −8.55%(AI capex 부담)</li>
    <li>S&P500 4월 전체 +10.42% — 2020년 이후 최대</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">WTI 장중</div><div class="val">$122</div><div class="chg down">쇼크</div></div>
    <div class="kpi"><div class="lbl">Alphabet</div><div class="val up">+9.96%</div><div class="chg up">클라우드 +63%</div></div>
    <div class="kpi"><div class="lbl">S&P 4월</div><div class="val up">+10.42%</div><div class="chg up">역대급</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "06 / 10"))
)

# 07 FRIDAY
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 5/1</div>
  <h1 class="day-headline">메이데이 휴장<br>Apple이 마무리</h1>
  <p class="day-summary">
    한국·중국·홍콩 근로자의 날 휴장.<br>
    닛케이만 +0.38% 거래.<br><br>
    Apple이 Q2 매출 <strong>$111.2B(+17% YoY)</strong>, EPS $2.01(+22%) 발표하며<br>
    <strong>+5.4% 급등</strong>. S&P500은 +0.29%(7,230)로 5월 첫 거래일 사상 최고 경신.
  </p>
  <ul class="detail-list">
    <li>한국·중국·홍콩 메이데이 휴장</li>
    <li>Apple 기록 실적: 매출 +17%, EPS +22%</li>
    <li>S&P500 사상 최고 7,230.12 마감</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Apple</div><div class="val up">+5.4%</div><div class="chg up">기록 실적</div></div>
    <div class="kpi"><div class="lbl">S&P500</div><div class="val">7,230</div><div class="chg up">사상 최고</div></div>
    <div class="kpi"><div class="lbl">Brent</div><div class="val down">−0.53%</div><div class="chg">$108 안정</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "07 / 10"))
)

# 08 INSIGHT 1 — KOREA RALLY
WEEKLY.append(("08_insight_kospi", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 한국 시장</div>
  <h1 class="head">한국 시총 세계 8위<br>4월 +30% 반등의 의미</h1>
  <p class="lede">한 주 3회 ATH + 4월 글로벌 최강 반등. 무엇이 달라졌나?</p>

  <div class="insight-box">
    <div class="qa">3월 폭락에서 4월 역대급 반등까지</div>
    <p>
      관세 + 이란 쇼크로 3월 폭락했던 코스피가 4월 <strong>+30.61%</strong> 반등하며<br>
      <span class="hl">한국 시총이 영국을 추월해 세계 8위</span>로 부상했습니다.<br><br>
      배경 ① <strong>반도체 수출 호조</strong> — AI HBM 수요 지속 확인<br>
      배경 ② <strong>외국인 수급</strong> — 달러 약세가 환손실 리스크 완화<br>
      배경 ③ <strong>상대 강세</strong> — 유럽 −3%, 한국 +4~5% 분화<br><br>
      장중 6,700 돌파 후 마감 6,598은 자연스러운 속도 조절로 해석됩니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">KOSPI 4월</div><div class="val up">+30.61%</div><div class="chg">글로벌 최강</div></div>
    <div class="kpi"><div class="lbl">한국 시총</div><div class="val">$4T</div><div class="chg up">세계 8위</div></div>
    <div class="kpi"><div class="lbl">장중 고점</div><div class="val">6,712</div><div class="chg">화요일</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "08 / 10"))
)

# 09 INSIGHT 2 — OIL PARADOX
WEEKLY.append(("09_insight_oil", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 유가</div>
  <h1 class="head">$100~$122 밴드<br>새로운 균형점</h1>
  <p class="lede">호르무즈 봉쇄 + 이란 타격 위협에도 $122→$108 반락이 가능했던 이유?</p>

  <div class="insight-box" style="border-left-color:var(--down)">
    <div class="qa" style="color:var(--down)">공급 충격 vs 협상 기대의 줄다리기</div>
    <p>
      이번 주 유가는 극단을 오갔습니다.<br>
      UAE OPEC 탈퇴 + 호르무즈 봉쇄 + 이란 타격 브리핑 = <strong>WTI $122</strong><br>
      주말 협상 기대 + OPEC+ 증산 가능성 = <strong>$104~108 반락</strong><br><br>
      시장은 <span class="hl">"$100 이하 회귀는 어렵지만 $120 이상 장기 유지도 힘든"</span> 균형점을 찾아가는 중입니다.<br><br>
      UAE 탈퇴로 OPEC 가격 조정 메커니즘이 약화되면서,<br>
      중동 지정학이 유가의 유일한 방향 결정자가 되고 있습니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">Brent WTD</div><div class="val up">+9.12%</div><div class="chg up">$107.96</div></div>
    <div class="kpi"><div class="lbl">WTI 주중 최고</div><div class="val">$122</div><div class="chg">목요일</div></div>
    <div class="kpi"><div class="lbl">주말 반락</div><div class="val">$108</div><div class="chg">협상 기대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W18", "09 / 10"))
)

# 10 CLOSING / NEXT WEEK
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W19</div>
  <h2>다음 주<br>주목할 <span class="accent">3대 리스크</span></h2>
  <p>이란 협상·4월 고용보고서·Fed 리더십 전환<br>— 세 변수가 W19 방향을 결정합니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">이란 군사타격 실행 여부</h4>
      <p style="color:#cfe0f3">트럼프가 타격 브리핑을 받고 있으며, 협상 교착 시 추가 공격 가능성 상존. 실행 시 Brent $120+ 재시도.</p>
    </div>
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">4월 고용보고서 (5/2)</h4>
      <p style="color:#cfe0f3">에너지 물가 급등 속 노동시장 건강이 핵심. 예상보다 약하면 스태그플레이션 내러티브 강화.</p>
    </div>
    <div class="risk-item med" style="background:rgba(212,139,7,.1);border-left-color:#e8a73a">
      <span class="tag" style="background:#e8a73a">MED</span>
      <h4 style="color:#fff">Fed 리더십 진공</h4>
      <p style="color:#cfe0f3">파월 5/15 퇴임, Warsh 인준 일정 불확실. 중간기 Fed 의사소통 공백이 채권·FX 변동성 높일 가능성.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-05-04 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W18</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    W18 수치 회고 + W19 시나리오·포지셔닝<br>
    이란·고용·Fed 전환기 대응 전략
  </div>
  <div class="meta">2026-04-27 ~ 2026-05-01 · 4/5 영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">3회 ATH 경신<br>시총 세계 8위 부상</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">6,598.87</span>
    <span class="ch up">+1.90%</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD +1.90%</strong> · MTD +30.61% — 월·화·수 3연 ATH</li>
    <li>장중 고점 6,712.73(화) — 6,700 첫 돌파 후 차익실현</li>
    <li>한국 시총 <strong>$4T 돌파</strong> — 영국 추월 세계 8위(Bloomberg)</li>
    <li>KOSDAQ 1,192.35 (+1.54%) — 주 초반 AI·바이오 강세</li>
    <li>섹터: IT +4.24%, 에너지/화학 +5.03% 리더 · 헬스케어·금융 부진</li>
    <li>USD/KRW 1,471.32 (−0.36%) — 원화 소폭 강세</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">외국인 W18</div><div class="val up">+1.2조</div><div class="chg">순매수 지속</div></div>
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">3.78%</div><div class="chg up">+3.5bp</div></div>
    <div class="kpi"><div class="lbl">4월 MTD</div><div class="val up">+30.61%</div><div class="chg">글로벌 최강</div></div>
  </div>
</div>
""", "PM STORY · W18", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">4월 +10.42%<br>빅테크 EPS 분화</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">4월</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,230.12</td><td class="vl up">+0.91%</td><td class="vl up">+10.42%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">25,114.44</td><td class="vl up">+1.12%</td><td class="vl up">+11.28%</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">2,812.82</td><td class="vl up">+0.93%</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일별: 월 +1.02%(이란 평화) → 화 −0.33% → 수 −0.21%(FOMC) → 목 +1.02%(Alphabet) → 금 +0.29%(Apple)</li>
    <li>4월 전체 <strong>+10.42%</strong> — 2020년 11월 이후 최대 월간 상승</li>
    <li>빅테크: <span class="up">Apple +5.4%, Alphabet +9.96%</span> // <span class="down">META −8.55%</span></li>
    <li>Q1 어닝: 80% EPS beat율 · Apple 매출 +17% · Alphabet 클라우드 +63%</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    4월 역대급 랠리 — 5월은 이란·고용·Fed 전환기가 방향 결정
  </div>
</div>
""", "PM STORY · W18", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 및 중국</div>
  <h1 class="head">닛케이 60K 돌파 후<br>조정 · EM 강세 유지</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">닛케이225</td><td class="vl">59,513</td><td class="vl down">−0.34%</td><td class="vl up">+17.2%</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">—</td><td class="vl">−0.01%</td><td class="vl up">+35%</td></tr>
    <tr><td class="nm">상하이</td><td class="vl">4,112</td><td class="vl up">+0.46%</td><td class="vl">—</td></tr>
    <tr><td class="nm">항셍</td><td class="vl">25,776</td><td class="vl down">−0.54%</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>닛케이 월요일 사상 첫 60,000 돌파(60,537) 후 조정</li>
    <li>BOJ GDP 1.0%→0.5% 하향(4/28) — 엔화 강세 전환</li>
    <li>MSCI EM 64.13 (WTD +0.61%, MTD +12.92%) — 신흥국 4월 강세</li>
    <li>USD/JPY 157.06 (−1.43%) — 엔화 강세 전환</li>
  </ul>
</div>
""", "PM STORY · W18", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">FOMC 동결 + 파월 퇴임<br>유럽 보합</h1>

  <div class="region-grid">
    <div class="region-card us" style="border-left-color:var(--blue)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl">98.156 (−0.36%)</span></div>
      <div class="num-row"><span class="nm">US 10Y</span><span class="vl">4.378% (+1.6bp)</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl">18.2 (−5%)</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">$4,661 (−1.68%)</span></div>
    </div>
    <div class="region-card europe">
      <div class="rname">유럽 보합</div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl">5,881 (−0.03%)</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl up">24,169 (+0.06%)</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl down">8,077 (−1.82%)</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">10,363 (−0.15%)</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:24px">
    <li>FOMC 4/29 동결 3.50~3.75% — 1992년 이후 최다 반대표(Miran 인하 주장)</li>
    <li>파월: "에너지 인플레가 정책 경로 복잡하게" + 5/15 퇴임 후 이사직 잔류 선언</li>
    <li>US Q1 GDP +2.0%(연율) · PCE 3.5% — 유가 상승분 아직 미반영</li>
  </ul>
</div>
""", "PM STORY · W18", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">FOMC 당일 +8.4bp<br>커브 플래트닝</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:24px">
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val">4.378%</div><div class="chg up">+1.6bp</div></div>
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">3.888%</div><div class="chg up">+3.0bp</div></div>
    <div class="kpi"><div class="lbl">10-2 Spread</div><div class="val">49bp</div><div class="chg down">−8.2bp</div></div>
  </div>

  <div class="kpi-row" style="margin-bottom:24px">
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">3.78%</div><div class="chg up">+3.5bp</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val">4.966%</div><div class="chg up">+1.0bp</div></div>
    <div class="kpi"><div class="lbl">TLT</div><div class="val down">−1.27%</div><div class="chg down">장기채 약세</div></div>
  </div>

  <ul class="detail-list">
    <li>FOMC 당일 US 10Y +8.4bp 급등 후 5/1 −0.3bp 반락</li>
    <li>단기물 상승 > 장기물 — 인하 기대 후퇴 + 커브 플래트닝</li>
    <li>크레딧: LQD −0.91%, HYG −0.52% — 금리 상승 + 스프레드 소폭 확대</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    유가 $105~115 + 고용 견조 시 US 10Y 4.5% 돌파 리스크
  </div>
</div>
""", "PM STORY · W18", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W19 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>5/4 ~ 5/8</h1>
  <p class="lede">이란 협상 · NFP · 유가 경로가 결정합니다</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL</div>
      <h4>이란 합의 + NFP 견조</h4>
      <div class="pp">확률 20%</div>
      <p>호르무즈 재개통 합의 공식 발표. Brent $95 아래 급락. NFP +200K + 임금 안정. S&P500 7,400 돌파, KOSPI 6,700 재시도.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE</div>
      <h4>협상 진행 중 + NFP 예상선</h4>
      <div class="pp">확률 55%</div>
      <p>이란 협상 "진행 중" 결론 없음. Brent $105~115 밴드. NFP +150~180K 예상 부합. S&P500 7,100~7,300 박스권, KOSPI 6,500~6,700.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR</div>
      <h4>트럼프 타격 + NFP 쇼크</h4>
      <div class="pp">확률 25%</div>
      <p>이란 추가 군사타격 실행. Brent $125+ 재시도. NFP 급감 or 임금 급등 → 스태그플레 우려. S&P500 −3~5% 조정, KOSPI 6,400 이하.</p>
    </div>
  </div>
</div>
""", "PM STORY · W18", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W19 WATCH POINTS</div>
  <h1 class="head">주목할 6대 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국 / 🌏 아시아</h4>
      <ul>
        <li><strong>5/5(월) 한국 어린이날</strong> — 연휴 후 5/6 개장</li>
        <li>휴장 동안 해외 흐름 반영 갭 주목</li>
        <li>코스피 6,700 재돌파 여부</li>
        <li>If 유가 $120+ → 에너지 강세 but 지수 하방</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 / 🌐 매크로</h4>
      <ul>
        <li><strong>5/2(금) 4월 고용보고서(NFP)</strong> — 예상 +165K</li>
        <li>에너지 물가 속 고용 건강 확인</li>
        <li>5/5~8 어닝: AMD, Uber, Disney 등</li>
        <li>If NFP < +100K → 스태그플레 −2%+</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>5/5(월) 유로존 4월 PMI 확정치</li>
        <li>DAX 24,000 지지 여부</li>
        <li>에너지 인플레가 ECB 정책에 미치는 영향</li>
        <li>If ECB 추가 인상 시사 → 성장주 압박</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권 / 원자재</h4>
      <ul>
        <li>US 10Y 4.3~4.5% 밴드 예상</li>
        <li>고용 서프라이즈 시 4.5% 돌파 가능</li>
        <li>Brent: 협상 따라 $105~120 밴드</li>
        <li>Gold: $4,600~4,750 지정학 헤지</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">📊</span>Fed 전환</h4>
      <ul>
        <li>파월 5/15 퇴임, Warsh 인준 진행</li>
        <li>중간기 의사소통 공백 리스크</li>
        <li>채권·FX 변동성 확대 가능성</li>
        <li>트럼프 해임 위협 vs 이사직 잔류</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">⚠</span>리스크 체크</h4>
      <ul>
        <li>이란 군사타격 브리핑 후속</li>
        <li>호르무즈 완전 봉쇄 확인 시 $130+</li>
        <li>한국 5/1 휴장 전후 외국인 정리</li>
        <li>KOSPI PER 압박 vs 반도체 모멘텀</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W18", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W19 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>이란 군사타격 실행</h4>
      <p>트럼프가 이란 타격 브리핑을 받고 있으며, 협상 교착 시 추가 공격 가능성 상존. <strong>호르무즈 완전 봉쇄 확인 시 Brent $130+</strong>, 글로벌 리스크오프 촉발.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>4월 NFP 쇼크 (5/2)</h4>
      <p>에너지 물가 급등 속 고용 급감 시 <strong>스태그플레이션 내러티브 본격화</strong>. 반대로 고용 강세 + 임금 상승은 금리 인하 기대 추가 후퇴로 직결.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>Fed 리더십 진공</h4>
      <p>파월 5/15 퇴임, Warsh 인준 일정 불확실. 중간기 Fed 의사소통 공백이 <strong>채권·FX 변동성</strong>을 높일 수 있음. 트럼프 해임 위협과 정면 충돌.</p>
    </div>
  </div>
</div>
""", "PM STORY · W18", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W19 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell ow"><div class="lbl">한국 주식</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">미국 대형주</div><div class="vl">OW</div></div>
    <div class="pos-cell n"><div class="lbl">유럽 주식</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">신흥국 주식</div><div class="vl">OW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell uw"><div class="lbl">미국 장기채</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">원유(Brent)</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">금</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">현금</div><div class="vl">N</div></div>
  </div>

  <div style="margin-top:36px;background:var(--bg-soft);border-radius:14px;padding:24px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:22px;color:var(--text);line-height:1.6;font-weight:500">
      반도체·AI 수혜 + 어닝 80% beat 비중 유지 ·<br>유가 인플레 + Fed 동결 장기화 → 장기채 축소
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W18", "10 / 10"))
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
        "--virtual-time-budget=4000",
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
