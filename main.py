import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MBTI 궁합 테스트",
    page_icon="💖",
    layout="centered"
)

# --- CSS 스타일 ---
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #FF6B81;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #666;
        margin-bottom: 40px;
    }
    .result-box {
        background-color: #ffeef2;
        padding: 20px;
        border-radius: 15px;
        font-size: 18px;
        color: #333;
        margin-top: 20px;
        box-shadow: 0px 4px 8px rgba(255, 105, 135, 0.2);
    }
    .reason {
        font-size: 16px;
        color: #444;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- MBTI 궁합 데이터 ---
compatibility_data = {
    ("ENFP", "INFJ"): {
        "compat": "환상의 조합 💫",
        "desc": "서로의 부족한 점을 채워주며 깊은 관계를 형성합니다.",
        "reason": "ENFP의 활발함이 INFJ의 조용한 성향을 깨우고, INFJ의 깊은 통찰이 ENFP를 안정시킵니다.",
        "img": "https://img.icons8.com/color/96/000000/love.png"
    },
    ("ENTP", "ENTJ"): {
        "compat": "에너지가 넘치는 팀 ⚡",
        "desc": "목표 지향적인 에너지가 서로를 북돋아 줍니다.",
        "reason": "ENTP의 창의력과 ENTJ의 추진력이 만나 빠르게 성과를 냅니다.",
        "img": "https://img.icons8.com/color/96/000000/rocket.png"
    },
    ("ISFJ", "ESFP"): {
        "compat": "서로를 따뜻하게 하는 관계 🌸",
        "desc": "서로의 성향을 존중하며 조화롭게 지냅니다.",
        "reason": "ISFJ의 안정감이 ESFP의 자유분방함을 포용하고, ESFP의 밝음이 ISFJ를 즐겁게 합니다.",
        "img": "https://img.icons8.com/color/96/000000/handshake.png"
    },
    ("INTP", "INTJ"): {
        "compat": "두뇌풀가동 전략가 조합 🧠",
        "desc": "깊이 있는 대화를 나누며 지적인 유대감을 형성합니다.",
        "reason": "INTP의 탐구심과 INTJ의 계획성이 결합해 완벽한 실행을 가능하게 합니다.",
        "img": "https://img.icons8.com/color/96/000000/strategy.png"
    },
    ("ISFP", "ENFJ"): {
        "compat": "따뜻한 예술가 & 리더 💐",
        "desc": "감성적이고 서로를 이해하는 관계입니다.",
        "reason": "ISFP의 감수성과 ENFJ의 배려심이 만나 깊은 공감을 이끌어냅니다.",
        "img": "https://img.icons8.com/color/96/000000/artist.png"
    },
    ("INFP", "ENFJ"): {
        "compat": "이해와 공감의 달인 🌷",
        "desc": "깊이 있는 감정 교류로 서로를 지지하는 관계입니다.",
        "reason": "INFP의 감수성과 ENFJ의 리더십이 만나 안정적인 유대감을 형성합니다.",
        "img": "https://img.icons8.com/color/96/000000/holding-hands.png"
    },
    ("INFP", "ENFP"): {
        "compat": "감성과 열정의 만남 🔥",
        "desc": "비슷한 가치관과 에너지로 함께 성장하는 관계입니다.",
        "reason": "둘 다 이상주의적이지만, ENFP가 INFP의 내향성을 부드럽게 열어줍니다.",
        "img": "https://img.icons8.com/color/96/000000/fire-heart.png"
    },
    ("INFP", "INFJ"): {
        "compat": "영혼의 대화가 가능한 관계 🌌",
        "desc": "깊은 이해와 공감으로 서로에게 위로가 됩니다.",
        "reason": "두 사람 모두 가치 중심적이며, 의미 있는 대화를 나누는 데 즐거움을 느낍니다.",
        "img": "https://img.icons8.com/color/96/000000/moon-symbol.png"
    }
}

# --- 제목 ---
st.markdown('<p class="title">💖 MBTI 궁합 테스트</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">두 사람의 MBTI를 선택하면 궁합과 이유를 알려드립니다!</p>', unsafe_allow_html=True)

# --- MBTI 선택 ---
col1, col2 = st.columns(2)

with col1:
    mbti1 = st.selectbox("👤 첫 번째 사람 MBTI", ["선택하세요"] + sorted(set([mbti for pair in compatibility_data.keys() for mbti in pair])))

with col2:
    mbti2 = st.selectbox("👤 두 번째 사람 MBTI", ["선택하세요"] + sorted(set([mbti for pair in compatibility_data.keys() for mbti in pair])))

# --- 결과 출력 ---
if mbti1 != "선택하세요" and mbti2 != "선택하세요":
    pair = (mbti1, mbti2)
    reverse_pair = (mbti2, mbti1)

    if pair in compatibility_data:
        data = compatibility_data[pair]
    elif reverse_pair in compatibility_data:
        data = compatibility_data[reverse_pair]
    else:
        data = {
            "compat": "일반적인 관계 😊",
            "desc": "서로 다른 매력을 가진 조합입니다.",
            "reason": "다양한 성향을 이해하고 존중하면 관계가 더욱 깊어질 수 있습니다.",
            "img": "https://img.icons8.com/color/96/000000/friends.png"
        }

    # 출력
    st.image(data["img"], width=80)
    st.subheader(f"{mbti1} ❤️ {mbti2} → {data['compat']}")
    st.markdown(
        f"""
        <div class="result-box">
        <strong>관계 설명:</strong> {data['desc']}<br><br>
        <strong>궁합 이유:</strong> {data['reason']}
        </div>
        """,
        unsafe_allow_html=True
    )
