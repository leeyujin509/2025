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
