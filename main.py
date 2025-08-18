import streamlit as st
import random

# 전생 데이터 (텍스트 + 이미지)
past_lives = [
    {
        "title": "고양이 집사",
        "desc": "전생에 당신은 길고양이들을 돌보던 따뜻한 마음의 집사였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "title": "중세 기사",
        "desc": "전생에 당신은 용맹하게 싸웠지만, 사실은 이불을 갑옷 삼아 전투에 나갔습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/1640/1640453.png"
    },
    {
        "title": "감자탕집 간판",
        "desc": "전생에 당신은 감자탕집의 간판이었어요. 늘 많은 손님을 맞이했답니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3075/3075977.png"
    },
    {
        "title": "바다의 해파리",
        "desc": "전생에 당신은 바다에서 둥둥 떠다니던 평화로운 해파리였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616490.png"
    },
    {
        "title": "피라미드 도시락 담당자",
        "desc": "전생에 당신은 고대 이집트 피라미드 건설 현장의 점심 도시락 담당이었어요!",
        "img": "https://cdn-icons-png.flaticon.com/512/4151/4151067.png"
    },
    {
        "title": "용의 친구",
        "desc": "전생에 당신은 용과 함께 하늘을 날아다니며 장난치던 자유로운 영혼이었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/523/523442.png"
    }
]

# Streamlit UI
st.set_page_config(page_title="전생 테스트", page_icon="🔮", layout="centered")

st.title("🔮 나의 전생 테스트")
st.write("이름을 입력하고 버튼을 눌러, 당신의 전생을 확인해보세요!")

name = st.text_input("이름을 입력하세요:")

if st.button("전생 알아보기 ✨"):
    if name.strip() == "":
        st.warning("이름을 입력해야 전생을 볼 수 있습니다!")
    else:
        result = random.choice(past_lives)
        st.subheader(f"✨ {name}님의 전생은... **{result['title']}** ✨")
        st.image(result["img"], width=200)
        st.write(result["desc"])
