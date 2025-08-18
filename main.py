# file: lucky_grade_predictor.py
import streamlit as st
import pandas as pd
import numpy as np
import hashlib
import random
from datetime import date

# ===================== 페이지/스타일 =====================
st.set_page_config(page_title="시험 성적 예측기 (운빨 ver.)", page_icon="🎲", layout="centered")

st.markdown("""
<style>
/* 배경 그라디언트 */
.stApp {
  background: linear-gradient(135deg, #fff2f2 0%, #f8f9ff 50%, #f2fffa 100%);
}
/* 타이틀 */
.title {
  font-size: 42px; font-weight: 800; text-align: center; margin: 0.2rem 0 0.3rem 0;
  background: -webkit-linear-gradient(45deg, #ff6b6b, #4dabf7, #51cf66);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.subtitle { text-align:center; color:#555; margin-bottom:1.2rem; }

/* 카드 */
.card {
  background: #ffffffcc; backdrop-filter: blur(4px);
  padding: 1.1rem; border-radius: 18px; box-shadow: 0 10px 24px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.05);
}
.badge {
  display:inline-block; padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight:700;
  background:#f1f3f5; color:#495057; border:1px solid #e9ecef;
}
.metric {
  display:flex; align-items:center; justify-content:space-between; gap: 12px;
  padding: 10px 12px; border-radius: 12px; border:1px dashed #e9ecef; margin-top:6px;
}
.metric span { font-weight: 700; }
.footer {
  text-align:center; color:#666; font-size:12.5px; margin-top:16px;
}
hr { border: none; border-top: 1px solid #eee; margin: 10px 0 18px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎲 시험 성적 예측기 (운빨 ver.)</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">“오늘의 럭키팩터”로 예측한 재미용 성적! (교육 포인트: 운 vs. 공부의 상대적 영향)</div>', unsafe_allow_html=True)

# ===================== 입력 영역 =====================
with st.container():
    with st.sidebar:
        st.header("⚙️ 설정")
        name = st.text_input("이름(닉네임 가능)", value="")
        today = date.today()
        day_toggle = st.checkbox("오늘 날짜 고정(재현 가능)", value=True)
        base_date = str(today) if day_toggle else st.text_input("날짜(YYYY-MM-DD)", value=str(today))
        subjects_default = ["국어", "수학", "영어", "과학", "사회"]
        subjects = st.multiselect("과목 선택", options=subjects_default + ["한국사", "탐구", "제2외국어", "정보", "음악", "미술", "체육"],
                                  default=subjects_default, max_selections=8)
        st.divider()
        st.caption("🎯 교육용 가중치 (선택)")
        study_boost = st.slider("공부 부스트(실력 가산치, 최대 +10)", 0, 10, 2)
        variability = st.slider("점수 변동성(운의 난이도)", 5, 30, 18)
        reroll = st.number_input("럭키 차밍 시드(재굴림용)", min_value=0, max_value=9999, value=0, step=1,
                                 help="숫자를 바꾸면 운빨이 살짝 달라져요!")

# ===================== 유틸 =====================
def stable_seed(*args) -> int:
    s = "|".join(map(str, args))
    h = hashlib.sha256(s.encode()).hexdigest()
    return int(h[:12], 16)

def luck_to_shift(luck_0_100: int) -> float:
    """
    luck 0~100 -> 평균 이동값(음수~양수).
    50은 0 이동. 끝으로 갈수록 점차 강해지되 과한 치팅은 방지.
    """
    centered = (luck_0_100 - 50) / 50.0  # -1 ~ 1
    return 10 * np.tanh(centered * 1.2)  # 약 -10 ~ +10 사이

def witty_comment(score: int) -> str:
    if score >= 95: return "🧠 “감독님, 전국대회는 어디로 가면 되죠?”"
    if score >= 90: return "🚀 “펜 잡는 손이 달리네요.”"
    if score >= 80: return "😎 “계획대로 되고 있어.”"
    if score >= 70: return "🙂 “오… 나쁘지 않은데?”"
    if score >= 60: return "🫠 “그래도 과락은 아니야…”"
    if score >= 40: return "🤡 “문제가 나를 퀴즈로 냈다.”"
    return "🕳️ “시험지가 나를 삼켜버림.”"

# ===================== 시드/운빨 계산 =====================
if not name or len(subjects) == 0:
    st.info("왼쪽 **설정**에서 이름과 과목을 입력해주세요!")
    st.stop()

seed = stable_seed(name.strip().lower(), base_date, reroll)
random.seed(seed)
np.random.seed(seed % (2**32 - 1))

# 럭키팩터: 개인 고유 시드 + 날짜 기반 (0~100)
lucky_factor = random.randint(0, 100)
shift = luck_to_shift(lucky_factor)

# ===================== 점수 생성 로직 =====================
# 기반 분포: 평균 60, 표준편차 = variability (클립 0~100)
base_scores = np.clip(np.random.normal(60, variability, size=len(subjects)), 0, 100)
# 운빨 이동 + 공부부스트
pred_scores = np.clip(base_scores + shift + study_boost, 0, 100).round().astype(int)

df = pd.DataFrame({
    "과목": subjects,
    "예측 점수": pred_scores
}).sort_values("예측 점수", ascending=False).reset_index(drop=True)

avg_score = int(df["예측 점수"].mean().round())
best_row = df.iloc[0]
worst_row = df.iloc[-1]

# ===================== 상단 결과 카드 =====================
colA, colB, colC = st.columns([1,1,1])
with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"<span class='badge'>이름</span><h3>{name}</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric'><span>오늘의 럭키팩터</span> {lucky_factor} / 100</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric'><span>운 이동치</span> {shift:+.1f} 점</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<span class='badge'>종합</span>", unsafe_allow_html=True)
    st.metric("예측 평균", f"{avg_score}점", delta=None)
    st.markdown(f"<div class='metric'><span>공부 부스트</span> +{study_boost} 점</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with colC:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<span class='badge'>하이라이트</span>", unsafe_allow_html=True)
    st.markdown(f"🏆 최고: **{best_row['과목']} {best_row['예측 점수']}점**", unsafe_allow_html=True)
    st.markdown(f"🪦 최저: **{worst_row['과목']} {worst_row['예측 점수']}점**", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ===================== 표 + 코멘트 =====================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 예측 점수표")
st.dataframe(df, use_container_width=True, height=260)

st.markdown("---")
st.subheader("😂 한줄 평")
for _, r in df.iterrows():
    st.write(f"- **{r['과목']} {r['예측 점수']}점** → {witty_comment(int(r['예측 점수']))}")

st.markdown('</div>', unsafe_allow_html=True)

# ===================== 차트 =====================
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📈 과목별 예측 차트")
st.bar_chart(df.set_index("과목"))
st.markdown('</div>', unsafe_allow_html=True)

# ===================== 다운로드/재굴림 =====================
csv = df.to_csv(index=False).encode("utf-8-sig")
st.download_button("⬇️ 점수표 CSV 다운로드", data=csv, file_name=f"{name}_예측점수.csv", mime="text/csv")

st.caption("🔁 운빨을 다시 굴리고 싶으면 왼쪽 **럭키 차밍 시드** 숫자를 바꿔보세요!")

# ===================== 각주(교육 포인트) =====================
st.markdown("""
<div class="footer">
<b>주의</b> · 이 사이트는 재미용 시뮬레이터입니다. 실제 성적을 예측하지 않아요.<br/>
교육 포인트: 동일한 실력(공부 부스트)에서도 운 요소(럭키팩터)에 따라 결과가 달라짐을 시각화했습니다.
</div>
""", unsafe_allow_html=True)

