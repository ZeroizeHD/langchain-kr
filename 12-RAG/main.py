import streamlit as st

st.title("PDF 기반 GPT")
st.subheader("PDF 파일을 기준으로 무엇이든 물어보세요!")

with st.sidebar:
    button = st.button("버튼을 클릭해 주세요")

if button:
    st.write("버튼이 클릭되었습니다.")