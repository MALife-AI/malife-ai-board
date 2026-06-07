"""
W23 Card News Generator  (2026-06-01 ~ 06-05)
- 신고점 8,801 돌파 직후 AVGO 가이던스 미스 + NFP 서프라이즈로 서킷브레이커
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
  <div class="badge-week">W23 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">신고점 8,801<br><span class="accent">돌파</span> 직후<br>서킷브레이커</div>
  <div class="lead">
    AVGO AI 가이던스 미스 + NFP 서프라이즈 쌍악재.<br>
    코스피 <strong>−3.72%</strong>·SOXX <strong>−10.44%</strong>·VIX <strong>+39.7%</strong>로 마감.
  </div>
  <div class="meta">2026-06-01 · 06-02 · 06-03(휴) · 06-04 · 06-05</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">월·화 신고점 8,801 돌파<br>금요일 서킷브레이커</h1>
  <p class="lede">AVGO AI 칩 가이던스 $16B (예상 $17.2B 하회) + 미국 5월 NFP +172K<br>두 충격이 같은 주에 겹치며 글로벌 AI 랠리에 제동.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia" style="border-left-color:var(--down)">
      <div class="flag">🇰🇷</div>
      <div class="rname">한국</div>
      <div class="verdict down">금요일 서킷브레이커</div>
      <div class="num-row"><span class="nm">KOSPI WTD</span><span class="vl down">−3.72%</span></div>
      <div class="num-row"><span class="nm">KOSDAQ WTD</span><span class="vl down">−6.73%</span></div>
      <div class="num-row"><span class="nm">USD/KRW</span><span class="vl down">1,559 (+3.43%)</span></div>
    </div>
    <div class="region-card us" style="border-left-color:var(--down)">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국</div>
      <div class="verdict down">SOXX 반도체 −10.44%</div>
      <div class="num-row"><span class="nm">S&P500</span><span class="vl down">−2.59%</span></div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl down">−4.68%</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl down">21.51 (+39.7%)</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--up)">
      <div class="flag">🌏</div>
      <div class="rname">아시아</div>
      <div class="verdict up">JP·TW 상대 방어</div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl up">+0.39%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl up">+0.76%</span></div>
      <div class="num-row"><span class="nm">상하이</span><span class="vl down">−1.00%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--warn)">
      <div class="flag">🛢️</div>
      <div class="rname">크로스에셋</div>
      <div class="verdict down">비전형 — 금↓ 유가↑</div>
      <div class="num-row"><span class="nm">금 WTD</span><span class="vl down">−4.90%</span></div>
      <div class="num-row"><span class="nm">WTI WTD</span><span class="vl up">+3.64%</span></div>
      <div class="num-row"><span class="nm">DXY WTD</span><span class="vl up">+1.17%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W23", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 6/1</div>
  <h1 class="day-headline">코스피 <span style="color:var(--up)">+3.68%</span><br>8,788 임박</h1>
  <p class="day-summary">
    반도체·IT 대형주 중심의 강한 외국인 순매수가 이어지며<br>
    코스피는 <strong>+3.68% (8,788)</strong>까지 급등.<br><br>
    YTD 누적 <strong>+93%</strong>에 육박하는 사상 최강 흐름.<br>
    8,800선 돌파가 가시권에 진입했고,<br>
    글로벌 AI 슈퍼사이클 모멘텀이 한 주의 출발을 지지.
  </p>
  <ul class="detail-list">
    <li>외국인 강한 순매수 — 반도체·IT 대형주 집중</li>
    <li>코스피 8,788 (+3.68%) · YTD +93%</li>
    <li>8,800선 돌파 가시권 — AI 모멘텀 연장</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">+3.68%</div><div class="chg up">8,788</div></div>
    <div class="kpi"><div class="lbl">YTD</div><div class="val up">+93%</div><div class="chg up">사상 최강</div></div>
    <div class="kpi"><div class="lbl">외국인</div><div class="val up">대량 순매수</div><div class="chg up">반도체 IT</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 6/2</div>
  <h1 class="day-headline">코스피 <span style="color:var(--up)">8,801</span><br>첫 8,800 돌파</h1>
  <p class="day-summary">
    코스피 <strong>+0.15% (8,801)</strong>로<br>
    사상 처음 <strong>8,800선</strong>을 넘어섰습니다.<br><br>
    미국 증시도 완만한 상승세를 이어가며<br>
    나스닥 YTD <strong>+10%</strong>대를 유지.<br>
    한 주의 고점 — 이후 모든 반전은 이 지점부터 시작됩니다.
  </p>
  <ul class="detail-list">
    <li>KOSPI 8,801 첫 돌파 — 주간 고점이자 W23의 정점</li>
    <li>나스닥 YTD +10%대 유지 · 미국 완만한 상승</li>
    <li>VIX 15선대 저변동 국면 — 시장 안도</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val up">8,801</div><div class="chg up">첫 돌파</div></div>
    <div class="kpi"><div class="lbl">NASDAQ YTD</div><div class="val up">+10%대</div><div class="chg up">유지</div></div>
    <div class="kpi"><div class="lbl">시장</div><div class="val">정점</div><div class="chg">주간 고점</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "04 / 10"))
)

# 05 WEDNESDAY — 한국 휴장 + AVGO 가이던스 미스
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 6/3 — 한국 휴장</div>
  <h1 class="day-headline">AVGO 가이던스 미스<br><span style="color:var(--down)">$16B vs $17.2B</span></h1>
  <p class="day-summary">
    한국은 휴장이었으나, 미국 장 마감 후<br>
    <strong>브로드컴(AVGO)이 Q3 실적</strong>을 발표했습니다.<br><br>
    AI 칩 매출 가이던스가 <strong>$16B</strong>로<br>
    시장 컨센서스 <strong>$17.2B를 7%</strong> 하회.<br>
    AVGO 시간외 <strong>−18%</strong>, AI 수요에 대한<br>
    의구심이 한 번에 확산되며 분위기가 급전환.
  </p>
  <ul class="detail-list">
    <li>AVGO Q3 AI 칩 가이던스 $16B (예상 $17.2B 하회)</li>
    <li>"AI 인프라 무한 확장" 가정에 첫 균열</li>
    <li>AVGO AH −18% · 한국은 휴장으로 충격 흡수 지연</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">AVGO 가이던스</div><div class="val down">$16B</div><div class="chg down">컨센 $17.2B</div></div>
    <div class="kpi"><div class="lbl">미스 폭</div><div class="val down">−$1.2B</div><div class="chg down">−7%</div></div>
    <div class="kpi"><div class="lbl">AVGO AH</div><div class="val down">−18%</div><div class="chg down">시간외</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "05 / 10"))
)

# 06 THURSDAY
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 6/4</div>
  <h1 class="day-headline">코스피 <span style="color:var(--down)">−1.84%</span><br>이틀 충격 반영</h1>
  <p class="day-summary">
    한국 증시가 이틀 공백을 한꺼번에 반영,<br>
    코스피는 <strong>−1.84% (8,639)</strong>로 하락.<br><br>
    미국 S&P500은 <strong>+0.41%</strong> 소폭 반등했으나<br>
    반도체 섹터 매도 압력은 지속.<br>
    AVGO 쇼크가 글로벌 AI 공급망으로 전이되는 첫 신호.
  </p>
  <ul class="detail-list">
    <li>코스피 -1.84%(8,639) — AVGO 충격 일부 흡수</li>
    <li>미국 S&P +0.41% 소폭 반등 / 반도체 섹터는 약세 지속</li>
    <li>삼성전자·SK하이닉스 등 HBM 공급망 동반 압박</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val down">−1.84%</div><div class="chg down">8,639</div></div>
    <div class="kpi"><div class="lbl">S&P500</div><div class="val up">+0.41%</div><div class="chg up">소폭 반등</div></div>
    <div class="kpi"><div class="lbl">반도체</div><div class="val down">약세</div><div class="chg down">AVGO 전이</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "06 / 10"))
)

# 07 FRIDAY — NFP + 서킷브레이커
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 6/5</div>
  <h1 class="day-headline">NFP <span style="color:var(--down)">+172K</span> 서프라이즈<br>코스피 서킷브레이커</h1>
  <p class="day-summary">
    미국 5월 NFP <strong>+172K</strong>(예상 +145K)가<br>
    연준의 금리 인하 기대를 후퇴시켰습니다.<br><br>
    AVGO 쇼크와 매크로 충격이 겹치면서<br>
    코스피는 장중 <strong>서킷브레이커 발동</strong><br>
    <strong>−5.54% (8,161)</strong>로 급락.<br>
    나스닥 <strong>−4.18%</strong>, SOXX <strong>−10.44%</strong>로 마무리.
  </p>
  <ul class="detail-list">
    <li>NFP +172K 예상 상회 → 연내 금리인하 기대 후퇴</li>
    <li>코스피 −5.54%(8,161) 장중 서킷브레이커 발동</li>
    <li>SOXX −10.44% · 반도체 시총 $1조 소멸</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">NFP</div><div class="val down">+172K</div><div class="chg down">예상 +145K</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val down">−5.54%</div><div class="chg down">서킷브레이커</div></div>
    <div class="kpi"><div class="lbl">SOXX</div><div class="val down">−10.44%</div><div class="chg down">반도체 직격</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "07 / 10"))
)

# 08 INSIGHT 1 — Good News Is Bad News
WEEKLY.append(("08_insight_paradox", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 매크로 역설</div>
  <h1 class="head">Good News Is<br><span style="color:var(--down)">Bad News</span></h1>
  <p class="lede">고용 서프라이즈가 왜 주가에 악재로 작용했는가</p>

  <div class="insight-box" style="border-left-color:var(--down)">
    <div class="qa" style="color:var(--down)">강한 고용 = 강한 경기 = ... 그런데 왜 시장은 하락?</div>
    <p>
      미국 5월 NFP <strong>+172K</strong>는 경기 건전성을 확인해줬지만,<br>
      <span class="hl">연준의 금리 인하 기대를 후퇴</span>시키며 주식 시장에는 악재.<br><br>
      US 10Y는 주간 <strong>+8bp 상승</strong>해 4.54%에 도달했고,<br>
      달러/원 환율은 <strong>+3.43%</strong> 급등하며 1,559원.<br>
      외국인의 한국 자산 달러 환산 매력도가 낮아졌습니다.<br><br>
      "경기가 강하면 금리도 강하다" — 인플레이션 잔존 국면에서<br>
      <strong>좋은 뉴스가 곧 나쁜 뉴스</strong>가 되는 패턴이 다시 작동했습니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">NFP 5월</div><div class="val down">+172K</div><div class="chg down">예상 +145K</div></div>
    <div class="kpi"><div class="lbl">US 10Y WTD</div><div class="val down">+8bp</div><div class="chg down">4.54%</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val down">+3.43%</div><div class="chg down">1,559</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "08 / 10"))
)

# 09 INSIGHT 2 — 비전형 패턴 (금 하락 + 유가 상승)
WEEKLY.append(("09_insight_atypical", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 크로스에셋</div>
  <h1 class="head">금 <span style="color:var(--down)">−4.90%</span><br>유가 <span style="color:var(--up)">+3.64%</span></h1>
  <p class="lede">이번 공포의 성격은 "지정학"이 아닌 "금리"였습니다</p>

  <div class="insight-box">
    <div class="qa">통상의 리스크오프와 무엇이 다른가</div>
    <p>
      통상적인 리스크오프에서는 <strong>금이 상승</strong>하지만,<br>
      W23에서 금은 <strong>−4.90%</strong>로 오히려 하락.<br>
      반면 WTI유는 <strong>+3.64%</strong>로 역행 상승했습니다.<br><br>
      이는 충격의 성격이 <span class="hl">"지정학적 위기"가 아닌<br>
      "실적 실망 + 금리 상승"</span>임을 반영합니다.<br>
      달러 강세(DXY +1.17%) 속 금 매도,<br>
      에너지 수요 기대에 유가 상승이라는 비전형 패턴.<br><br>
      W24에 같은 패턴이 이어지면 자산배분 가설을 점검해야 합니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:24px">
    <div class="kpi"><div class="lbl">금 WTD</div><div class="val down">−4.90%</div><div class="chg down">$4,337</div></div>
    <div class="kpi"><div class="lbl">WTI WTD</div><div class="val up">+3.64%</div><div class="chg up">$90.54</div></div>
    <div class="kpi"><div class="lbl">DXY WTD</div><div class="val up">+1.17%</div><div class="chg up">100</div></div>
  </div>
</div>
""", "WEEKLY STORY · W23", "09 / 10"))
)

# 10 CLOSING — W24 변수
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W24</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>핵심은 6/11 발표 예정 미국 5월 CPI.<br>NVDA·AMD 추가 가이던스와 USD/KRW 1,580선 방어 여부도 결정적입니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">미국 5월 CPI 재가속 (6/11)</h4>
      <p style="color:#cfe0f3">WTI YTD +57.68% 에너지 비용이 충분히 반영되지 않았다면 CPI 서프라이즈로 금리 재급등 가능. 9월 인하 기대도 흔들릴 수 있습니다.</p>
    </div>
    <div class="risk-item" style="background:rgba(217,48,79,.12);border-left-color:var(--down)">
      <span class="tag" style="background:var(--down)">HIGH</span>
      <h4 style="color:#fff">AI 수요 추가 실망 — NVDA·AMD</h4>
      <p style="color:#cfe0f3">AVGO 이후 엔비디아·AMD 가이던스에서 유사 신호가 나오면 SOXX 추가 조정 가능. AI 슈퍼사이클 재평가 국면 진입.</p>
    </div>
    <div class="risk-item med" style="background:rgba(203,96,21,.12);border-left-color:var(--warn)">
      <span class="tag" style="background:var(--warn)">MED</span>
      <h4 style="color:#fff">USD/KRW 1,580+ 돌파 위험</h4>
      <p style="color:#cfe0f3">외국인 한국 주식·채권 동반 이탈 가속 시 한은 긴급 외환 개입 여부 주목. 1,560 지지 → 1,540 회복이 안정 신호.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-06-08 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W23</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W24 시나리오·포지셔닝 가이드<br>
    (서킷브레이커 주, 4거래일)
  </div>
  <div class="meta">2026-06-01 ~ 2026-06-05 · 한국 6/3 휴장</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국</div>
  <h1 class="head">신고점 8,801 후 서킷브레이커<br>WTD −3.72%</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">8,161</span>
    <span class="ch down">−5.54% (금)</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD −3.72%</strong> · YTD <span class="up">+93.65%</span> — 주간 고점 8,801(화) → 금 8,161 서킷브레이커</li>
    <li>KOSDAQ 1,002 · WTD <span class="down">−6.73%</span> · YTD <span class="up">+8.32%</span> — 코스피 대비 상대적 약세 지속</li>
    <li>상위 종목: 삼성화재 <span class="up">+22.14%</span> · 신한지주 <span class="up">+14.85%</span> · KB금융 <span class="up">+13.94%</span> — <strong>금융주 차별화</strong></li>
    <li>하위 종목: 삼성SDI <span class="down">−17.44%</span> · 삼성전기 <span class="down">−17.40%</span> · 포스코퓨처엠 <span class="down">−14.87%</span></li>
    <li>USD/KRW 1,559 · WTD <span class="down">+3.43%</span> · YTD <span class="down">+8.21%</span> — 외국인 자금 유출 우려</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI WTD</div><div class="val down">−3.72%</div><div class="chg down">8,161</div></div>
    <div class="kpi"><div class="lbl">YTD</div><div class="val up">+93.65%</div><div class="chg up">고점 부담</div></div>
    <div class="kpi"><div class="lbl">USD/KRW</div><div class="val down">1,559</div><div class="chg down">+3.43% WTD</div></div>
  </div>
</div>
""", "PM STORY · W23", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국</div>
  <h1 class="head">SOXX −10.44%<br>AI 수요 재평가</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,384</td><td class="vl down">−2.59%</td><td class="vl up">+7.86%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">25,709</td><td class="vl down">−4.68%</td><td class="vl">—</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">2,834</td><td class="vl down">−2.94%</td><td class="vl">상대 선방</td></tr>
    <tr><td class="nm">VIX</td><td class="vl">21.51</td><td class="vl down">+39.7%</td><td class="vl">Elevated</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>AVGO 시간외 <span class="down">−18%</span>(수) — Q3 AI 칩 가이던스 $16B (컨센 $17.2B 미스 $1.2B)</li>
    <li>SOXX <span class="down">−10.44%</span> WTD — 반도체 시총 약 $1조 소멸. AI 슈퍼사이클 재평가 국면</li>
    <li>Russell2K <span class="down">−2.94%</span> 상대 선방 — 대형 기술주 쏠림 해소 조짐</li>
    <li>VIX 21.51 (+39.7% WTD) — Elevated 구간 진입. 25 돌파 시 변동성 확대 모드</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    "AI 인프라 무한 확장" 가정에 첫 균열 — NVDA·AMD 차기 가이던스가 W24 분기점
  </div>
</div>
""", "PM STORY · W23", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 및 중국</div>
  <h1 class="head">JP·TW 상대 방어<br>EM은 동반 급락</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">66,588</td><td class="vl up">+0.39%</td><td class="vl up">+32.28%</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">45,071</td><td class="vl up">+0.76%</td><td class="vl up">+55.61%</td></tr>
    <tr><td class="nm">Shanghai</td><td class="vl">4,028</td><td class="vl down">−1.00%</td><td class="vl">—</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">24,962</td><td class="vl down">−0.88%</td><td class="vl">—</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>니케이 상대 강세 — 엔 약세(USD/JPY 160 +0.68%) + 에너지 수혜 이중 호재</li>
    <li>대만 TWSE +0.76% — TSMC 상대 방어, 메모리(韓) 대비 시스템 반도체(臺) 디커플링</li>
    <li>NIFTY50 23,367 <span class="down">−0.77%</span> · 인도 상대 약세</li>
    <li><strong>MSCI EM <span class="down">−5.85% WTD</span></strong> — 한국 비중 반영 EM 전반 급락</li>
    <li>중국 부양책 모멘텀 부재 + 미중 갈등 잔존 — 본토는 -1% 박스</li>
  </ul>
</div>
""", "PM STORY · W23", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽</div>
  <h1 class="head">NFP +172K 충격<br>유가 +3.64% 역행</h1>

  <div class="region-grid">
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">NFP 5월</span><span class="vl down">+172K (vs 145K)</span></div>
      <div class="num-row"><span class="nm">WTI</span><span class="vl up">$90.54 (+3.64%)</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl down">$4,337 (−4.90%)</span></div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl up">100 (+1.17%)</span></div>
    </div>
    <div class="region-card europe">
      <div class="rname">유럽 (상대 선방)</div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl up">6,062 (+0.19%)</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl up">8,218 (+0.43%)</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl down">24,759 (−1.38%)</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">10,368 (−0.40%)</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:22px">
    <li>실업률 3.8% 유지 + NFP +172K — 연내 1회 인하 컨센서스도 흔들림</li>
    <li>WTI YTD <span class="up">+57.68%</span> — 에너지 인플레가 5월 CPI에 충분히 반영됐는지가 W24 분기점</li>
    <li>EUR/USD 1.15 (<span class="down">−1.11% WTD</span>) · GBP/USD 1.34 — 달러 강세에 유럽 통화 약세</li>
    <li>유럽 선진지수는 반도체 비중 낮아 상대 방어 — 그러나 MSCI EMEA <span class="down">−7.26%</span> 신흥 유럽은 급락</li>
  </ul>
</div>
""", "PM STORY · W23", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 · 금리</div>
  <h1 class="head">US 10Y +8bp · KR 10Y +20bp<br>한국이 더 가팔랐다</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val down">3.62%</div><div class="chg down">+4bp</div></div>
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val down">4.54%</div><div class="chg down">+8bp WTD</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val down">5.00%</div><div class="chg down">+1bp</div></div>
  </div>

  <div class="kpi-row" style="margin-top:0;margin-bottom:22px">
    <div class="kpi"><div class="lbl">10Y-2Y</div><div class="val">91bp</div><div class="chg">+5bp 스팁</div></div>
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val down">4.12%</div><div class="chg down">+20bp WTD</div></div>
    <div class="kpi"><div class="lbl">KR 3Y</div><div class="val down">3.88%</div><div class="chg down">+15bp</div></div>
  </div>

  <ul class="detail-list">
    <li>KR 10Y +20bp가 US 10Y +8bp의 <strong>2.5배</strong> — NFP+AVGO 복합 + 외국인 채권 매도</li>
    <li>크레딧 ETF 동반 약세: TLT $85.06 <span class="down">−0.82%</span> · LQD <span class="down">−1.09%</span> · HYG <span class="down">−1.10%</span></li>
    <li>커브: 10Y-2Y 91bp(+5bp) — 베어 스팁 패턴 유지 시 장기물 추가 압박</li>
  </ul>

  <div class="big-quote" style="margin-top:12px">
    6/11 CPI가 W24 분기점 — 상회 시 4.6%+ 재진입, 하회 시 4.4% 안도 랠리
  </div>
</div>
""", "PM STORY · W23", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W24 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>6/8 ~ 6/12</h1>
  <p class="lede">미국 5월 CPI(6/11) · NVDA·AMD 추가 가이던스 · USD/KRW 1,560 방어</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL (낮음)</div>
      <h4>CPI 하회 + 반도체 호재</h4>
      <div class="pp">기대 복원</div>
      <p>미국 CPI 하회 → 연내 인하 기대 복원. 반도체 추가 AI 수주 → AVGO 우려 해소. KOSPI 8,400~8,600 회복, US 10Y 4.3~4.4% 재진입, USD/KRW 1,520~1,540.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE (유력)</div>
      <h4>CPI 부합 + 박스 등락</h4>
      <div class="pp">가장 유력</div>
      <p>CPI 부합 → 금리 안정·추가 상승 억제. KOSPI 8,000~8,300 등락, S&P 7,300~7,500, USD/KRW 1,540~1,570, US 10Y 4.4~4.6% 안착. AVGO 여진 지속.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR (낮음)</div>
      <h4>CPI 상회 + AI 재실망</h4>
      <div class="pp">복합 충격</div>
      <p>CPI 상회 → 인하 기대 소멸, 금리 재급등. 추가 반도체 가이던스 미스 → AI 버블 우려. KOSPI 7,800 하방, US 10Y 4.7% 시도, USD/KRW 1,580~1,600.</p>
    </div>
  </div>
</div>
""", "PM STORY · W23", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W24 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li><strong>KOSPI 8,000 지지</strong> 여부 — 기술적 반등 가능성</li>
        <li>USD/KRW 1,560 저항 · 1,590 돌파 = 추가 이탈</li>
        <li>삼성·하이닉스 자사주 매입·코멘트 — 낙폭 과대 인식 반등</li>
        <li>금융주(삼성화재·신한지주) 모멘텀 지속</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li><strong>미국 5월 CPI 6/11</strong> — W24 핵심 변수</li>
        <li>WTI $90 유지 시 CPI 상방 리스크 증가</li>
        <li>DXY 100선 지지 — 강세 시 EM 추가 약세</li>
        <li>CPI &gt;예상 + PPI 강세 → 9월 인하도 불투명</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아 및 중국</h4>
      <ul>
        <li>니케이 글로벌 기술주 조정 속 상대 우위</li>
        <li>TWSE — TSMC AVGO 쇼크 여진 모니터</li>
        <li>USD/CNY 6.77 위안 안정 · 부양 동향</li>
        <li>MSCI EM −5.85% 이후 반등 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 실적·지표</h4>
      <ul>
        <li><strong>NVDA·AMD</strong> 차기 가이던스 변화 주시</li>
        <li>SOXX −10.44% 후 기술적 반등 vs 재평가</li>
        <li>VIX 21.51 — 25 돌파 시 변동성 확대</li>
        <li>러셀2K 상대 선방 → 자금 이동 신호</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>STOXX50·CAC40 상대 강세 지속 여부</li>
        <li>ECB 추가 인하 기대 유지 · EUR/USD 1.15</li>
        <li>CPI 하회 → EUR/USD 1.17+ 회복 가능</li>
        <li>DAX 24,759 — 독일 제조업 지표 점검</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권</h4>
      <ul>
        <li>US 10Y 4.6% 돌파 → 주식 추가 압박</li>
        <li>4.4% 재진입 → 안도 랠리 신호</li>
        <li>KR 10Y +20bp — 한은 통화정책 재점검</li>
        <li>HYG −1.10% — 크레딧 스프레드 모니터</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W23", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W24 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>CPI 재가속 (6/11 발표)</h4>
      <p>WTI YTD <strong>+57.68%</strong> 에너지 비용이 5월 CPI에 충분히 반영되지 않았다면, 6/11 발표치가 예상을 상회하며 금리 재급등을 촉발할 수 있습니다. 9월 인하 기대도 흔들릴 수 있습니다.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>AI 수요 추가 실망 — NVDA·AMD</h4>
      <p>엔비디아·AMD 등 주요 반도체 기업의 실적·코멘트에서 <strong>AVGO와 유사한 신호</strong>가 나올 경우 SOXX 추가 조정 예상. AI 슈퍼사이클 재평가 국면이 본격화될 수 있습니다.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>USD/KRW 1,580+ 돌파 — 외국인 이탈 가속</h4>
      <p>외국인의 한국 주식·채권 동반 이탈이 가속화될 경우 <strong>한은 긴급 외환 개입</strong> 여부가 주목됩니다. 1,560 지지 → 1,540 회복이 안정 신호.</p>
    </div>
  </div>
</div>
""", "PM STORY · W23", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W24 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell n"><div class="lbl">한국 주식</div><div class="vl">N</div></div>
    <div class="pos-cell uw"><div class="lbl">미국 기술/반도체</div><div class="vl">N→UW</div></div>
    <div class="pos-cell n"><div class="lbl">JP·TW</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">유럽 (방어)</div><div class="vl">N→OW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell n"><div class="lbl">미국 채권</div><div class="vl">N</div></div>
    <div class="pos-cell n"><div class="lbl">한국 채권</div><div class="vl">관망</div></div>
    <div class="pos-cell n"><div class="lbl">에너지</div><div class="vl">N</div></div>
    <div class="pos-cell uw"><div class="lbl">금</div><div class="vl">UW</div></div>
  </div>

  <div style="margin-top:30px;background:var(--bg-soft);border-radius:14px;padding:22px 28px;border-left:6px solid var(--blue)">
    <div style="font-size:18px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:21px;color:var(--text);line-height:1.6;font-weight:500">
      KOSPI 8,000 지지 확인 후 재진입 ·<br>유럽 방어주 N→OW · CPI 결과 후 가속
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:14px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W23", "10 / 10"))
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
