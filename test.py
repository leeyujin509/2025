import streamlit as st
import random

# ----- 전생 데이터 (웃긴 버전 많이 추가) -----
past_lives = [
    {"title": "고양이 집사", "desc": "전생에 당신은 고양이 간식 챙기고, 꾹꾹이 받는 걸 인생 목표로 삼던 집사였습니다."},
    {"title": "피라미드 도시락 담당자", "desc": "고대 이집트에서 피라미드 인부들에게 도시락 배달을 하던 영광스러운 자리에 있었습니다."},
    {"title": "조선시대 사랑꾼", "desc": "담장 넘어가며 연애 편지를 전해주던 전설의 연애 마스터였습니다."},
    {"title": "판다 보디가드", "desc": "판다들이 구르지 않게 지켜주던 숲속 히어로였습니다."},
    {"title": "중세 기사", "desc": "번쩍이는 갑옷 대신 이불 두르고 싸우던 귀여운 기사였습니다."},
    {"title": "노래방 리모컨 마스터", "desc": "전생에 당신은 리모컨으로 노래방 점수를 조작(?)하던 고수였습니다."},
    {"title": "치킨 배달부", "desc": "전생에 당신은 밤마다 성곽을 넘나들며 치킨을 배달하던 숨은 영웅이었습니다."},
    {"title": "양치기 알람시계", "desc": "양들에게 ‘매에에~’ 하며 아침을 알려주던 살아있는 알람시계였습니다."},
    {"title": "붕어빵 장인", "desc": "팥 넣을까 슈크림 넣을까 고민하던 최고의 고민러이자 장인이었습니다."},
    {"title": "바닷속 인어", "desc": "고래와 듀엣 공연을 하던 바닷속 뮤지션이었습니다."},
    {"title": "왕의 공식 웃음 담당", "desc": "전생에 당신은 왕이 기분 안 좋을 때마다 억지로 웃기던 궁중 개그맨이었습니다."},
    {"title": "연애 편지 배달부", "desc": "누군가의 짝사랑을 이어주던 달콤한 큐피드였습니다."},
    {"title": "비둘기 스파이", "desc": "중세 도시 위를 날아다니며 편지를 훔쳐보던 비둘기였습니다."},
    {"title": "바람잡이 관객", "desc": "전생에 당신은 장터에서 ‘와~’ 하고 환호하는 직업적 관객이었습니다."},
    {"title": "초코송이 균사", "desc": "과자와 초콜릿 사이에서 ‘내가 진짜 본체다’라고 외치던 균사였습니다."},
    {"title": "옛날 주막 술 시식 담당", "desc": "주막마다 술 맛을 체크하며 은근슬쩍 공짜로 얻어먹던 미식가였습니다."},
    {"title": "구석기 시대 불 피우기 담당", "desc": "성냥도 라이터도 없이 ‘훅훅’ 불씨를 피우던 고생쟁이였습니다."},
    {"title": "드라마 엑스트라", "desc": "전생에 당신은 고대 전쟁씬에서 항상 제일 먼저 쓰러지던 엑스트라였습니다."},
]

# ----- 페이지 기본 설정 -----
st.set_page_config(page_title="나의 전생 찾기", layout="centered")

# ----- CSS 스타일 -----
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fdfbfb, #ebedee);
        font-family: 'NanumSquareRound', sans-serif;
    }
    .title {
        font-size: 50px;
        font-weight: 900;
        color: white;
        text-align: center;
        background: linear-gradient(90deg, #f093fb, #f5576c);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        margin-bottom: 30px;
    }
    .result-title {
        font-size: 35px;
        font-weight: 800;
        color: #222;
        text-align: center;
        margin-top: 25px;
    }
    .result-desc {
        font-size: 20px;
        color: #444;
        text-align: center;
        margin-top: 10px;
        padding: 15px;
        background: #ffffffcc;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- 제목 -----
st.markdown("<div class='title'>✨ 나의 전생은 무엇이었을까? ✨</div>", unsafe_allow_html=True)

# ----- 이름 입력 -----
name = st.text_input("당신의 이름을 입력하세요:")

if st.button("전생 확인하기 🔮"):
    if name:
        result = random.choice(past_lives)
        st.markdown(f"<div class='result-title'>{name}님의 전생은 👉 {result['title']} 👈</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-desc'>{result['desc']}</div>", unsafe_allow_html=True)
    else:
        st.warning("이름을 입력해주세요!")

