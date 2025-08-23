import streamlit as st
import random

st.set_page_config(
    page_title="전생 데이트 테스트 💘",
    page_icon="💘",
    layout="wide"
)

# 스타일 적용 (배경 + 폰트 + 꾸미기)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        text-align: center;
        color: #ff4d6d;
        font-size: 60px;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px #fff;
    }
    .subtitle {
        text-align: center;
        font-size: 22px;
        color: #fff;
        margin-bottom: 50px;
    }
    .result {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
        font-size: 20px;
        text-align: center;
        margin-top: 30px;
        line-height: 1.6;
    }
    .highlight {
        font-size: 28px;
        font-weight: bold;
        color: #ff4d6d;
    }
    </style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<div class='title'>💘 전생 데이트 테스트 💘</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>우리가 전생에 어떤 관계였을까? 지금 확인해보자!</div>", unsafe_allow_html=True)

# 입력
col1, col2 = st.columns(2)

with col1:
    name1 = st.text_input("당신의 이름을 입력하세요", key="name1")
with col2:
    name2 = st.text_input("상대방 이름을 입력하세요", key="name2")

# 전생 데이터 (데이트 버전)
past_lives = [
    ("전생에 둘은 🐱 고양이 주인과 고양이였다.", "당신은 매일 밥을 챙겨주고, 상대방은 고양이답게 시크하게 무시했지만 은근 좋아했대요."),
    ("전생에 둘은 🎤 트로트 가수와 열혈 팬이었다.", "무대 위에서 노래 부를 때마다 상대방이 제일 앞에서 야광봉 흔들며 응원했어요."),
    ("전생에 둘은 🍜 라면 가게 사장과 단골손님이었다.", "상대방은 늘 '사장님! 국물 리필!'을 외쳤다고 해요."),
    ("전생에 둘은 🏯 성을 지키는 기사와 몰래 들어온 도둑이었다.", "잡히면 큰일이었지만, 사실 서로 눈빛에서 사랑이 싹텄대요."),
    ("전생에 둘은 🎨 화가와 모델이었다.", "하루 종일 그려도 질리지 않았던 특별한 인연이었죠."),
    ("전생에 둘은 🎮 오락실 격투 게임 캐릭터였다.", "서로 붙을 때마다 'KO!'를 외쳤지만 속으로는 친해지고 싶어했대요."),
    ("전생에 둘은 🍟 패스트푸드점 알바생과 손님이었다.", "상대방은 감자튀김만 주문하면서 사실 당신 보려고 갔대요."),
    ("전생에 둘은 🚌 같은 버스에서 맨날 마주치는 통학생이었다.", "눈이 마주칠 때마다 운명이라 느꼈을지도 몰라요."),
    ("전생에 둘은 🦸 슈퍼히어로와 악당이었다.", "서로 싸우면서도 왠지 모르게 끌렸던 사이였죠."),
    ("전생에 둘은 🎤 노래방 듀엣 파트너였다.", "발라드 듀엣곡은 항상 찰떡처럼 맞았대요."),
    ("전생에 둘은 📚 도서관에서 자주 마주친 책벌레였다.", "조용히 눈인사만 했지만, 이미 마음은 통하고 있었죠."),
    ("전생에 둘은 🛶 뗏목을 같이 타고 바다를 건넌 생존자였다.", "위험한 상황에서도 서로 의지하며 살아남았대요."),
    ("전생에 둘은 🎭 마을 축제에서 광대와 관객이었다.", "농담에 빵빵 터졌던 웃음이 지금까지 이어진대요."),
    ("전생에 둘은 🍦 아이스크림 가게 사장과 단골이었다.", "상대방은 늘 딸기맛만 시켰다고 하네요."),
    ("전생에 둘은 🎤 아이돌과 팬이었다.", "전생에도 '최애와 팬' 관계였으니 이번 생엔 꼭 이어지나 봐요."),
]

# 버튼 누르면 결과 표시
if st.button("전생 인연 보기 💘"):
    if name1 and name2:
        result = random.choice(past_lives)
        st.markdown(f"""
            <div class="result">
                <span class="highlight">{name1}</span> 님과 <span class="highlight">{name2}</span> 님은<br><br>
                <b>{result[0]}</b><br><br>
                {result[1]}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("두 사람의 이름을 모두 입력해주세요!")
