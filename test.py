import streamlit as st
import random

# ----- 전생 데이터 (많이 추가함!) -----
past_lives = [
    {"title": "고양이 집사", "desc": "당신은 전생에 고양이들의 편안한 삶을 위해 하루종일 간식과 잠자리를 챙겨주던 헌신적인 집사였습니다."},
    {"title": "피라미드 도시락 담당자", "desc": "전생에 당신은 고대 이집트에서 피라미드를 짓는 인부들에게 점심 도시락을 배달하던 중요한 역할을 맡았었습니다."},
    {"title": "조선시대 사랑꾼", "desc": "전생에 당신은 기왓집 담장을 뛰어넘어 연애 편지를 전달하던 달콤한 연애꾼이었습니다."},
    {"title": "고대 철학자", "desc": "전생에 당신은 소크라테스 옆에서 ‘밥 먹었니?’라고 묻던 소소한 철학적 질문을 던지던 현인이었습니다."},
    {"title": "판다 보호자", "desc": "전생에 당신은 대나무 숲에서 판다들이 굴러다니지 않게 지켜주는 ‘판다 보디가드’였습니다."},
    {"title": "중세 기사", "desc": "전생에 당신은 번쩍이는 갑옷 대신 이불을 두르고 싸우던 귀여운 기사였습니다."},
    {"title": "바닷속 인어", "desc": "전생에 당신은 바닷속에서 고래랑 노래를 부르던 자유로운 인어였습니다."},
    {"title": "전국 노래자랑 우승자", "desc": "전생에 당신은 매주 마을 장터에서 ‘노래자랑’ 무대를 휩쓸던 인기 가수였습니다."},
    {"title": "해적단 간식 담당", "desc": "전생에 당신은 해적선에서 보물을 지키진 못했지만, 선원들에게 최고의 쿠키를 구워주던 주방장이었습니다."},
    {"title": "빙하기 사냥꾼", "desc": "전생에 당신은 매머드를 사냥하러 나갔지만 사실은 불 피우는 데만 특화된 불 전문 사냥꾼이었습니다."},
    {"title": "산신령 조수", "desc": "전생에 당신은 깊은 산 속에서 산신령님이 주문을 외울 때 옆에서 북을 치던 조수였습니다."},
    {"title": "달나라 토끼", "desc": "전생에 당신은 달에서 떡방아를 찧던 귀여운 토끼였습니다."},
    {"title": "중세 도서관 수호자", "desc": "전생에 당신은 고서를 지키며 책장 사이에서 몰래 꿀빵을 먹던 도서관 수호자였습니다."},
    {"title": "로마 검투사", "desc": "전생에 당신은 강력한 전사였지만 사실 경기를 시작하기도 전에 관중들에게 인사만 하고 끝내버리던 검투사였습니다."},
    {"title": "미래에서 온 시간여행자", "desc": "전생이 아니라 사실 당신은 미래에서 잠깐 잘못 온 시간여행자일지도 모릅니다."},
    {"title": "바닷가 조개 수집가", "desc": "전생에 당신은 매일같이 조개를 모아 목걸이를 만들던 순수한 수집가였습니다."},
    {"title": "용사 동료 NPC", "desc": "전생에 당신은 전설의 용사 옆에서 ‘안녕하세요 여행자님’만 반복하던 NPC였습니다."},
    {"title": "왕국의 광대", "desc": "전생에 당신은 항상 웃음을 선물하며 왕과 신하들의 스트레스를 풀어주던 광대였습니다."},
    {"title": "하늘의 별", "desc": "전생에 당신은 그저 반짝이며 수많은 연인들을 이어주던 별이었습니다."},
    {"title": "마을 점쟁이", "desc": "전생에 당신은 매일 ‘내일은 좋은 일이 있을 겁니다’라는 똑같은 예언만 하던 점쟁이였습니다."}
]

# ----- 앱 설정 -----
st.set_page_config(page_title="🔮 전생 테스트", page_icon="✨", layout="centered")

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
    color: white;   /* ✨ 흰색으로 변경 ✨ */
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

# ----- 앱 제목 -----
st.markdown("<h1>✨ 나의 전생은 무엇이었을까? ✨</h1>", unsafe_allow_html=True)

# ----- 이름 입력 -----
name = st.text_input("당신의 이름을 입력하세요:", "")

if st.button("🔮 전생 확인하기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        result = random.choice(past_lives)
        st.markdown(f"<div class='result-title'>{name}님의 전생은 '{result['title']}' 이었습니다!</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-desc'>{result['desc']}</div>", unsafe_allow_html=True)
