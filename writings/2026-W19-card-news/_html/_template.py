"""
W19 Card News Generator
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
  <div class="badge-week">W19 · 2026</div>
  <div class="eyebrow">WEEKLY STORY</div>
  <div class="title-xl">KOSPI<br>사상 최초 <span class="accent">7,000 / 7,500</span></div>
  <div class="lead">
    한 주에 +13.63% 폭등, 삼성전자 1조달러·SK하이닉스 1,000조.<br>
    S&P·나스닥 6주 연속 사상 최고, 유가는 −6% 급락.
  </div>
  <div class="meta">2026-05-04 · 05-05 · 05-06 · 05-07 · 05-08</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KEY FRAME
WEEKLY.append(("02_keyframe", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">한 주 요약</div>
  <h1 class="head">코스피 +13.63% 글로벌 1위<br>유가만 −6% 역방향</h1>
  <p class="lede">5일 연휴 누적 호재 + 반도체 슈퍼사이클 + 미·이란 휴전.<br>위험자산은 사상 최고, 유가는 큰 폭 하락.</p>

  <div class="region-grid" style="margin-top:30px">
    <div class="region-card asia">
      <div class="flag">🇰🇷🇹🇼🇯🇵</div>
      <div class="rname">아시아 압도적 강세</div>
      <div class="verdict up">글로벌 1~3위 수익률</div>
      <div class="num-row"><span class="nm">KOSPI</span><span class="vl up">+13.63%</span></div>
      <div class="num-row"><span class="nm">TWSE</span><span class="vl up">+6.88%</span></div>
      <div class="num-row"><span class="nm">Nikkei</span><span class="vl up">+5.38%</span></div>
    </div>
    <div class="region-card us">
      <div class="flag">🇺🇸</div>
      <div class="rname">미국 사상 최고 6주 연속</div>
      <div class="verdict up">골디락스 구도</div>
      <div class="num-row"><span class="nm">NASDAQ</span><span class="vl up">+4.51%</span></div>
      <div class="num-row"><span class="nm">S&amp;P500</span><span class="vl up">+2.33%</span></div>
      <div class="num-row"><span class="nm">Russell2K</span><span class="vl up">+1.72%</span></div>
    </div>
    <div class="region-card europe">
      <div class="flag">🇪🇺</div>
      <div class="rname">유럽 디커플링</div>
      <div class="verdict down">관세 위협 + ECB 매파</div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl up">+0.70%</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl up">+0.43%</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">−1.26%</span></div>
    </div>
    <div class="region-card asia" style="border-left-color:var(--down)">
      <div class="flag">🛢️</div>
      <div class="rname">유가 급락 vs 금속 강세</div>
      <div class="verdict down" style="color:var(--down)">분화 — 인플레 부담 완화</div>
      <div class="num-row"><span class="nm">WTI WTD</span><span class="vl down">−6.40%</span></div>
      <div class="num-row"><span class="nm">Copper</span><span class="vl up">+4.71%</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl up">+1.49%</span></div>
    </div>
  </div>
</div>
""", "WEEKLY STORY · W19", "02 / 10"))
)

# 03 MONDAY
WEEKLY.append(("03_monday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">MONDAY · 5/4</div>
  <h1 class="day-headline">5일 연휴 호재 폭발<br>코스피 6,900 첫 돌파</h1>
  <p class="day-summary">
    5일 연휴 동안 쌓인 호재가 한꺼번에 터진 날.<br>
    코스피 <strong>+5.12%(6,936.99)</strong>로 사상 처음 6,900을 넘어섰고,<br>
    SK하이닉스 <strong>+12%</strong>로 시총 1,000조원을 첫 돌파했습니다.<br><br>
    외국인·기관 합산 <strong>5조 순매수</strong>가 랠리를 주도. 반면 유럽은<br>
    트럼프의 EU 자동차 관세 25% 위협에 STOXX50 <strong>−2.00%</strong> 급락.
  </p>
  <ul class="detail-list">
    <li>UAE OAPEC 탈퇴로 WTI +2.99%·Brent +5.80% 급등</li>
    <li>다우 −1.13%(UPS −10.47% 실적 충격)</li>
    <li>아시아 독주 · 유럽·미국과 대비 극명</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">6,936</div><div class="chg up">+5.12%</div></div>
    <div class="kpi"><div class="lbl">SK하이닉스</div><div class="val up">+12%</div><div class="chg up">시총 1,000조</div></div>
    <div class="kpi"><div class="lbl">STOXX50</div><span class="val down" style="font-size:22px">−2.00%</span><div class="chg down">관세 충격</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "03 / 10"))
)

# 04 TUESDAY
WEEKLY.append(("04_tuesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">TUESDAY · 5/5</div>
  <h1 class="day-headline">아시아 4개국 휴장<br>유럽·미국이 반등</h1>
  <p class="day-summary">
    한국·일본·중국·대만 4개국이 동시 휴장.<br>
    유럽은 전일 관세 충격에서 반등(STOXX <strong>+1.84%</strong>),<br>
    우니크레디트 1분기 순이익 <strong>32억€(21분기 연속 흑자)</strong> 호재.<br><br>
    미국은 이란 우려 완화에 유가 <strong>−3%대</strong> 급락,<br>
    나스닥과 러셀2000이 신고점을 갱신했습니다.
  </p>
  <ul class="detail-list">
    <li>아시아 공백 속에서도 위험선호 심리 살아남</li>
    <li>나스닥 신고점 갱신 — 반도체·빅테크 주도</li>
    <li>유가 급락 → 인플레 부담 완화 기대</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">STOXX50</div><div class="val up">+1.84%</div><div class="chg up">반등</div></div>
    <div class="kpi"><div class="lbl">유가(WTI)</div><div class="val down">−3%</div><div class="chg down">이란 우려 완화</div></div>
    <div class="kpi"><div class="lbl">나스닥</div><div class="val up">신고점</div><div class="chg up">갱신</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "04 / 10"))
)

# 05 WEDNESDAY
WEEKLY.append(("05_wednesday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">WEDNESDAY · 5/6</div>
  <h1 class="day-headline">코스피 사상 최초<br><span style="color:var(--orange)">7,000 시대</span> 개막</h1>
  <p class="day-summary">
    개장 직후 코스피가 7,000선을 돌파, <strong>사상 최초 7,000 시대</strong>.<br>
    장중 7,426까지 치솟으며 <strong>7,384.56(+6.45%)</strong>으로 마감.<br>
    <strong>삼성전자 +14.41%(266,000원)</strong>로 시총 1.03조달러 — 아시아 두 번째 1조달러 클럽.<br><br>
    미·이란 휴전 확인에 Brent <strong>−7.67%</strong>·WTI <strong>−7.03%</strong> 급락,<br>
    S&amp;P·나스닥도 동반 사상 최고.
  </p>
  <ul class="detail-list">
    <li>매수 사이드카 발동 — 코스피200 선물 5%+ 급등</li>
    <li>엔비디아 +5.77%·TSMC +6.36% 반도체 랠리 글로벌 확산</li>
    <li>금 +2.98%(4,703달러) — 위험·안전자산 동반 강세</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">7,384</div><div class="chg up">+6.45%</div></div>
    <div class="kpi"><div class="lbl">삼성전자</div><div class="val up">1.03조$</div><div class="chg up">1조달러 클럽</div></div>
    <div class="kpi"><div class="lbl">Brent</div><div class="val down">−7.67%</div><div class="chg down">휴전 확인</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "05 / 10"))
)

# 06 THURSDAY
WEEKLY.append(("06_thursday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">THURSDAY · 5/7</div>
  <h1 class="day-headline">닛케이 <span style="color:var(--orange)">+5.58%</span><br>골든위크 캐치업 폭등</h1>
  <p class="day-summary">
    골든위크 4거래일 연휴 후 재개장한 닛케이225가<br>
    <strong>+5.58%(62,833)</strong>로 폭등, 사상 최초 62,000 돌파.<br>
    연휴 사이 AMD +18.61% 실적 + 미국 사상 최고 + 미·이란 휴전,<br>
    3일치 호재를 단일 세션에 소화한 캐치업 랠리.<br><br>
    코스피는 건설 <strong>+6.83%</strong>·중공업 <strong>+2.67%</strong> 주도로 <strong>+1.43%(7,490)</strong>.
  </p>
  <ul class="detail-list">
    <li>주간 실업수당 청구 20만 건 — 2년 래 최저, 노동시장 견조</li>
    <li>S&amp;P −0.38%·나스닥 −0.13% — 사상 최고 후 자연스러운 숨고르기</li>
    <li>반도체 일변도 → 건설·중공업 섹터 확산 시도</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">Nikkei225</div><div class="val">62,833</div><div class="chg up">+5.58%</div></div>
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">7,490</div><div class="chg up">+1.43%</div></div>
    <div class="kpi"><div class="lbl">실업수당</div><div class="val">20만</div><div class="chg up">2년 최저</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "06 / 10"))
)

# 07 FRIDAY
WEEKLY.append(("07_friday", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="day-tag">FRIDAY · 5/8</div>
  <h1 class="day-headline">NFP 깜짝 강세<br>7,500 첫 돌파 + 6주 연속</h1>
  <p class="day-summary">
    코스피 <strong>+0.11%(7,498)</strong> 4거래일 연속 사상 최고, 장중 7,500 첫 돌파.<br>
    외국인이 <strong>5조 5,662억</strong> 역대급 매도에도<br>
    개인 +3.97조·기관 +1.55조가 정확히 흡수.<br><br>
    미국 4월 NFP <strong>+11.5만(예상 +6.2만, 거의 2배)</strong>,<br>
    S&amp;P <strong>+0.84%(7,398)</strong>·나스닥 <strong>+1.71%(26,247)</strong> 사상 최고,<br>
    주간 기준 <strong>6주 연속</strong> 상승 기록.
  </p>
  <ul class="detail-list">
    <li>현대차 +7.17% — Atlas 휴머노이드 영상 공개, 로봇 테마 부상</li>
    <li>강한 고용에도 US 10Y −2.3bp — 골디락스 재확인</li>
    <li>호르무즈 미·이란 직접 교전 보도 — 다음 주 리스크 상존</li>
  </ul>
  <div class="kpi-row">
    <div class="kpi"><div class="lbl">KOSPI</div><div class="val">7,498</div><div class="chg up">4연 사상 최고</div></div>
    <div class="kpi"><div class="lbl">NFP 4월</div><div class="val up">+115K</div><div class="chg up">예상의 2배</div></div>
    <div class="kpi"><div class="lbl">S&amp;P500</div><div class="val up">7,398</div><div class="chg up">6주 연속 ↑</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "07 / 10"))
)

# 08 INSIGHT 1 — 삼성전자 1조달러
WEEKLY.append(("08_insight_samsung", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 01 · 한국 시장</div>
  <h1 class="head">삼성 1조달러<br>SK하이닉스 1,000조</h1>
  <p class="lede">한국이 아시아 두 번째 1조달러 클럽에 진입한 구조적 배경은?</p>

  <div class="insight-box">
    <div class="qa">AI 데이터센터 + HBM 슈퍼사이클의 직접 동력</div>
    <p>
      ① <strong>5/4 SK하이닉스 +12%</strong> — 시총 1,000조 원 첫 돌파<br>
      ② <strong>5/6 삼성전자 +14.41%(266,000원)</strong> — 시총 1.03조달러,<br>
      &nbsp;&nbsp;&nbsp;&nbsp;아시아에서 TSMC에 이어 두 번째 1조달러 클럽 진입<br><br>
      AI 데이터센터 투자 확대와 HBM 수요 급증이 직접 동력.<br>
      <span class="hl">한국이 신흥국 변방이 아닌 글로벌 메가캡 보유 시장</span>으로<br>
      인식되는 구조적 변화가 진행 중입니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">삼성전자 시총</div><div class="val up">1.03조$</div><div class="chg up">아시아 2위</div></div>
    <div class="kpi"><div class="lbl">SK하이닉스</div><div class="val up">1,000조</div><div class="chg up">국내 2번째</div></div>
    <div class="kpi"><div class="lbl">KOSPI YTD</div><div class="val up">+73.98%</div><div class="chg up">글로벌 압도</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "08 / 10"))
)

# 09 INSIGHT 2 — 호르무즈 사이클
WEEKLY.append(("09_insight_hormuz", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">INSIGHT 02 · 지정학</div>
  <h1 class="head">충돌 → 휴전 → 재충돌<br>유가만 −6% 급락</h1>
  <p class="lede">미·이란이 한 주에 세 번 드라마를 썼는데 왜 유가는 오히려 내렸을까요?</p>

  <div class="insight-box" style="border-left-color:var(--down)">
    <div class="qa" style="color:var(--down)">OPEC+ 증산 기대가 지정학 프리미엄을 상쇄</div>
    <p>
      5/4 UAE OAPEC 탈퇴 → 유가 +5% 급등<br>
      5/6 미·이란 휴전 확인 → Brent <strong>−7.67%</strong>·WTI <strong>−7.03%</strong><br>
      5/8 호르무즈 직접 교전 보도 → 유가 재반등<br><br>
      결국 주간 합산 WTI <strong>−6.40%</strong>·Brent <strong>−6.36%</strong>.<br>
      OPEC+ 증산 가능성 + 글로벌 수요 둔화 우려가<br>
      <span class="hl">지정학 프리미엄을 완전히 상쇄</span>한 결과입니다.<br>
      유가 하락은 인플레 부담 완화로 이어져<br>
      오히려 위험자산 추가 상승 동력이 됐습니다.
    </p>
  </div>

  <div class="kpi-row" style="margin-top:30px">
    <div class="kpi"><div class="lbl">WTI WTD</div><div class="val down">−6.40%</div><div class="chg down">95.42달러</div></div>
    <div class="kpi"><div class="lbl">Brent WTD</div><div class="val down">−6.36%</div><div class="chg down">101.29달러</div></div>
    <div class="kpi"><div class="lbl">구리 WTD</div><div class="val up">+4.71%</div><div class="chg up">수요 기대</div></div>
  </div>
</div>
""", "WEEKLY STORY · W19", "09 / 10"))
)

# 10 CLOSING
WEEKLY.append(("10_closing", page(f"""
<div class="card closing">
  <div class="brand-bar"></div>
  <div class="eyebrow">NEXT WEEK · W20</div>
  <h2>다음 주<br>방향을 가를 <span class="accent">3대 변수</span></h2>
  <p>코스피 7,500 안착·CPI·호르무즈 — 하나라도 어긋나면<br>6주 연속 상승의 첫 조정이 올 수 있습니다.</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">코스피 외국인 매도 누적 — 7,500 안착 vs 차익실현</h4>
      <p style="color:#cfe0f3">5/8 단일 세션 5.57조 역대급 매도. 개인·기관 흡수 한계 시 KOSPI PER 28.55의 밸류 부담과 맞물려 차익실현 폭발 가능.</p>
    </div>
    <div class="risk-item" style="background:rgba(245,130,32,.08);border-left-color:var(--orange)">
      <span class="tag" style="background:var(--orange)">HIGH</span>
      <h4 style="color:#fff">미국 4월 CPI 상회 시 멀티플 압축</h4>
      <p style="color:#cfe0f3">CPI 컨센 +0.2%P 상회 → 연준 인하 기대 후퇴 + 그로스/모멘텀 멀티플 압축. 6주 연속 사상 최고의 첫 조정 트리거.</p>
    </div>
    <div class="risk-item med" style="background:rgba(212,139,7,.1);border-left-color:#e8a73a">
      <span class="tag" style="background:#e8a73a">MED</span>
      <h4 style="color:#fff">호르무즈 충돌 격화 + EU 관세 본격화</h4>
      <p style="color:#cfe0f3">5/8 직접 교전 보도로 긴장 재고조. 본격 봉쇄 시 WTI 105달러+ 재급등 → 인플레 재가속 경로 재개.</p>
    </div>
  </div>

  <div class="sign">
    <span class="left">미래에셋생명 AI Board · Weekly Story</span>
    <span>2026-05-11 발행</span>
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
  <div class="badge-week" style="background:var(--orange)">PM · W19</div>
  <div class="eyebrow">PM STORY + OUTLOOK</div>
  <div class="title-xl">포트폴리오<br><span class="accent">매니저 브리프</span></div>
  <div class="lead">
    수치·수익률 중심 의사결정 브리프<br>
    + W20 시나리오·포지셔닝 가이드
  </div>
  <div class="meta">2026-05-04 ~ 2026-05-08 · 4영업일</div>
</div>
""", "MIRAE ASSET LIFE · AI BOARD", "01 / 10"))
)

# 02 KOREA
PM.append(("02_korea", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇰🇷 한국 — 회고 W19</div>
  <h1 class="head">KOSPI 6,597 → 7,498<br>한 주에 +13.63%</h1>

  <div class="hero-num">
    <span class="nm">KOSPI 종가</span>
    <span class="vl">7,498</span>
    <span class="ch up">+13.63%</span>
  </div>

  <ul class="detail-list">
    <li><strong style="color:var(--blue)">WTD +13.63%</strong> · MTD +13.63% · YTD +73.98% — 글로벌 주요 지수 단연 1위</li>
    <li>5/6 수 <span class="up">+6.45%(7,384)</span> — 사상 첫 7,000 돌파, 삼성전자 +14.41% 1조달러 클럽, 매수 사이드카 발동</li>
    <li>5/4 월 <span class="up">+5.12%(6,936)</span> — 5일 연휴 후 재개장, SK하이닉스 +12% 시총 1,000조 첫 돌파</li>
    <li>5/8 금 <span class="up">+0.11%(7,498)</span> — 외국인 <span class="down">−5조 5,662억</span> 역대급 매도 vs 개인·기관 흡수</li>
    <li>섹터 WTD: IT <span class="up">+18.84%</span>·경기소비재 <span class="up">+10.68%</span>·건설 <span class="up">+6.76%</span> / 헬스케어 <span class="down">−2.36%</span>·커뮤니케이션 <span class="down">−1.96%</span></li>
    <li>코스닥 <span class="mono">1,207.72</span> WTD <span class="up">+1.29%</span> / USD/KRW <span class="mono">1,461.8</span> WTD <span class="down">−0.65%</span>(원화 강세)</li>
  </ul>

  <div class="kpi-row">
    <div class="kpi"><div class="lbl">PER</div><div class="val">28.55배</div><div class="chg down">단기 과열</div></div>
    <div class="kpi"><div class="lbl">PBR</div><div class="val">2.29배</div><div class="chg">프리미엄</div></div>
    <div class="kpi"><div class="lbl">외국인 5/8</div><div class="val down">−5.57조</div><div class="chg down">역대급</div></div>
  </div>
</div>
""", "PM STORY · W19", "02 / 10"))
)

# 03 USA
PM.append(("03_usa", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🇺🇸 미국 — 회고 W19</div>
  <h1 class="head">S&amp;P·나스닥 6주 연속<br>NFP 깜짝 + 골디락스</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">S&amp;P500</td><td class="vl">7,398.93</td><td class="vl up">+2.33%</td><td class="vl up">+7.88%</td></tr>
    <tr><td class="nm">NASDAQ</td><td class="vl">26,247.08</td><td class="vl up">+4.51%</td><td class="vl up">+12.96%</td></tr>
    <tr><td class="nm">Russell2K</td><td class="vl">2,861.21</td><td class="vl up">+1.72%</td><td class="vl up">+14.07%</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>일별 리듬: 화 신고점 → 수 <span class="up">+1.46%</span>(엔비디아 +5.77%·TSMC +6.36%) → 목 숨고르기 → 금 <span class="up">+0.84%</span>(NFP)</li>
    <li>섹터: SPDR Tech <span class="up">+8.43%</span>(MTD +10.04%) · ConsDiscr <span class="up">+1.32%</span> / Energy <span class="down">−5.35%</span>·Util <span class="down">−3.93%</span>·Fin <span class="down">−1.31%</span></li>
    <li>스타일: Momentum <span class="up">+5.86%</span>·Growth <span class="up">+3.98%</span>·Quality <span class="up">+1.58%</span> / Value <span class="up">+0.34%</span>·LowVol <span class="down">−0.58%</span></li>
    <li>VIX 17.19 — 사상 최고에도 변동성 낮은 수준 유지</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    4월 NFP +115K(예상 +62K 2배) + US 10Y −1.4bp<br>
    강한 고용 + 금리 하락 = 골디락스 구도 재확인
  </div>
</div>
""", "PM STORY · W19", "03 / 10"))
)

# 04 ASIA
PM.append(("04_asia", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌏 아시아 — 회고 W19</div>
  <h1 class="head">한국·대만·일본 강세<br>AI·반도체 직접 수혜</h1>

  <table class="ticker-tbl">
    <tr><th>지수</th><th style="text-align:right">종가</th><th style="text-align:right">WTD</th><th style="text-align:right">YTD</th></tr>
    <tr><td class="nm">KOSPI</td><td class="vl">7,498.00</td><td class="vl up">+13.63%</td><td class="vl up">+73.98%</td></tr>
    <tr><td class="nm">TWSE</td><td class="vl">41,603.94</td><td class="vl up">+6.88%</td><td class="vl up">+41.75%</td></tr>
    <tr><td class="nm">Nikkei225</td><td class="vl">62,713.65</td><td class="vl up">+5.38%</td><td class="vl up">+20.99%</td></tr>
    <tr><td class="nm">HSI</td><td class="vl">26,393.71</td><td class="vl up">+2.39%</td><td class="vl up">+0.21%</td></tr>
    <tr><td class="nm">Shanghai</td><td class="vl">4,179.95</td><td class="vl up">+1.65%</td><td class="vl up">+3.89%</td></tr>
    <tr><td class="nm">NIFTY50</td><td class="vl">24,176.15</td><td class="vl up">+0.74%</td><td class="vl down">−7.54%</td></tr>
  </table>

  <ul class="detail-list" style="margin-top:24px">
    <li>닛케이 5/7 <span class="up">+5.58%(62,833)</span> — 골든위크 캐치업, 사상 첫 62,000 돌파</li>
    <li>MSCI EM WTD <span class="up">+5.94%</span> — 신흥국 전체 강세</li>
    <li>USD/JPY 156.67 WTD −0.25% / USD/CNY 6.801 WTD −0.40% / 중화권 반응 미온적</li>
  </ul>
</div>
""", "PM STORY · W19", "04 / 10"))
)

# 05 MACRO + EUROPE
PM.append(("05_macro", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">🌐 매크로 · 🇪🇺 유럽 — 회고 W19</div>
  <h1 class="head">유럽 디커플링<br>관세·ECB 매파 삼중고</h1>

  <div class="region-grid">
    <div class="region-card europe">
      <div class="rname">유럽 지수 (WTD)</div>
      <div class="num-row"><span class="nm">STOXX50</span><span class="vl up">+0.51%</span></div>
      <div class="num-row"><span class="nm">DAX</span><span class="vl up">+0.70%</span></div>
      <div class="num-row"><span class="nm">CAC40</span><span class="vl up">+0.43%</span></div>
      <div class="num-row"><span class="nm">FTSE100</span><span class="vl down">−1.26%</span></div>
    </div>
    <div class="region-card us" style="border-left-color:var(--orange)">
      <div class="rname">매크로 핵심</div>
      <div class="num-row"><span class="nm">DXY</span><span class="vl down">97.9 (−0.26%)</span></div>
      <div class="num-row"><span class="nm">WTI</span><span class="vl down">95.42 (−6.40%)</span></div>
      <div class="num-row"><span class="nm">Gold</span><span class="vl up">4,730 (+1.49%)</span></div>
      <div class="num-row"><span class="nm">VIX</span><span class="vl">17.19 (+1.18%)</span></div>
    </div>
  </div>

  <ul class="detail-list" style="margin-top:24px">
    <li>5/4 트럼프 EU 자동차 관세 15→25% 위협 → STOXX50 단일일 <span class="down">−2.00%</span></li>
    <li>5/8 라가르드 매파 발언 + 슈나벨 인플레 경고 → 유럽 추가 약세</li>
    <li>5/6 수 미·이란 휴전 날 일제 반등(DAX <span class="up">+2.12%</span>·CAC <span class="up">+2.94%</span>) — 유일한 반등일</li>
    <li>EUR/USD <span class="mono">1.179</span> WTD <span class="up">+0.60%</span> / GBP/USD <span class="mono">1.363</span> WTD <span class="up">+0.37%</span></li>
  </ul>
</div>
""", "PM STORY · W19", "05 / 10"))
)

# 06 BONDS
PM.append(("06_bonds", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">💵 채권 — 회고 W19</div>
  <h1 class="head">강한 NFP에도 금리 하락<br>골디락스의 정수</h1>

  <div class="kpi-row" style="margin-top:0;margin-bottom:24px">
    <div class="kpi"><div class="lbl">US 10Y</div><div class="val">4.364%</div><div class="chg down">−1.4bp WTD</div></div>
    <div class="kpi"><div class="lbl">US 2Y</div><div class="val">3.893%</div><div class="chg up">+0.5bp WTD</div></div>
    <div class="kpi"><div class="lbl">10-2 스프레드</div><div class="val">+47.1bp</div><div class="chg">정상 스팁</div></div>
  </div>

  <div class="kpi-row" style="margin-bottom:24px">
    <div class="kpi"><div class="lbl">KR 10Y</div><div class="val">3.748%</div><div class="chg down">−3.2bp WTD</div></div>
    <div class="kpi"><div class="lbl">KR 3Y</div><div class="val">3.569%</div><div class="chg down">−2.6bp WTD</div></div>
    <div class="kpi"><div class="lbl">US 30Y</div><div class="val">4.947%</div><div class="chg down">−1.0bp WTD</div></div>
  </div>

  <ul class="detail-list">
    <li>크레딧 WTD: HYG <span class="up">+0.10%</span>·LQD <span class="up">+0.55%</span>·EMB <span class="up">+0.61%</span>·TLT <span class="up">+0.55%</span> — 전 구간 강세</li>
    <li>Copper <span class="up">+4.71%</span>·Silver <span class="up">+5.41%</span> — 산업금속 강세, 제조업 수요 기대</li>
    <li>KR-US 10Y 스프레드 추가 축소 — 한국 금리 매력도 상승</li>
  </ul>

  <div class="big-quote" style="margin-top:14px">
    NFP +115K 깜짝 강세에도 US 10Y −1.4bp.<br>
    위험·안전자산이 동시에 이긴 이상적 구도.
  </div>
</div>
""", "PM STORY · W19", "06 / 10"))
)

# 07 SCENARIOS
PM.append(("07_scenarios", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W20 OUTLOOK</div>
  <h1 class="head">시나리오 3가지<br>5/11 ~ 5/15</h1>
  <p class="lede">CPI · 코스피 7,500 안착 · 호르무즈가 결정합니다</p>

  <div class="scen-grid" style="margin-top:24px">
    <div class="scen bull">
      <div class="stag">🟢 BULL</div>
      <h4>CPI 하회 + 호르무즈 완화</h4>
      <div class="pp">확률: 낮음~중간</div>
      <p>CPI 컨센 하회, 호르무즈 외교 진전, 코스피 7,500 안착. 코스피 7,700 도전, S&amp;P 7,500, 나스닥 27,000. USD/KRW 1,440, WTI 90달러, US 10Y 4.20% 시도.</p>
    </div>
    <div class="scen base">
      <div class="stag">⚪ BASE (유력)</div>
      <h4>CPI 컨센 부근 + 박스권</h4>
      <div class="pp">확률: 유력</div>
      <p>CPI 컨센, 호르무즈 박스권, 코스피 7,400~7,550 안착. S&amp;P 7,350~7,450·나스닥 26,000~26,500 횡보. USD/KRW 1,455~1,475, WTI 92~98달러, US 10Y 4.30~4.40%.</p>
    </div>
    <div class="scen bear">
      <div class="stag">🔴 BEAR</div>
      <h4>CPI 상회 + 외국인 차익실현</h4>
      <div class="pp">확률: 중간</div>
      <p>CPI +0.2%P 상회 + 임금 가속 + 호르무즈 봉쇄. 코스피 7,200 후퇴, S&amp;P 7,200·나스닥 25,500 조정. USD/KRW 1,490, WTI 105달러+, US 10Y 4.50%, VIX 22+.</p>
    </div>
  </div>
</div>
""", "PM STORY · W19", "07 / 10"))
)

# 08 WATCH POINTS
PM.append(("08_watch", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">W20 WATCH POINTS</div>
  <h1 class="head">놓치면 안 될 이벤트</h1>

  <div class="watch-grid" style="margin-top:18px">
    <div class="watch">
      <h4><span class="em">🇰🇷</span>한국</h4>
      <ul>
        <li>KR 4월 수출 잠정치</li>
        <li>외국인 5/9 이후 매도 지속 여부</li>
        <li><strong>7,500 안착 vs 차익실현 분기점</strong></li>
        <li>USD/KRW 1,460 지지 / 1,480 돌파 여부</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌐</span>매크로</h4>
      <ul>
        <li><strong>미국 4월 CPI/PPI (주중반)</strong></li>
        <li>미시간 소비자 심리 (주말)</li>
        <li>연준 위원 발언</li>
        <li>호르무즈 긴장 추이 / OPEC+ 증산 시그널</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🌏</span>아시아 및 중국</h4>
      <ul>
        <li>중국 4월 CPI/PPI (주초)</li>
        <li>일본 1Q GDP 잠정치</li>
        <li>대만 4월 수출</li>
        <li>닛케이 62,000 안착 / 항셍 26,000 지지</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇺🇸</span>미국 실적</h4>
      <ul>
        <li>CPI/PPI 발표 — 주 최대 이벤트</li>
        <li>1Q 어닝 시즌 마지막 주(소매·기술)</li>
        <li>S&amp;P500 7,400 안착 / VIX 17~19</li>
        <li>SPDR Tech 175 라인 / 모멘텀 지속</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">🇪🇺</span>유럽</h4>
      <ul>
        <li>유로존 1Q GDP 잠정치</li>
        <li>독일 ZEW 경제심리</li>
        <li>ECB 위원 발언 — 인하 사이클 종료?</li>
        <li>DAX 24,000 지지 / EUR/USD 1.18 부근</li>
      </ul>
    </div>
    <div class="watch">
      <h4><span class="em">💵</span>채권</h4>
      <ul>
        <li>미국 4월 CPI/PPI</li>
        <li>30Y 국채 입찰</li>
        <li>US 10Y 4.30% 지지 / 4.45% 저항</li>
        <li>KR 10Y 3.70% 안정 여부</li>
      </ul>
    </div>
  </div>
</div>
""", "PM STORY · W19", "08 / 10"))
)

# 09 RISKS
PM.append(("09_risks", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">⚠ W20 통합 리스크</div>
  <h1 class="head">3가지 핵심 리스크</h1>
  <p class="lede">우선순위 — HIGH 2 / MED 1</p>

  <div class="risk-list" style="margin-top:18px">
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>코스피 외국인 매도 누적 → 차익실현</h4>
      <p>W19 누적 외국인 매도 + 5/8 단일 세션 5.57조. 개인·기관 흡수 한계 시 차익실현 폭발. <strong>7,500 하방 이탈이 트리거</strong>. KOSPI PER 28.55 밸류에이션 부담 가세.</p>
    </div>
    <div class="risk-item">
      <span class="tag">HIGH</span>
      <h4>미국 4월 CPI 상회 → 멀티플 압축</h4>
      <p>CPI 컨센 +0.2%P 상회 시 연준 인하 기대 후퇴 + 그로스/모멘텀 멀티플 압축 동시 발생. <strong>6주 연속 주간 상승의 사상 최고권에서 첫 조정 트리거</strong>.</p>
    </div>
    <div class="risk-item med">
      <span class="tag">MED</span>
      <h4>호르무즈 미·이란 충돌 격화</h4>
      <p>W19 충돌·휴전·재충돌 사이클 반복, 5/8 직접 교전 보도. 봉쇄 시나리오 현실화 → <strong>W19 −6%대 하락 유가 빠른 되돌림</strong> → 인플레 재가속 → 위험자산 조정.</p>
    </div>
  </div>
</div>
""", "PM STORY · W19", "09 / 10"))
)

# 10 POSITIONING
PM.append(("10_positioning", page(f"""
<div class="card">
  <div class="brand-bar"></div>
  <div class="kicker">📊 W20 BASE 시나리오 포지셔닝</div>
  <h1 class="head">포지셔닝 시사점</h1>
  <p class="lede">방향성 참고용 · OW 비중확대 / N 중립 / UW 비중축소</p>

  <div class="pos-grid" style="margin-top:24px">
    <div class="pos-cell n"><div class="lbl">🇰🇷 한국</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">🇺🇸 미국 테크</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">🇯🇵🇹🇼 일본·대만</div><div class="vl">OW</div></div>
    <div class="pos-cell uw"><div class="lbl">🇪🇺 유럽</div><div class="vl">UW</div></div>
  </div>
  <div class="pos-grid" style="margin-top:16px">
    <div class="pos-cell n"><div class="lbl">🇨🇳 중국</div><div class="vl">N</div></div>
    <div class="pos-cell ow"><div class="lbl">💵 채권 듀레이션</div><div class="vl">OW</div></div>
    <div class="pos-cell ow"><div class="lbl">🥇 금 / 산업금속</div><div class="vl">OW</div></div>
    <div class="pos-cell n"><div class="lbl">🛢️ 원유</div><div class="vl">N</div></div>
  </div>

  <div style="margin-top:32px;background:var(--bg-soft);border-radius:14px;padding:22px 26px;border-left:6px solid var(--blue)">
    <div style="font-size:16px;color:var(--blue);font-weight:700;letter-spacing:2px;margin-bottom:8px">핵심 메시지</div>
    <div style="font-size:20px;color:var(--text);line-height:1.6;font-weight:500">
      한국 N(관망) — 7,500 안착·외국인 매도 확인 후 판단<br>
      미국 테크·일본·대만 OW · 유럽 UW · 채권 OW 유지
    </div>
  </div>

  <div style="position:absolute;left:72px;right:72px;bottom:90px;font-size:13px;color:var(--muted);line-height:1.5">
    ※ 본 자료는 시장 데이터 기반 방향성 참고용이며, 매수·매도 직접 권유가 아닙니다.<br>
    개별 상품 운용은 각 상품 운용 정책 및 리스크 가이드라인을 따릅니다.
  </div>
</div>
""", "PM STORY · W19", "10 / 10"))
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
