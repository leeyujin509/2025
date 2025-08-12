import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="MBTI 기반 진로 추천",
    page_icon="🎯",
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
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #4B9CD3;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #666;
        margin-bottom: 40px;
    }
    .recommendation {
        background-color: #e8f4fc;
        padding: 20px;
        border-radius: 12px;
        font-size: 18px;
        color: #333;
        margin-top: 20px;
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

# --- MBTI 데이터 ---
mbti_info = {
    "ISTJ": {
        "desc": "책임감 있고 신중하며, 체계적인 성격입니다.",
        "reason": "정확성과 규칙을 중시하므로, 조직적인 업무에 강점이 있습니다.",
        "jobs": ["회계사", "데이터 분석가", "행정 공무원"],
        "img": "https://img.icons8.com/color/96/000000/briefcase.png"
    },
    "ENFP": {
        "desc": "창의적이고 열정적이며, 사람들과의 교류를 즐깁니다.",
        "reason": "아이디어를 발산하고 새로운 시도를 하는 환경에서 강점을 발휘합니다.",
        "jobs": ["광고 기획자", "작가", "강연가"],
        "img": "https://img.icons8.com/color/96/000000/idea.png"
    },
    "INFJ": {
        "desc": "이상적이고 통찰력이 뛰어나며, 타인을 돕고 싶어 합니다.",
        "reason": "사람들의 성장과 변화를 지원하는 역할에서 큰 만족을 느낍니다.",
        "jobs": ["심리학자", "작가", "사회운동가"],
        "img": "https://img.icons8.com/color/96/000000/handshake.png"
    },
    "ENTJ": {
        "desc": "리더십이 뛰어나고, 목표를 향해 체계적으로 나아갑니다.",
        "reason": "전략적 사고와 추진력을 살려 조직을 이끄는 역할에 적합합니다.",
        "jobs": ["CEO", "전략 컨설턴트", "변호사"],
        "img": "https://img.icons8.com/color/96/000000/leader.png"
    },
    "ISFP": {
        "desc": "감각적이고 온화하며, 자유로운 환경을 선호합니다.",
        "reason": "창의성과 미적 감각을 살릴 수 있는 직업에서 두각을 나타냅니다.",
        "jobs": ["디자이너", "요리사", "예술가"],
        "img": "https://img.icons8.com/color/96/000000/art-prices.png"
    },
}

# --- 제목 ---
st.markdown('<p class="title">🎯 MBTI 기반 진로 추천</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">당신의 성격 유형에 맞는 직업과 적합 이유를 알려드립니다!</p>', unsafe_allow_html=True)

# --- MBTI 선택 ---
selected_mbti = st.selectbox(
    "📌 나의 MBTI를 선택하세요:",
    options=["선택하세요"] + list(mbti_info.keys())
)

# --- 결과 출력 ---
if selected_mbti != "선택하세요":
    info = mbti_info[selected_mbti]
    
    # 이미지
    st.image(info["img"], width=80)
    
    # 설명
    st.subheader(f"{selected_mbti} 유형")
    st.write(f"**성격 설명:** {info['desc']}")
    st.write(f"**진로 적합 이유:** {info['reason']}")
    
    # 직업 추천
    st.markdown(
        f"""
        <div class="recommendation">
        <strong>추천 직업:</strong><br>
        ✅ {info['jobs'][0]}<br>
        ✅ {info['jobs'][1]}<br>
        ✅ {info['jobs'][2]}
        </div>
        """,
        unsafe_allow_html=True
    )
