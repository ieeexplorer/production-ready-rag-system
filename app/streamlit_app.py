import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://localhost:8000/ask")

st.set_page_config(page_title="Production-Ready RAG System")

st.title("Production-Ready RAG System")
st.caption("Enterprise-style Retrieval-Augmented Generation demo")

st.sidebar.subheader("Configuration")
st.sidebar.code(API_URL)

question = st.text_input("Ask a question about the knowledge base")

example_questions = [
    "What is this system designed for?",
    "What future upgrades are planned?",
    "How does the architecture work?",
]

selected_example = st.selectbox("Example questions", [""] + example_questions)

if selected_example:
    question = selected_example

if st.button("Submit") and question:
    with st.spinner("Generating answer..."):
        try:
            response = requests.post(API_URL, json={"question": question}, timeout=30)

            if response.status_code == 200:
                data = response.json()

                if data.get("blocked"):
                    st.error(data.get("reason"))
                else:
                    st.subheader("Answer")
                    st.write(data.get("answer"))

                    st.subheader("Sources")
                    for source in data.get("sources", []):
                        st.code(source)
            else:
                st.error(f"API request failed with status code: {response.status_code}")

        except Exception as error:
            st.error(f"Connection error: {error}")
