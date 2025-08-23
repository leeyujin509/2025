import streamlit as st
import random

st.set_page_config(page_title="전생 테스트", page_icon="🔮", layout="centered")

st.title("🔮 나의 전생은 무엇이었을까?")
st.write("이름을 입력하고 전생을 확인해보세요!")

# 이름 입력
name = st.text_input("이름을 입력하세요:")

# 전생 데이터 (텍스트 + 이미지 세트)
past_lives = [
    {
        "text": "전생에 당신은 고양이 카페 사장이었습니다. 손님보다 고양이를 더 챙겼죠!",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 중세 기사였는데, 사실 갑옷 대신 솜이불을 두르고 싸웠습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616430.png"
    },
    {
        "text": "전생에 당신은 감자탕집 간판이었습니다. 비바람 속에서도 꿋꿋이 버텼죠!",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 고양이였는데, 사실은 집사가 더 필요했어요.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 강아지였는데, 산책 나가는 게 너무 귀찮아서 집에만 있었어요.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 피라미드 건설 현장의 도시락 담당자였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 구름이었어요. 하지만 바람이 불면 바로 사라졌습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/414/414927.png"
    },
    {
        "text": "전생에 당신은 게임 속 NPC였습니다. 늘 같은 말만 반복했죠.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 학교 앞 떡볶이 집 주인이었습니다. 하지만 맨날 본인이 다 먹었어요.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "text": "전생에 당신은 달이었어요. 하지만 태양이 너무 강해서 자주 숨었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
]

if st.button("🔮 전생 알아보기"):
    if name.strip() == "":
        st.warning("이름을 입력해주세요!")
    else:
        result = random.choice(past_lives)  # 세트에서 랜덤 선택
        st.subheader(f"{name}님의 전생 결과는...")
        st.image(result["img"], width=150)
        st.success(result["text"])
