import streamlit as st
from llm import db_chain

st.title("Auto insurance: Database Q&A ")

question = st.text_input("Question: ")

if question:
    chain = db_chain()
    response = chain.run(question)
    st.header("Answer")
    st.write(response)