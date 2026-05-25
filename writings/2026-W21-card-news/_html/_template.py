"""
W21 Card News Generator  (2026-05-18 ~ 05-22)
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
  <div class="badge-week">W21 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">공포에서<br><span class="accent">환희</span>로<br>V자 반전</div>
  <div class="lead">
    이란 경고·채권 발작으로 3일 연속 하락한 코스피가<br>
    삼성 파업 타결+엔비디아 서프라이즈에 +8.42% 폭등.<br>
    <strong>WTD +4.73%</strong>로 마감한 한 주.
  </div>
  <div class="meta">2026-05-18 · 05-19 · 05-20 · 05-21 · 05-22</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">지정학 공포 → 이중 호재<br>주간 코스피 +4.73%</h1>
  <p class="lede">월~수 채권·유가 충격으로 코스피 7,208까지 추락<br>→ 목요일 삼성 타결+엔비디아 실적이 흐름을 뒤집었습니다.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷</div>
      <div class="rname">한국</div>
      <div class="verdict up">목요일 +8.42% 역사적 급등</div>
      <div class="num-row"><span class="nm">KOSPI WTD</span><span class="vl up">+4.73%</span></div>
      <div class="num-row"><span class="nm">KOSDAQ WTD</span><span class="vl up">+2.77%</span></div>
      <div class="num-row"><span class="nm">USD/KRW</span><span class="vl down">1,504</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict flat">엔비디아 실적에도 채권 부담</div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl up">+0.88%</span></div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl up">+0.45%</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl up">−9.39%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--up)">
      <div class="flag">🌏</div>
      <div class="rname">아시아</div>
      <div class="verdict up">일본·대만 AI 부품 주도</div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl up">+3.14%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl up">+2.17% (금)</span></div>
      <div class="num-row"><span class="nm">상하이</span><span class="vl down">−2.04% (목)</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--down)">
      <div class="flag">🛢️</div>
      <div class="rname">원자재 · 채권</div>
      <div class="verdict down">유가 급락·금리 고원</div>
      <div class="num-row"><span class="nm">WTI WTD</span><span class="vl down">−8.37%</span></div>
      <div class="num-row"><span class="nm">US 30Y</span><span class="vl down">5.064%</span></div>
      <div class="num-row"><span class="nm">DXY WTD</span><span class="vl up">+0.05%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W21", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 5/18</div>
  <h1 class="day-headline">이란 경고·사이드카<br>장중 <span style="color:var(--down)">−4.68%</span> 후 반등</h1>
  <p class="day-summary">
    주말 트럼프의 "이란, 시계가 가고 있다" 경고에<br>
    야간 <strong>Brent 112달러</strong>까지 급등하며 출발.<br><br>
    코스피는 장중 7,142(<strong>−4.68%</strong>)까지 추락하며<br>
    코스피200 선물 매도 사이드카가 발동됐으나,<br>
    개인 1.2조원 순매수로 종가 <strong>+0.31%</strong> 극적 반등.
  </p>
  <ul class="detail-list">
    <li>Brent 야간 112달러 급등 — Hormuz 봉쇄 공포 재부각</li>
    <li>코스피 사이드카 발동 후 개인 1.2조원 순매수로 종가 +0.31%</li>
    <li>유가 되돌림·삼성 노사 협상 기대가 반전 동력</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI 장중 저점</div><div class="val down">7,142</div><div class="chg down">−4.68%</div></div>
    <div class="kpi"><div class="lbl">KOSPI 종가</div><div class="val">+0.31%</div><div class="chg up">극적 반등</div></div>
    <div class="kpi"><div class="lbl">Brent 야간</div><div class="val up">$112</div><div class="chg down">이란 공포</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 5/19</div>
  <h1 class="day-headline">미 30Y <span style="color:var(--down)">5.197%</span><br>2007년 이후 최고치</h1>
  <p class="day-summary">
    미 30년물 국채 금리가 <strong>5.197%</strong>까지 치솟아<br>
    2007년 이후 <strong>19년 만의 최고치</strong> 경신.<br><br>
    "채권 자경단"의 복귀에 코스피 <strong>−3.25%</strong>(7,271) 재급락.<br>
    현대차 <strong>−9.05%</strong> 등 전날 반등 수혜주 이익실현.<br>
    USD/KRW는 <strong>1,507원</strong>까지 급등.
  </p>
  <ul class="detail-list">
    <li>US 30Y 5.197% — Moody's 강등·감세법안 재정 우려 발화</li>
    <li>코스피 −3.25%(7,271) 재급락 · 현대차 −9.05%</li>
    <li>USD/KRW 1,507 고점 — 광범위 위험회피</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val down">5.197%</div><div class="chg down">19년 최고</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val down">−3.25%</div><div class="chg down">채권 자경단</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val down">1,507</div><div class="chg down">고점</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "04 / 10"))
)

# 05 WEDNESDAY
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 5/20</div>
  <h1 class="day-headline">UK CPI 2.8% + 이란 진전<br>유럽 <span style="color:var(--up)">+2.13%</span> 반등</h1>
  <p class="day-summary">
    영국 4월 CPI <strong>2.8%</strong>(예상 3.0%)로 하회 서프라이즈,<br>
    트럼프의 "이란 협상 최종 단계" 발언이 더해지며<br>
    Brent는 <strong>−5.19%</strong> 단일일 최대 낙폭을 기록.<br><br>
    유럽 STOXX50 <strong>+2.13%</strong>·S&P500 <strong>+1.08%</strong> 반등.<br>
    아시아는 시차로 코스피 −0.86% 소외.
  </p>
  <ul class="detail-list">
    <li>UK CPI 2.8% — BOE 금리인하 기대 강화</li>
    <li>Brent −5.19% — 호르무즈 유조선 통과 호재</li>
    <li>유럽·미국 반등 / 아시아 시차로 소외</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Brent</div><div class="val down">−5.19%</div><div class="chg up">인플레 완화</div></div>
    <div class="kpi"><div class="lbl">STOXX50</div><div class="val up">+2.13%</div><div class="chg up">유럽 반등</div></div>
    <div class="kpi"><div class="lbl">S&P500</div><div class="val up">+1.08%</div><div class="chg up">금리 안정</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "05 / 10"))
)

# 06 THURSDAY — 핵심 반전일
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 5/21</div>
  <h1 class="day-headline">삼성 타결 + 엔비디아<br>코스피 <span style="color:var(--up)">+8.42%</span> 폭등</h1>
  <p class="day-summary">
    전날 밤 삼성전자 노사가 <strong>잠정 합의</strong>에 도달해<br>
    예정 파업이 중단됐고, 엔비디아가 분기 매출<br>
    <strong>$81.6B (+85% YoY)</strong> 역대 최고 실적 발표.<br><br>
    이중 호재로 코스피 <strong>+8.42%(7,815)</strong> 폭등.<br>
    SK하이닉스 <strong>+11.17%</strong> · LG전자 <strong>+29.83%</strong> ·<br>
    현대모비스 <strong>+25.23%</strong>가 주도.
  </p>
  <ul class="detail-list">
    <li>삼성 노사 잠정합의 — 반도체 이익 10.5% 보너스</li>
    <li>엔비디아 Q1 $81.6B(+85%) · 데이터센터 +92%</li>
    <li>코스피 +8.42% 역사적 단일 거래일 급등</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+8.42%</div><div class="chg up">7,815</div></div>
    <div class="kpi"><div class="lbl">SK하이닉스</div><div class="val up">+11.17%</div><div class="chg up">AI 수요</div></div>
    <div class="kpi"><div class="lbl">LG전자</div><div class="val up">+29.83%</div><div class="chg up">단일일</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "06 / 10"))
)

# 07 FRIDAY
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 5/22</div>
  <h1 class="day-headline">부품·방산 2차 랠리<br>코스닥 <span style="color:var(--up)">+4.99%</span></h1>
  <p class="day-summary">
    삼성전자·한미반도체 차익실현 매물이<br>
    <strong>삼성전기 +11.3%·SK Inc +11.5%</strong> 등 부품주와<br>
    <strong>한화오션 +7.6%·현대로템 +5.4%</strong> 방산주로 이동.<br><br>
    코스닥 <strong>+4.99%</strong>가 2차 랠리를 이끌었고,<br>
    닛케이225도 TDK·르네사스 등 전자부품주 주도로<br>
    <strong>+2.68%</strong> 상승하며 한 주를 마감.
  </p>
  <ul class="detail-list">
    <li>대형주 차익실현 → 부품·방산 2차 점화</li>
    <li>코스닥 +4.99% · 닛케이 +2.68% · TWSE +2.17%</li>
    <li>주간 마감: 코스피 WTD +4.73% / 닛케이 +3.14% / DAX +3.92%</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">코스닥</div><div class="val up">+4.99%</div><div class="chg up">2차 랠리</div></div>
    <div class="kpi"><div class="lbl">한화오션</div><div class="val up">+7.6%</div><div class="chg up">방산 회전</div></div>
    <div class="kpi"><div class="lbl">닛케이</div><div class="val up">+2.68%</div><div class="chg up">AI 부품</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "07 / 10"))
)

# 08 INSIGHT 1 — 채권 자경단
WEEKLY.append(("08_insight_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 채권 자경단</div>
  <h1 class="head">유가 → 인플레 → 금리<br>경로의 위력</h1>
  <p class="lede">미 30년물 5.197% — 2007년 이후 최고치가 의미하는 것</p>

  <div class="insight-box">
    <div class="qa">왜 채권이 주식의 적이 되었나</div>
    <p>
      이란 전쟁 이후 Brent <strong>+54%</strong> 급등이<br>
      인플레이션 기대를 끌어올리고,<br>
      Moody's 신용등급 강등(<strong>Aaa → Aa1</strong>)과<br>
      감세 법안 '빅뷰티플' 재정 충격이 맞물려<br>
      "채권 자경단"이 돌아왔다는 표현이 회자됐습니다.<br><br>
      수요일 유가 -5%·UK CPI 하회로 5.116%까지 후퇴했으나,<br>
      주간 마감은 <strong>5.064%</strong>로 <span class="hl">구조적 위협을 유지</span>.<br>
      BofA 설문 응답자 <strong>62%</strong>가 30Y 6% 도달을 예상합니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">30Y 주간 고점</div><div class="val down">5.197%</div><div class="chg down">19년 최고</div></div>
    <div class="kpi"><div class="lbl">30Y 마감</div><div class="val down">5.064%</div><div class="chg down">고원 유지</div></div>
    <div class="kpi"><div class="lbl">BofA 설문</div><div class="val">62%</div><div class="chg down">30Y 6% 예상</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "08 / 10"))
)

# 09 INSIGHT 2 — AI 슈퍼사이클
WEEKLY.append(("09_insight_nvidia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · AI 슈퍼사이클</div>
  <h1 class="head">엔비디아 +85% YoY<br>수혜는 공급망으로</h1>
  <p class="lede">설계사 → 후공정·부품 사이클 성숙의 신호</p>

  <div class="insight-box" style="border-left-color:var(--up)">
    <div class="qa" style="color:var(--up)">엔비디아 주가는 떨어졌는데, 왜 부품주가 폭등?</div>
    <p>
      엔비디아 Q1 매출은 <strong>$81.6B(+85% YoY)</strong>,<br>
      데이터센터 매출은 <strong>+92% YoY</strong>로 AI 인프라 폭발을 확인.<br>
      <strong>$80B 추가 자사주</strong>와 분기 배당 25배 인상까지 발표했지만<br>
      주가는 <strong>−1.77%</strong>로 "Buy rumor, sell news" 패턴.<br><br>
      대신 다음 날 <span class="hl">삼성전기·SK Inc 등 한국 부품주</span>와<br>
      TDK·르네사스 등 일본 전자부품주로 수혜가 빠르게 확산.<br>
      AI 수혜의 무게중심이 <strong>설계사에서 공급망으로</strong> 이동하는<br>
      사이클 성숙 단계의 모습입니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">NVDA Q1 매출</div><div class="val up">$81.6B</div><div class="chg up">+85% YoY</div></div>
    <div class="kpi"><div class="lbl">데이터센터</div><div class="val up">+92%</div><div class="chg up">YoY</div></div>
    <div class="kpi"><div class="lbl">NVDA 주가(목)</div><div class="val down">−1.77%</div><div class="chg down">매물 출회</div></div>
  </div>
</div>
""", "WEEKLY STORY · W21", "09 / 10"))
)

# 10 CLOSING / NEXT WEEK
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W22</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>미국 PCE(5/30)·이란 핵협상·'빅뷰티플' 상원 표결.<br>메모리얼 데이(5/25 월) US 휴장으로 한 주가 짧습니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">미국 재정 우려 — 30Y 5.06% 구조 상승</h4>
      <p style="color:#cfe0f3">Moody's 강등·'빅뷰티플' 상원 심의 잔존. 추가 재정 확대 신호 시 30Y 5.2% 재돌파 → 주식 멀티플 압박.</p>
    </div>
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">이란 핵협상 교착 — 유가 재급등 리스크</h4>
      <p style="color:#cfe0f3">금요일 이란 최고지도자 우라늄 반출 거부로 협상 교착. 결렬 시 WTI $100+ 재돌파·30Y 재상승 경로 활성화.</p>
    </div>
    <div class="risk-item med" style="background:rgba(203,96,21,.12);border-left-color:var(--warn)">
      <span class="tag" style="background:var(--warn)">MED</span>
      <h4 style="color:#fff">코스피 PER 29.76 — 밸류에이션 과열</h4>
      <p style="color:#cfe0f3">YTD +82%·VIX 16.70 단기 안정권. 외국인 매도 재가속·채권 충격 재발 시 변동성 재확대 가능.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-05-25 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W21</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W22 시나리오·포지셔닝 가이드
  </div>
  <div class="meta">2026-05-18 ~ 2026-05-22 · 5/5 영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">목요일 +8.42% V반등<br>코스피 WTD +4.73%</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">7,847.71</span>
    <span class="ch up">+0.41% (금)</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD +4.73%</strong> · MTD +18.93% · YTD <span class="up">+82.3%</span> — 월~수 7,208 추락 → 목 V반등 → 금 2차 랠리</li>
    <li>목요일 단일일 <span class="up">+8.42%</span> — 삼성전자 +8.51%, SK하이닉스 +11.17%, LG전자 +29.83%, 현대모비스 +25.23%</li>
    <li>KOSDAQ 1,161.13 · WTD <span class="up">+2.77%</span> — 부품·방산 2차 랠리(삼성전기 +11.3%, 한화오션 +7.6%)</li>
    <li>USD/KRW 1,504.4 · 화요일 1,507 고점 후 소폭 되돌림 · 외국인 WTD 순매도 지속</li>
    <li>KOSPI200 IT WTD <span class="up">+12%+</span>, 경기소비재 <span class="up">+13%+</span> 주도</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI WTD</div><div class="val up">+4.73%</div><div class="chg up">MTD +18.93%</div></div>
    <div class="kpi"><div class="lbl">목요일 단일</div><div class="val up">+8.42%</div><div class="chg up">역사적 급등</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val">1,504</div><div class="chg down">고점 1,507</div></div>
  </div>
</div>
""", "PM STORY · W21", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">엔비디아 호실적도<br>채권 부담에 제한적</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">MTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,473.47</td><td class="vl up">+0.88%</td><td class="vl up">+3.67%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">26,343.97</td><td class="vl up">+0.45%</td><td class="vl">—</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">—</td><td class="vl up">+0.91% (금)</td><td class="vl">—</td></tr>
    <tr><td class="nm">VIX</td><td class="vl">16.70</td><td class="vl down">−9.39%</td><td class="vl">단기 안정</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>NVIDIA <span class="down">−1.77%</span>(목) — Q1 매출 $81.6B(+85% YoY), 데이터센터 $75.2B(+92%), 추가 자사주 $80B</li>
    <li>월마트 <span class="down">−7.27%</span>(목) 급락 · Apple <span class="up">+1.26%</span>, 테슬라 <span class="up">+1.95%</span>(금) 방어</li>
    <li>Moody's 미국 신용등급 <span class="down">Aaa→Aa1</span> 강등 · '빅뷰티플' 재정 우려 잔존</li>
    <li>WTD +0.88%로 코스피·닛케이·DAX 대비 상대 저조 — 채권 압박이 지수 상승 여력 제한</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    "Buy rumor, sell news" — 엔비디아 실적이 한국·일본 공급망으로 이동
  </div>
</div>
""", "PM STORY · W21", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 및 중국</div>
  <h1 class="head">일본·대만 AI 부품 강세<br>중국은 미중 갈등 소외</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">금요일</th></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">63,339.07</td><td class="vl up">+3.14%</td><td class="vl up">+2.68%</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">42,267.97</td><td class="vl up">—</td><td class="vl up">+2.17%</td></tr>
    <tr><td class="nm">Shanghai</td><td class="vl">—</td><td class="vl">혼조</td><td class="vl down">−2.04%(목)</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">—</td><td class="vl">반등</td><td class="vl down">−1.03%(목)</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일본 AI 부품주 주도: TDK <span class="up">+7.3%</span>, 르네사스 <span class="up">+6.8%</span>, Fanuc <span class="up">+6.6%</span>, Murata <span class="up">+6.0%</span></li>
    <li>대만 ASE Tech <span class="up">+10.0%</span> — AI 반도체 공급망 수혜 극명</li>
    <li>중국 4월 산업생산 <span class="down">+4.1%</span>(예상 +5.9%), 고정자산투자 <span class="down">−1.6%</span>(예상 +1.6%) 쇼크</li>
    <li>중국 4월 소매판매 <span class="down">+0.2%</span>(예상 +2.0%) · 미중 항만 수수료 분쟁 확전</li>
    <li>홍콩 바이두 <span class="down">−5.74%</span>, 콰이쇼우 <span class="down">−5.66%</span> 목요일 약세</li>
  </ul>
</div>
""", "PM STORY · W21", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">유가 −8.37% 급락<br>유럽 DAX +3.92%</h1>

  <div class="region-grid">
    <div class="region-card europe">
      <div class="rname">유럽 (반도체·명품 이중 수혜)</div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl up">24,888.56 (+3.92%)</span></div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl up">6,019.45 (+2.13% 수)</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl up">8,115.75</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl up">10,466.30</span></div>
    </div>
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl up">+0.05% WTD</span></div>
      <div class="num-row"><span class="nm">WTI</span><span class="vl down">$96.60 (−8.37%)</span></div>
      <div class="num-row"><span class="nm">Brent</span><span class="vl down">$105 (-5.19% 수)</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">−0.76% WTD</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:22px">
    <li>UK CPI 4월 <span class="up">2.8%</span>(예상 3.0%, 전월 3.3%) — BOE 금리인하 기대 강화</li>
    <li>일본 1Q GDP <span class="up">+0.5%</span> QoQ(예상 +0.4%) 서프라이즈 — 닛케이 반응 제한적</li>
    <li>ASML·Infineon·STMicro 반도체 장비주 DAX 주도 · 리슈몽 +2.3% 명품주 강세</li>
    <li>이란 협상 결과가 에너지 인플레·금리 방향의 핵심 단기 변수</li>
  </ul>
</div>
""", "PM STORY · W21", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">30Y 5.197% 후 후퇴<br>구조적 우려 잔존</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">3.585%</div><div class="chg">단기 안정</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val">4.558%</div><div class="chg">중간 구간</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val down">5.064%</div><div class="chg down">고점 5.197%</div></div>
  </div>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">10Y-2Y</div><div class="val up">+97bp</div><div class="chg up">스티프닝</div></div>
    <div class="kpi"><div class="lbl">화요일 30Y</div><div class="val down">5.197%</div><div class="chg down">2007년 이후</div></div>
    <div class="kpi"><div class="lbl">BofA 설문</div><div class="val">62%</div><div class="chg down">30Y 6% 예상</div></div>
  </div>

  <ul class="detail-list">
    <li>주간 흐름: 화 매도 가속(5.197%) → 수 UK CPI+유가 -5%로 안정 → 금 5.064% 마감</li>
    <li>Moody's 미국 신용 <span class="down">Aaa → Aa1</span> 강등 · '빅뷰티플' 감세법안 텀 프리미엄 요구</li>
    <li>10Y-2Y +97bp — 스티프닝 지속, 듀레이션 자산 압박 구조</li>
  </ul>

  <div class="big-quote" style="margin-top:12px">
    이란 협상 → 유가 → 인플레 → 금리 안정 경로가 Base 시나리오
  </div>
</div>
""", "PM STORY · W21", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W22 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>5/25 ~ 5/30</h1>
  <p class="lede">PCE·이란·감세법안 — 메모리얼 데이 휴장으로 짧은 주</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL (30%)</div>
      <h4>이란 타결 + 금리 정상화</h4>
      <div class="pp">확률: 30%</div>
      <p>이란 핵협상 최종 타결 → WTI $90 하회 → 30Y 5% 이하 복귀. 삼성 노사합의 비준 완료·외국인 매도 전환. 코스피 8,000선 재도전, NASDAQ 추가 강세.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE (50%)</div>
      <h4>박스권 횡보 + 로테이션</h4>
      <div class="pp">확률: 50% (가장 유력)</div>
      <p>이란 협상 교착 유지 → 유가 $95~102 박스. 30Y 5.0~5.15% 고원 지속·지수 상단 제한. 코스피 7,600~7,900 횡보, 부품·방산 로테이션 유지. PCE가 단기 방향 결정.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR (20%)</div>
      <h4>이란 결렬 + 재정 우려</h4>
      <div class="pp">확률: 20%</div>
      <p>이란 협상 결렬 → WTI $105+ 재급등, 30Y 5.2%+ 재경신. 삼성 비준 실패·외국인 매도 가속 → 코스피 7,400 이하 재조정. VIX 20 돌파 시 변동성 레짐 전환 주의.</p>
    </div>
  </div>
</div>
""", "PM STORY · W21", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W22 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li><strong>삼성전자 노사합의 비준</strong> 여부</li>
        <li>코스피 7,600 지지 · 8,000 재도전</li>
        <li>외국인 매도세 전환 여부</li>
        <li>PER 29.76 밸류에이션 부담 점검</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li><strong>5/30 미국 PCE 디플레이터</strong> — 연준 금리 경로</li>
        <li>이란 핵협상 진행 (상시)</li>
        <li>WTI $95~102 박스 vs $105+ 이탈</li>
        <li>DXY 보합 vs 강세 재가속</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아 및 중국</h4>
      <ul>
        <li>중국 추가 부양책 발표 여부</li>
        <li>미중 항만 수수료 분쟁 확전 관찰</li>
        <li>닛케이 63,000 지지 · TWSE 42,000</li>
        <li>일본 BOJ 정책 톤 변화</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 정치·실적</h4>
      <ul>
        <li><strong>'빅뷰티플' 상원 표결</strong> — 재정·30Y 방향</li>
        <li>G7 정상회담 — 관세·AI 공동 성명</li>
        <li>5/25(월) 메모리얼 데이 휴장</li>
        <li>S&P 7,400 지지 · VIX 20 이탈 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>BOE 금리인하 기대 강도 점검</li>
        <li>DAX 24,500 지지 · STOXX50 6,000</li>
        <li>EUR/USD · GBP/USD 강세 지속 여부</li>
        <li>ASML·STMicro 등 반도체 장비주 모멘텀</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권</h4>
      <ul>
        <li>US 30Y 5.0~5.15% vs 5.2%+ 재돌파</li>
        <li>10Y-2Y +97bp 스티프닝 유지</li>
        <li>BofA 설문 62% 30Y 6% 시나리오 점검</li>
        <li>TLT·AGG 듀레이션 자산 유출 흐름</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W21", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W22 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>미국 재정·채권 충격 — 30Y 5.06% 구조 상승</h4>
      <p>Moody's 신용등급 강등(Aaa→Aa1)과 <strong>'빅뷰티플' 상원 심의</strong>가 W22 핵심 변수. 추가 재정 확대 신호 시 30Y 5.2% 재돌파 가능, 이는 주식 밸류에이션을 직접 압박. BofA 설문 62%가 30Y 6% 도달을 예상.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>이란 핵협상 결렬 — 유가 재급등</h4>
      <p>금요일 이란 최고지도자가 <strong>고농축 우라늄 해외 반출 거부</strong>로 협상 교착. 결렬 시 WTI $100+ 재돌파·채권 금리 상승 재개 경로 활성화. 호르무즈 봉쇄 장기화 꼬리 리스크 잔존.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>코스피 밸류에이션 과열 — PER 29.76 · YTD +82%</h4>
      <p>목요일 +8.42% 급등 이후 <strong>외국인 매도세 재연 가능성</strong>과 밸류에이션 부담 교차. VIX 16.70 단기 안정권이나 이란·채권 충격 재발 시 변동성 재확대 가능.</p>
    </div>
  </div>
</div>
""", "PM STORY · W21", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W22 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell ow"><div class="lbl">한국 부품·방산</div><div class="vl">OW</div></div>
    <div class="pos-cell n"><div class="lbl">미국 대형기술</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">일본 전자부품</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">유럽 반도체장비</div><div class="vl">OW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell uw"><div class="lbl">장기 듀레이션</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">IG 회사채</div><div class="vl">N</div></div>
    <div class="pos-cell uw"><div class="lbl">에너지 섹터</div><div class="vl">UW</div></div>
    <div class="pos-cell ow"><div class="lbl">구리</div><div class="vl">OW</div></div>
  </div>

  <div style="margin-top:30px;background:var(--bg-soft);border-radius:14px;padding:22px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:21px;color:var(--text);line-height:1.6;font-weight:500">
      AI 공급망 확산 추세 OW ·<br>30Y 5%+ 듀레이션 UW · PCE 확인 후 가속
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W21", "10 / 10"))
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
