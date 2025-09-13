import streamlit as st
from api_client import ask_backend

st.title(" Medical FAQ Assistant")
st.write("Ask me any health-related question from our knowledge base!")

user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            answer = ask_backend(user_input)
        st.success(answer)
