import streamlit as st
import random

st.set_page_config(
    page_title="우리는 전생의 무슨 관계? 🔮",
    page_icon="💘",
    layout="wide"
)

# -----------------------------
# 배경 + 스타일 (전생 느낌 화려하게)
# -----------------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #3a1c71, #d76d77, #ffaf7b);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    @keyframes gradientBG {
        0% {background-position:0% 50%;}
        50% {background-position:100% 50%;}
        100% {background-position:0% 50%;}
    }
    .title {
        text-align: center;
        color: #fff7b2;
        font-size: 65px;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 3px 3px 10px #000;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #fff;
        margin-bottom: 50px;
    }
    .result {
        background: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.4);
        font-size: 22px;
        text-align: center;
        margin-top: 40px;
        line-height: 1.8;
        animation: fadeIn 2s;
    }
    .highlight {
        font-size: 30px;
        font-weight: bold;
        color: #e91e63;
    }
    .relation {
        font-size: 26px;
        font-weight: bold;
        color: #3a1c71;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 제목
# -----------------------------
st.markdown("<div class='title'>🔮 우리는 전생의 무슨 관계? 🔮</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>두 사람의 이름을 입력하면, 전생의 인연을 알려드립니다 ✨</div>", unsafe_allow_html=True)

# -----------------------------
# 입력
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    name1 = st.text_input("👉 당신의 이름", key="name1")
with col2:
    name2 = st.text_input("👉 상대방 이름", key="name2")

# -----------------------------
# 전생 관계 데이터
# -----------------------------
past_lives = [
    ("🐱 주인과 고양이", "당신은 매일 밥을 챙겨주고, 상대방은 시크하게 무시했지만 은근 좋아했답니다."),
    ("🎤 트로트 가수와 열혈 팬", "무대 위에서 노래 부를 때마다 상대방이 제일 앞에서 야광봉 흔들며 응원했어요."),
    ("🍜 라면 가게 사장과 단골손님", "상대방은 늘 '사장님! 국물 리필!'을 외쳤다고 해요."),
    ("🏯 성을 지키는 기사와 몰래 들어온 도둑", "잡히면 큰일이었지만, 사실 서로 눈빛에서 사랑이 싹텄대요."),
    ("🎨 화가와 모델", "하루 종일 그려도 질리지 않았던 특별한 인연이었죠."),
    ("🎮 오락실 격투 게임 캐릭터", "서로 붙을 때마다 'KO!'를 외쳤지만 속으로는 친해지고 싶어했대요."),
    ("🍟 패스트푸드점 알바생과 단골손님", "상대방은 감자튀김만 주문하면서 사실 당신 보려고 갔대요."),
    ("🚌 매일 같은 버스에서 마주친 통학생", "눈이 마주칠 때마다 운명이라 느꼈을지도 몰라요."),
    ("🦸 슈퍼히어로와 악당", "서로 싸우면서도 왠지 모르게 끌렸던 사이였죠."),
    ("🎤 노래방 듀엣 파트너", "발라드 듀엣곡은 항상 찰떡처럼 맞았대요."),
    ("📚 도서관 책벌레", "조용히 눈인사만 했지만, 이미 마음은 통하고 있었죠."),
    ("🛶 뗏목 생존 동료", "위험한 상황에서도 서로 의지하며 살아남았대요."),
    ("🎭 축제의 광대와 관객", "농담에 빵빵 터졌던 웃음이 지금까지 이어진대요."),
    ("🍦 아이스크림 가게 사장과 단골", "상대방은 늘 딸기맛만 시켰다고 하네요."),
    ("🌌 별자리 관측 동료", "밤하늘을 보며 서로의 미래를 점쳤대요."),
    ("⚔️ 검객과 무술 라이벌", "싸울 때마다 '다음에 또 보자!' 하며 헤어졌답니다."),
    ("🎤 아이돌과 팬", "전생에도 '최애와 팬' 관계였으니 이번 생엔 꼭 이어지나 봐요."),
]

# -----------------------------
# 결과 버튼
# -----------------------------
if st.button("🔮 전생 인연 보기"):
    if name1 and name2:
        relation = random.choice(past_lives)
        st.markdown(f"""
            <div class="result">
                <span class="highlight">{name1}</span> 님과 
                <span class="highlight">{name2}</span> 님은<br><br>
                <span class="relation">{relation[0]}</span><br><br>
                {relation[1]}
            </div>
        """, unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/2917/2917995.png", width=120)  # 전생 관련 심볼
    else:
        st.warning("두 사람의 이름을 모두 입력해주세요!")
