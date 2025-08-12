import streamlit as st

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="MBTI 기반 진로 추천",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 스타일 적용 (CSS) ---
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #4B9CD3;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555;
    }
    .recommendation {
        background-color: #e8f4fc;
        padding: 20px;
        border-radius: 12px;
        font-size: 18px;
        color: #333;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- MBTI별 추천 직업 데이터 ---
mbti_jobs = {
    "ISTJ": ["회계사", "데이터 분석가", "행정 공무원"],
    "ISFJ": ["교사", "간호사", "상담사"],
    "INFJ": ["심리학자", "작가", "사회운동가"],
    "INTJ": ["전략 컨설턴트", "연구원", "기획자"],
    "ISTP": ["엔지니어", "파일럿", "경찰관"],
    "ISFP": ["디자이너", "요리사", "예술가"],
    "INFP": ["작가", "상담가", "사회복지사"],
    "INTP": ["개발자", "교수", "과학자"],
    "ESTP": ["마케팅 전문가", "기자", "기업가"],
    "ESFP": ["배우", "이벤트 플래너", "홍보 담당자"],
    "ENFP": ["광고 기획자", "작가", "강연가"],
    "ENTP": ["스타트업 창업가", "변호사", "컨설턴트"],
    "ESTJ": ["경영자", "프로젝트 매니저", "군인"],
    "ESFJ": ["교사", "간호사", "HR 담당자"],
    "ENFJ": ["코치", "홍보 전문가", "정치가"],
    "ENTJ": ["CEO", "전략 컨설턴트", "변호사"],
}

# --- 제목 ---
st.markdown('<p class="title">🎯 MBTI 기반 진로 추천</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">당신의 MBTI를 선택하면 적합한 직업을 추천해드립니다!</p>', unsafe_allow_html=True)

# --- MBTI 선택 ---
selected_mbti = st.selectbox(
    "📌 나의 MBTI를 선택하세요:",
    options=["선택하세요"] + list(mbti_jobs.keys())
)

# --- 추천 직업 출력 ---
if selected_mbti != "선택하세요":
    recommendations = mbti_jobs[selected_mbti]
    st.markdown(
        f"""
        <div class="recommendation">
        <strong>{selected_mbti}</strong> 유형의 추천 직업은:<br>
        ✅ {recommendations[0]}<br>
        ✅ {recommendations[1]}<br>
        ✅ {recommendations[2]}
        </div>
        """,
        unsafe_allow_html=True
    )

