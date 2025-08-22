import streamlit as st
import pandas as pd

st.set_page_config(page_title="체육 진로 탐색 도우미", page_icon="🏅")

st.title("🏅 체육 진로 탐색 도우미")
st.write("""
안녕하세요! 이 앱은 **체육 관련 진로**를 탐색하는 도우미예요.  
체육 분야(군인·경호 / 체육교사 / 레저스포츠)를 선택하면,  
그 안에서 직업과 관련 학과들을 확인할 수 있습니다.
""")

# 데이터 준비 (분야 기준)
data = {
    "군인·경호": {
        "군인": ["국방학과", "군사학과", "체육학과"],
        "경호원": ["경호비서학과", "체육학과"]
    },
    "체육교사": {
        "체육교사": ["체육교육과", "스포츠교육학과", "사범대 체육학과"]
    },
    "레저스포츠": {
        "레저스포츠 지도자": ["레저스포츠학과", "스포츠레저학과", "체육학과"]
    }
}

# 분야 선택
field = st.selectbox("관심 있는 체육 분야를 선택하세요", list(data.keys()))

if field:
    st.subheader(f"📌 {field} 분야 진로 탐색")
    for job, majors in data[field].items():
        st.write(f"**직업: {job}**")
        st.write("관련 학과: " + ", ".join(majors))
        st.markdown("---")
