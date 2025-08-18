import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import requests
from io import BytesIO

# --- 페이지 설정 ---
st.set_page_config(
    page_title="AI 밈 생성기",
    page_icon="🤣",
    layout="centered"
)

# --- CSS ---
st.markdown("""
<style>
.title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#FF6347;
}
.subtitle {
    font-size:18px;
    text-align:center;
    color:#555;
}
</style>
""", unsafe_allow_html=True)

# --- 제목 ---
st.markdown('<p class="title">🤣 AI 밈 생성기</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">텍스트를 입력하면 랜덤 밈 이미지에 합성해드립니다!</p>', unsafe_allow_html=True)

# --- 밈 템플릿 (무료 이미지 URL) ---
meme_templates = [
    "https://i.imgflip.com/1bij.jpg",  # 드레이크 밈
    "https://i.imgflip.com/26am.jpg",  # 성공 아기
    "https://i.imgflip.com/1ur9b0.jpg", # 고양이 테이블 밈
    "https://i.imgflip.com/30b1gx.jpg", # 놀란 피카츄
]

# --- 사용자 입력 ---
user_text = st.text_input("👉 밈에 넣을 문장을 입력하세요:", "")

if user_text:
    # 랜덤 밈 선택
    meme_url = random.choice(meme_templates)
    response = requests.get(meme_url)
    meme_img = Image.open(BytesIO(response.content))

    # --- 텍스트 합성 ---
    draw = ImageDraw.Draw(meme_img)
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # Windows 기본 폰트
    except:
        font = ImageFont.load_default()

    # 중앙 하단에 텍스트 추가
    W, H = meme_img.size
    w, h = draw.textsize(user_text, font=font)
    position = ((W-w)/2, H-h-20)
    draw.text(position, user_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    # --- 결과 출력 ---
    st.image(meme_img, caption="✨ 생성된 밈", use_column_width=True)
