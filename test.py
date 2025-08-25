import streamlit as st
import random

# CSS 배경 + 폰트 꾸미기
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
h1 {
    color: white;   /* 흰색으로 변경 완료 ✅ */
    text-shadow: 2px 2px 8px black;
    font-size: 3em;
    text-align: center;
}
.result-title {
    color: #FF69B4;
    font-size: 2em;
    font-weight: bold;
    text-align: center;
    margin-top: 20px;
    text-shadow: 1px 1px 5px black;
}
.result-desc {
    color: white;
    font-size: 1.2em;
    text-align: center;
    margin-top: 10px;
    text-shadow: 1px 1px 4px black;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 제목
st.markdown("<h1>✨ 나의 전생은 무엇이었을까? ✨</h1>", unsafe_allow_html=True)

# 이름 입력
name = st.text_input("당신의 이름을 입력하세요:")

# 전생 데이터 (재미있게 추가)
past_lives = [
    ("이집트 파라오", "당신은 피라미드 속에서 호화롭게 살던 파라오였습니다. 하지만 덥고 모래바람이 심해 자주 짜증났습니다."),
    ("중세 기사", "용과 싸우며 백성을 지키던 기사였습니다. 하지만 사실 갑옷이 너무 무거워 자주 넘어졌습니다."),
    ("고양이", "하루 20시간을 자고, 4시간을 집사를 괴롭히던 고양이였습니다."),
    ("강아지", "주인을 보자마자 꼬리를 흔드는 충직한 강아지였습니다. 밥그릇이 비면 서운해했습니다."),
    ("왕실 요리사", "왕에게 최고의 요리를 대접했지만, 사실 본인은 라면이 제일 좋았습니다."),
    ("유명 화가", "그림으로 세상을 감동시켰지만, 생전에는 아무도 몰라줬습니다."),
    ("조선 시대 선비", "책만 읽고 글만 쓰던 선비였지만, 사실 글씨가 악필이었습니다."),
    ("궁궐의 비밀 요정", "왕이 힘들 때마다 몰래 나타나 도와주었지만, 들키면 안 돼서 항상 쭈그려 숨었습니다."),
    ("바닷속 인어", "바다에서 노래를 부르며 놀았지만, 성대결절이 와서 목이 아팠습니다."),
    ("탐험가", "새로운 땅을 발견했지만, 길치라서 자주 길을 잃었습니다."),
    ("무술 도사", "세상을 지키는 무술을 익혔지만, 사실 뱀을 무서워했습니다."),
    ("빙하기 동굴 속 원시인", "돌멩이로 불을 피우던 당신은 사실 불쓸 줄 몰라서 옆 동굴에서 빌려왔습니다."),
    ("전생의 개그맨", "당신은 전생에 사람들을 웃기던 개그맨이었지만, 농담이 너무 썰렁해서 자주 외면당했습니다."),
    ("용감한 해적", "보물을 찾으러 다녔지만, 배멀미 때문에 매일 힘들었습니다."),
    ("우주 외계인", "지구를 탐험했지만, 인간의 치킨 맛에 반해 돌아가지 못했습니다."),
    ("비밀 스파이", "세계를 구하는 스파이였지만, 암호를 자꾸 까먹었습니다."),
    ("전생의 나무늘보", "평생을 누워만 있었고, 지금의 게으른 습관이 여기서 온 듯합니다."),
    ("만두 장인", "세상에서 제일 맛있는 만두를 빚었지만, 본인은 김치찌개를 더 좋아했습니다."),
    ("유명 발명가", "놀라운 발명을 했지만, 대부분은 이미 누가 만든 거였습니다."),
    ("신화 속 용", "하늘을 날며 불을 뿜었지만, 사실 감기에 자주 걸렸습니다."),
]

# 버튼 클릭 시 결과 출력
if st.button("🔮 전생 알아보기"):
    if name:
        result = random.choice(past_lives)
        st.markdown(f"<div class='result-title'>{name}님의 전생은 바로... {result[0]}!</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-desc'>{result[1]}</div>", unsafe_allow_html=True)
    else:
        st.warning("이름을 입력해야 전생을 볼 수 있어요!")
