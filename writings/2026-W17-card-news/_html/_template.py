"""
W17 Card News Generator
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
  <div class="badge-week">W17 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">KOSPI<br>사상 최고치 <span class="accent">랠리</span></div>
  <div class="lead">
    반도체 수출 +183%, GDP 서프라이즈, 빅테크 어닝.<br>
    아시아가 글로벌 증시의 중심에 선 한 주.
  </div>
  <div class="meta">2026-04-20 · 04-21 · 04-22 · 04-23 · 04-24</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">아시아 +4~6%, 유럽 −3%<br>같은 세계, 다른 결과</h1>
  <p class="lede">중동 지정학 · 반도체 수출 · 빅테크 어닝이<br>지역별로 정반대 결과를 만들었습니다.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷🇹🇼</div>
      <div class="rname">아시아</div>
      <div class="verdict up">압도적 강세 · 3연 ATH</div>
      <div class="num-row"><span class="nm">KOSPI</span><span class="vl up">+4.58%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl up">+5.78%</span></div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl up">+2.12%</span></div>
    </div>
    <div class="region-card europe">
      <div class="flag">🇪🇺</div>
      <div class="rname">유럽</div>
      <div class="verdict down">전 지수 약세</div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl down">−3.17%</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl down">−2.32%</span></div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl down">−2.88%</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict up">실적 반전 소폭 플러스</div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl up">+1.50%</span></div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl up">+0.55%</span></div>
      <div class="num-row"><span class="nm">WTI</span><span class="vl up">+12.58%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--gold)">
      <div class="flag">🛢️</div>
      <div class="rname">원자재 · 환율</div>
      <div class="verdict down" style="color:var(--gold)">유가 급등 · 금 약세</div>
      <div class="num-row"><span class="nm">Brent</span><span class="vl up">+9.68%</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">−2.84%</span></div>
      <div class="num-row"><span class="nm">USD/KRW</span><span class="vl">1,476.67</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W17", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 4/20</div>
  <h1 class="day-headline">정전 만료 D-1<br>유가가 먼저 반응했다</h1>
  <p class="day-summary">
    미-이란 정전 만료를 하루 앞둔 월요일,<br>
    <strong>Brent 유가가 +4.29%</strong> 급등하며 시장 첫날부터 긴장감이 드리웠습니다.<br><br>
    유럽·미국이 하락한 가운데 KOSPI는 <strong>+0.44%</strong>로 상대 강세를 보이며 주간 랠리의 토대를 닦았습니다.
  </p>
  <ul class="detail-list">
    <li>이틀 뒤 정전 만료를 앞두고 위험회피 심리 확산</li>
    <li>DAX −1.15%, CAC40 −1.12%, S&P500 −0.24%</li>
    <li>아시아만 상대적으로 견조 — KOSPI 6,219 (+0.44%)</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Brent</div><div class="val">+4.29%</div><div class="chg up">단일일 급등</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">6,219</div><div class="chg up">+0.44%</div></div>
    <div class="kpi"><div class="lbl">S&P500</div><div class="val mono">−0.24%</div><div class="chg down">정전 우려</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 4/21</div>
  <h1 class="day-headline">반도체 수출 <span style="color:var(--orange)">+183%</span><br>한국 시장 새 역사</h1>
  <p class="day-summary">
    관세청 발표 — 4월 1~20일 반도체 수출액이<br>
    <strong>전년 동기 대비 +183%</strong> 폭증.<br><br>
    SK하이닉스 +5.19%, 삼성전자 +2.10%의 대형주 주도로<br>
    KOSPI가 <strong>6,388.47</strong>로 사상 최고치를 경신했습니다.
  </p>
  <ul class="detail-list">
    <li>외국인 W17 누적 5.79조원 순매수 — AI HBM 수요 확인</li>
    <li>KOSPI +2.72% — 주중 최대 상승일</li>
    <li>같은 시각 유럽은 정전 만료 당일 불안에 추가 약세</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">반도체 수출</div><div class="val up">+183%</div><div class="chg up">YoY</div></div>
    <div class="kpi"><div class="lbl">KOSPI 첫 ATH</div><div class="val">6,388</div><div class="chg up">+2.72%</div></div>
    <div class="kpi"><div class="lbl">외국인 순매수</div><div class="val up">5.79조</div><div class="chg up">W17 누적</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "04 / 10"))
)

# 05 WEDNESDAY
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 4/22</div>
  <h1 class="day-headline">정전 무기한 연장<br>그런데 유가는 +8%</h1>
  <p class="day-summary">
    트럼프 대통령이 미-이란 정전을 무기한 연장 발표.<br>
    위험선호가 살아나며 한·미 동시 <strong>'트리플 ATH'</strong>가 찾아왔습니다.<br><br>
    그러나 정전 직후 이란이 호르무즈에서 선박 2척을 나포하며 <strong>WTI가 하루 +8.1%</strong> 폭등하는 아이러니가 펼쳐졌습니다.
  </p>
  <ul class="detail-list">
    <li>KOSPI 6,418 — 이틀 연속 ATH</li>
    <li>S&P500 +1.05%, NASDAQ +1.64% — 동시 사상 최고치</li>
    <li>장 마감 후 테슬라 어닝 서프라이즈</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">6,418</div><div class="chg up">+0.46% · 2연 ATH</div></div>
    <div class="kpi"><div class="lbl">NASDAQ</div><div class="val up">+1.64%</div><div class="chg up">트리플 ATH</div></div>
    <div class="kpi"><div class="lbl">WTI 단일일</div><div class="val up">+8.1%</div><div class="chg up">호르무즈 나포</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "05 / 10"))
)

# 06 THURSDAY
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 4/23</div>
  <h1 class="day-headline">GDP 서프라이즈<br>SW 쇼크 충돌</h1>
  <p class="day-summary">
    한국은행 Q1 GDP <strong>+1.7%</strong> — 컨센서스의 두 배.<br>
    KOSPI 사흘 연속 ATH(<strong>6,475.81</strong>) 달성.<br><br>
    그러나 미국 세션에서 <strong>IBM −8%, ServiceNow −18%</strong>의 SW 실적 쇼크 + 컨테이너선 공격 보도.<br>
    Brent가 $105.95까지 치솟으며 S&P500은 장중 신고점에서 −0.41% 반락.
  </p>
  <ul class="detail-list">
    <li>KOSPI 3연 ATH — 펀더멘탈 모멘텀 확인</li>
    <li>"AI 수익화는 반도체에만?" 우려 부각</li>
    <li>Brent 주중 최고 $105.95 — 인플레 재가속 우려</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KR Q1 GDP</div><div class="val up">+1.7%</div><div class="chg up">컨센 2배</div></div>
    <div class="kpi"><div class="lbl">IBM</div><div class="val down">−8%</div><div class="chg down">SW 쇼크</div></div>
    <div class="kpi"><div class="lbl">ServiceNow</div><div class="val down">−18%</div><div class="chg down">SW 쇼크</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "06 / 10"))
)

# 07 FRIDAY
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 4/24</div>
  <h1 class="day-headline">유가 급락 −6.4%<br>빅테크가 마무리했다</h1>
  <p class="day-summary">
    OPEC+ 증산 기대와 이란 외교 해소 보도에 <strong>Brent −6.44%($99.13)</strong> 급락.<br>
    한 주간의 유가 공포가 일부 해소.<br><br>
    아마존·메타·알파벳의 <strong>빅테크 어닝 서프라이즈</strong>가 NASDAQ을 +1.63% 견인하며 W17을 긍정 마무리.
  </p>
  <ul class="detail-list">
    <li>Amazon EPS $2.43 vs $1.94 컨센 — +25.3% beat</li>
    <li>Meta $7.21 vs $6.76 · Alphabet $2.81 vs $2.36</li>
    <li>TWSE +3.23% (TSMC +5.17%) — 반도체 체인 확산</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Brent</div><div class="val down">−6.44%</div><div class="chg down">유가 안도</div></div>
    <div class="kpi"><div class="lbl">NASDAQ</div><div class="val up">+1.63%</div><div class="chg up">빅테크 견인</div></div>
    <div class="kpi"><div class="lbl">TWSE</div><div class="val up">+3.23%</div><div class="chg up">TSMC +5.17%</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "07 / 10"))
)

# 08 INSIGHT 1 — KOSPI ATH
WEEKLY.append(("08_insight_kospi", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 한국 시장</div>
  <h1 class="head">KOSPI 3연 ATH<br>무엇이 달라졌나</h1>
  <p class="lede">단 3일 만에 사흘 연속 사상 최고치. 매우 이례적인 흐름의 배경은?</p>

  <div class="insight-box">
    <div class="qa">3가지 퍼즐이 동시에 맞아떨어진 한 주</div>
    <p>
      ① <strong>반도체 수출 +183%</strong> — AI HBM 수요 실측 확인<br>
      ② <strong>Q1 GDP +1.7%</strong> — 컨센서스 두 배의 펀더멘탈<br>
      ③ <strong>외국인 5.79조 순매수</strong> — 원화 강세가 환손실 리스크 축소<br><br>
      특히 외국인 수급이 핵심입니다. 원화 강세가 외국인의 환손실을 줄이며 유입을 가속했고, 금요일 보합 마감은 <span class="hl">자연스러운 속도 조절</span>로 해석됩니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">KOSPI WTD</div><div class="val up">+4.58%</div><div class="chg">YTD +50.26%</div></div>
    <div class="kpi"><div class="lbl">KOSPI PER</div><div class="val">26.83배</div><div class="chg">2025년말 대비 2배</div></div>
    <div class="kpi"><div class="lbl">외국인 W17</div><div class="val up">+5.79조</div><div class="chg">순매수</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "08 / 10"))
)

# 09 INSIGHT 2 — IRAN OIL
WEEKLY.append(("09_insight_oil", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 지정학</div>
  <h1 class="head">정전 연장인데<br>유가가 오른 이유</h1>
  <p class="lede">트럼프가 정전을 연장했는데 왜 유가가 +12.58% 올랐을까요?</p>

  <div class="insight-box" style="border-left-color:var(--down)">
    <div class="qa" style="color:var(--down)">핵심은 호르무즈 해협의 현실</div>
    <p>
      정전 = 미-이란 직접 군사 충돌 중단.<br>
      하지만 이란 혁명수비대가 <strong>제3국 민간 선박을 나포·공격</strong>하는 것은 막지 않습니다.<br><br>
      이번 주에만 이란이 <strong>선박 2척을 나포</strong>하고 컨테이너선을 공격했습니다.<br>
      호르무즈는 <span class="hl">전 세계 석유 무역의 약 20%</span>가 통과하는 병목.<br><br>
      이 병목이 흔들리면, 정전과 무관하게 유가는 즉시 반응합니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">WTI WTD</div><div class="val up">+12.58%</div><div class="chg up">$94.40</div></div>
    <div class="kpi"><div class="lbl">Brent WTD</div><div class="val up">+9.68%</div><div class="chg up">$99.13</div></div>
    <div class="kpi"><div class="lbl">금요일 안도</div><div class="val down">−6.44%</div><div class="chg down">OPEC+ 기대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W17", "09 / 10"))
)

# 10 CLOSING / NEXT WEEK
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W18</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>FOMC · 비농업고용 · 유가 경로 — 매파 시나리오로 기울 경우<br>US 10Y 4.5% 재테스트와 기술주 밸류에이션 압박이 부상합니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">FOMC (4/29~30) + NFP (5/1)</h4>
      <p style="color:#cfe0f3">파월의 기자회견 톤이 관건. 유가 $94~99 + 고용 견조 시 매파 전환 위험.</p>
    </div>
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">이란 지정학 — 금요일 안도는 일시적</h4>
      <p style="color:#cfe0f3">OPEC+ 증산 미확정 + 호르무즈 패턴 지속. Brent $105 재돌파 시 사이클 재가동.</p>
    </div>
    <div class="risk-item med" style="background:rgba(212,139,7,.1);border-left-color:#e8a73a">
      <span class="tag" style="background:#e8a73a">MED</span>
      <h4 style="color:#fff">KOSPI PER 26.8배 · 차익실현 리스크</h4>
      <p style="color:#cfe0f3">YTD +50% 반영. 5/1 휴장 전후 외국인 포지션 정리 집중 가능성.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-04-27 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W17</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W18 시나리오·포지셔닝 가이드
  </div>
  <div class="meta">2026-04-20 ~ 2026-04-24 · 5/5 영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">KOSPI 3연 ATH<br>역사적 프리미엄 구간</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">6,475.63</span>
    <span class="ch up">+4.58%</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD +4.58%</strong> · MTD +28.17% · YTD +50.26% — 화·수·목 3연 ATH</li>
    <li>KOSDAQ 1,203.84 (+2.89%) — 금 +2.51% 바이오·중소형 아웃퍼폼</li>
    <li>섹터: <span class="up">반도체 +4.46%</span> · 헬스케어 +4.25% // <span class="down">철강 −7.19%</span></li>
    <li>외국인 W17 누적 <strong>+5.79조원</strong> — 반도체 수출 + GDP 펀더멘탈</li>
    <li>USD/KRW 1,476.67 (+0.65%) · KR 10Y 3.683% (+10.30bp)</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">PER</div><div class="val">26.83배</div><div class="chg">2025말의 2배+</div></div>
    <div class="kpi"><div class="lbl">PBR</div><div class="val">2.07배</div><div class="chg">프리미엄</div></div>
    <div class="kpi"><div class="lbl">DY</div><div class="val">0.85%</div><div class="chg">압축</div></div>
  </div>
</div>
""", "PM STORY · W17", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">실적 혼조 → 빅테크<br>서프라이즈 반전</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,165.08</td><td class="vl up">+0.55%</td><td class="vl up">+4.67%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">24,836.60</td><td class="vl up">+1.50%</td><td class="vl up">+6.86%</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">—</td><td class="vl up">+0.36%</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일별 리듬: 월 −0.63% → 화 +1.05% (트리플 ATH) → 수 −0.41% (SW 쇼크) → 목 +0.80%</li>
    <li>섹터 1·꼴찌: <span class="up">Tech +3.80%</span> · Energy +3.36% // <span class="down">Health −3.10%</span></li>
    <li><strong style="color:var(--blue)">빅테크 EPS</strong>: Amazon $2.43 vs $1.94E (+25%) · Meta $7.21 vs $6.76E · Alphabet $2.81 vs $2.36E</li>
    <li>채권 ETF: TLT −0.41% · HYG −0.21% · TIPS +0.29% — 인플레 기대 유지</li>
  </ul>

  <div class="big-quote" style="margin-top:18px">
    FOMC 5월 동결 가격 반영 — 파월 톤이 W18 최대 변수
  </div>
</div>
""", "PM STORY · W17", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아</div>
  <h1 class="head">반도체 수출국 강세<br>에너지 수입국 부진</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">TWSE</td><td class="vl">38,932</td><td class="vl up">+5.78%</td><td class="vl up">+34.42%</td></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">59,716</td><td class="vl up">+2.12%</td><td class="vl up">+16.94%</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">25,978</td><td class="vl down">−0.70%</td><td class="vl">—</td></tr>
    <tr><td class="nm">Shanghai</td><td class="vl">4,080</td><td class="vl down">−0.69%</td><td class="vl">—</td></tr>
    <tr><td class="nm">NIFTY50</td><td class="vl">23,898</td><td class="vl down">−1.87%</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>TWSE 아시아 최강 — TSMC +5.17%, NVIDIA 데이터센터 추가 수주 기대</li>
    <li>USD/JPY 159.33 (+0.44%) · USD/CNY 6.836 (+0.26%) · USD/INR 94.11 (+1.14%)</li>
    <li><strong style="color:var(--blue)">분화 구조</strong>: 반도체 수출국(KR·TW)은 AI 직접 수혜, 에너지 수입국(인도)은 유가 충격</li>
  </ul>
</div>
""", "PM STORY · W17", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">유가 급등 → 유럽 직격<br>아시아와 8.9%p 분화</h1>

  <div class="region-grid">
    <div class="region-card europe">
      <div class="rname">유럽 전 지수 약세</div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl down">−3.17%</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">−2.70%</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl down">−2.32%</span></div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl down">−2.88%</span></div>
    </div>
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl up">+0.42%</span></div>
      <div class="num-row"><span class="nm">US 10Y</span><span class="vl">4.31% (+6.4bp)</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl up">+7.04% · 18.71</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">−2.84% · $4,741</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:24px">
    <li>유럽 하락 요인: ① 이란 유가 급등 (에너지 수입 의존) ② <strong>독일 GDP 1.0%→0.5% 하향</strong> ③ 유가 급락에도 에너지 섹터 매도</li>
    <li>예외: 로레알 +9% (CAC 목요일만 +0.87% 단독 플러스)</li>
    <li>EUR/USD 1.173 (−0.26%) · ECB 6월 25bp 인하 컨센 유지</li>
  </ul>
</div>
""", "PM STORY · W17", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">유가 발 인플레 우려<br>10Y 선행 상승</h1>

  <div style="font-size:14px;color:var(--orange);font-weight:700;letter-spacing:2px;margin:8px 0 10px">🇺🇸 미국 국채 (만기별)</div>
  <div class="kpi-row" style="margin-top:0;margin-bottom:18px">
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">3.593%</div><div class="chg down">−0.70bp</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val">4.310%</div><div class="chg up">+6.40bp</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val">4.916%</div><div class="chg up">+3.10bp</div></div>
  </div>

  <div style="font-size:14px;color:var(--orange);font-weight:700;letter-spacing:2px;margin:6px 0 10px">🇰🇷 한국 국채 + 美 2s10s</div>
  <div class="kpi-row" style="margin-top:0;margin-bottom:24px">
    <div class="kpi"><div class="lbl">KR 3Y</div><div class="val">3.496%</div><div class="chg up">+12.50bp</div></div>
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">3.683%</div><div class="chg up">+10.30bp</div></div>
    <div class="kpi"><div class="lbl">2s10s 스프레드</div><div class="val">71.7bp</div><div class="chg">장단기차</div></div>
  </div>

  <ul class="detail-list" style="margin-bottom:18px">
    <li>채권 ETF: <strong>TLT 86.71 (−0.41%)</strong> · AGG 99.59 (−0.26%) — 전반적 약세</li>
    <li>크레딧: HYG 80.48 (−0.21%) · LQD 109.60 (−0.40%) · EMB (−0.49%) — 신용위험 미미</li>
    <li>인플레 연동: <strong style="color:var(--up)">TIPS 111.80 (+0.29%)</strong> — 유가 하락에도 인플레 기대 유지</li>
    <li>한국 GDP +1.7% 서프라이즈 → <strong>한은 조기 인하 기대 후퇴</strong> (KR 금리 상승폭 &gt; US)</li>
  </ul>

  <div class="big-quote" style="margin-top:8px;font-size:24px">
    유가 $94~99 + 고용 호조 시 US 10Y 4.50% 테스트 가능 → Duration 축소 유지
  </div>
</div>
""", "PM STORY · W17", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W18 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>4/28 ~ 5/2</h1>
  <p class="lede">FOMC + NFP + 유가 경로가 결정합니다</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL</div>
      <h4>FOMC 비둘기 + 유가 안정</h4>
      <div class="pp">확률 25%</div>
      <p>파월 비둘기 톤 유지. NFP +20만 + 임금 둔화. Brent $95 이하 안착. KOSPI 6,600 돌파, NASDAQ 25,200, USD/KRW 1,460 방향.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE</div>
      <h4>동결 확인 + 유가 레인지</h4>
      <div class="pp">확률 55%</div>
      <p>FOMC 5월 동결, 파월 중립. NFP +15~20만. Brent $95~105 레인지. KOSPI 6,300~6,550, S&amp;P500 7,000~7,200. 빅테크 모멘텀 상방 지지.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR</div>
      <h4>파월 매파 + 유가 재급등</h4>
      <div class="pp">확률 20%</div>
      <p>"인플레 재가속 우려" 매파 전환. NFP +25만 + 임금 상승. Brent $105 재돌파. US 10Y 4.50% 테스트. KOSPI 6,100 이탈 시 PER 압박.</p>
    </div>
  </div>
</div>
""", "PM STORY · W17", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W18 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li>4/29 산업생산·소매판매</li>
        <li>4/30 경상수지</li>
        <li><strong>5/1 근로자의 날 휴장</strong></li>
        <li>외국인 차익실현·반도체 5월 초 수출</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li>4/28 US PCE · Personal Income</li>
        <li><strong>4/29~30 FOMC</strong></li>
        <li><strong>5/1 비농업고용 (NFP)</strong></li>
        <li>PCE &gt; 2.5% + NFP &gt; 25만 → 10Y 4.50%</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아</h4>
      <ul>
        <li>4/30 BOJ 결정회의 + 전망보고서</li>
        <li>4/30 중국 PMI (제조·서비스)</li>
        <li>JPY 160+ 시 긴급 개입 가능성</li>
        <li>중국 PMI &lt; 50 시 EM 매도 압력</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 실적</h4>
      <ul>
        <li>4/28 Apple · AMD 실적</li>
        <li>5/1 이후 추가 대형 실적</li>
        <li>Apple 가이던스(관세·중국)</li>
        <li>AMD AI 가속기 수주</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>4/30 유로존 Q1 GDP 속보</li>
        <li>4/30 유로존 4월 CPI 잠정</li>
        <li>독일 0.5% 하향 반영 여부</li>
        <li>GDP 미스 → ECB 6월 인하 확신</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🛢️</span>원자재·지정학</h4>
      <ul>
        <li><strong>5/2 OPEC+ 장관급 회의</strong></li>
        <li>이란 외교 협상 동향</li>
        <li>OPEC+ 증산 → Brent $90 하향</li>
        <li>호르무즈 재발 → Brent $108+</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W17", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W18 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>FOMC 매파 전환</h4>
      <p>유가 $94~99 + 고용 호조 조합에서 파월이 "인플레 우려 재부상" 언급 시 US 10Y 4.50% 돌파, 기술주 밸류에이션 압박. <strong>KOSPI PER 26.8배가 가장 취약</strong>.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>이란 호르무즈 재발</h4>
      <p>금요일 유가 급락이 OPEC+ 미확정 + 혁명수비대 패턴 구조적 지속이라는 점에서 일시적일 수 있음. <strong>Brent $105 재돌파</strong> 시 인플레→금리→성장주 매도 사이클 재가동.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>KOSPI 차익실현 집중</h4>
      <p>YTD +50%, PER 26.8배 진입. <strong>5/1 근로자의 날 휴장 전후 외국인 포지션 정리</strong> 집중 리스크. 6,200 이탈 시 지지선 확인 필요.</p>
    </div>
  </div>
</div>
""", "PM STORY · W17", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W18 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell ow"><div class="lbl">한국 주식</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">대만 주식</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">미국 기술</div><div class="vl">OW</div></div>
    <div class="pos-cell uw"><div class="lbl">유럽 주식</div><div class="vl">UW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell uw"><div class="lbl">미국 장기채</div><div class="vl">UW</div></div>
    <div class="pos-cell n"><div class="lbl">미국 단기채</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">Gold</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">원유</div><div class="vl">N→UW</div></div>
  </div>

  <div style="margin-top:36px;background:var(--bg-soft);border-radius:14px;padding:24px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:22px;color:var(--text);line-height:1.6;font-weight:500">
      반도체·AI 직접 수혜 지역 비중 유지 ·<br>유럽·장기채 축소 · 유가 하향 시 추가 UW 검토
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W17", "10 / 10"))
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
