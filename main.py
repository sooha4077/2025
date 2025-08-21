import streamlit as st

st.set_page_config(page_title="MBTI 진로 탐색", layout="wide")

# 사이드바 메뉴
menu = st.sidebar.selectbox("메뉴 선택", ["홈", "검사", "결과", "자료실"])

if menu == "홈":
    st.title("🌟 MBTI 기반 진로 탐색 웹앱")
    st.write("당신의 성격을 기반으로 진로와 전공을 추천해 드립니다!")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)

elif menu == "검사":
    st.header("🔎 MBTI 간단 검사")
    q1 = st.radio("Q1. 새로운 사람 만나는 게 즐겁나요?", ["예", "아니오"])
    q2 = st.radio("Q2. 계획보다는 즉흥적인 걸 좋아하나요?", ["예", "아니오"])
    # ... 질문 추가

    if st.button("결과 보기"):
        st.success("당신의 MBTI는... INFP (예시)")

elif menu == "결과":
    st.header("📊 검사 결과")
    st.subheader("당신의 MBTI: INFP")
    st.write("이상주의적이고 창의적인 성향. 문학, 예술, 상담 분야에 적합합니다.")
    st.table({
        "추천 직업": ["작가", "상담사", "디자이너", "교사"],
    })

elif menu == "자료실":
    st.header("📚 MBTI별 진로 자료")
    st.write("MBTI 유형별로 추천 진로와 학과를 정리했습니다.")
