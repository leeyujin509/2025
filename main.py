import streamlit as st
import random

# 전생 데이터 (재밌게 20개 이상 준비)
past_lives = [
    {
        "title": "길거리 붕어빵",
        "desc": "전생에 당신은 겨울마다 사람들을 행복하게 하던 붕어빵이었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3075/3075977.png"
    },
    {
        "title": "고양이 집사",
        "desc": "전생에 당신은 12마리 고양이를 키우던 집사였습니다. 지금도 야옹이 냄새가 납니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "title": "중세 기사",
        "desc": "전생에 당신은 용맹한 기사였지만 사실은 철갑옷이 무거워서 한 번도 싸운 적이 없었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/1640/1640453.png"
    },
    {
        "title": "감자탕집 간판",
        "desc": "전생에 당신은 감자탕집의 간판이었어요. 늘 맛있는 냄새를 맡으며 살았답니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3075/3075977.png"
    },
    {
        "title": "바다의 해파리",
        "desc": "전생에 당신은 바닷속에서 둥실둥실 떠다니던 평화로운 해파리였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616490.png"
    },
    {
        "title": "피라미드 도시락 담당자",
        "desc": "전생에 당신은 고대 이집트 피라미드 건설 현장의 점심 도시락 담당이었습니다!",
        "img": "https://cdn-icons-png.flaticon.com/512/4151/4151067.png"
    },
    {
        "title": "용의 친구",
        "desc": "전생에 당신은 하늘을 나는 용과 함께 장난치던 영혼이었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/523/523442.png"
    },
    {
        "title": "분식집 떡볶이 국물",
        "desc": "전생에 당신은 분식집 떡볶이 국물이었어요. 늘 사람들을 행복하게 만들었죠.",
        "img": "https://cdn-icons-png.flaticon.com/512/3523/3523063.png"
    },
    {
        "title": "전설의 바둑돌",
        "desc": "전생에 당신은 할아버지의 바둑판 위를 전전하던 전설의 바둑돌이었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3342/3342137.png"
    },
    {
        "title": "학교 매점 음료수 자판기",
        "desc": "전생에 당신은 학생들에게 늘 인기 많던 자판기였습니다. 가끔은 고장도 냈습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"
    },
    {
        "title": "컴퓨터 마우스패드",
        "desc": "전생에 당신은 손목의 고통을 줄여주던 착한 마우스패드였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/2991/2991131.png"
    },
    {
        "title": "왕의 코끼리",
        "desc": "전생에 당신은 왕궁에서 살던 귀한 코끼리였습니다. 사실 몰래 간식도 많이 먹었죠.",
        "img": "https://cdn-icons-png.flaticon.com/512/1998/1998627.png"
    },
    {
        "title": "90년대 휴대폰",
        "desc": "전생에 당신은 벽돌만큼 무거운 휴대폰이었습니다. 통화는 잘 됐습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3208/3208755.png"
    },
    {
        "title": "구석기인 불 지피기 담당",
        "desc": "전생에 당신은 불 지피기 담당이었지만, 사실은 늘 실패해서 바위만 두드렸습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/1995/1995574.png"
    },
    {
        "title": "도서관 책갈피",
        "desc": "전생에 당신은 도서관 책 사이에 끼워져 있던 책갈피였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/2905/2905020.png"
    },
    {
        "title": "버스 종점 벤치",
        "desc": "전생에 당신은 종점에서 기사님들을 기다리던 벤치였습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/535/535188.png"
    },
    {
        "title": "천 년 묵은 거북이",
        "desc": "전생에 당신은 바다에서 천 년을 살던 거북이였습니다. 지금도 오래 사는 중!",
        "img": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "title": "동네 놀이터 미끄럼틀",
        "desc": "전생에 당신은 아이들의 웃음소리를 매일 듣던 미끄럼틀이었습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/3011/3011308.png"
    },
    {
        "title": "왕의 옥좌 쿠션",
        "desc": "전생에 당신은 왕의 엉덩이를 받쳐주던 쿠션이었습니다. 충성을 다했죠.",
        "img": "https://cdn-icons-png.flaticon.com/512/815/815508.png"
    },
    {
        "title": "외계인의 통역기",
        "desc": "전생에 당신은 외계인과 인간을 연결해주던 통역기였습니다. 하지만 종종 오역도 했습니다.",
        "img": "https://cdn-icons-png.flaticon.com/512/4277/4277461.png"
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
