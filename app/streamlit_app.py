import requests
import streamlit as st


API_URL = "http://localhost:8000/ask"

st.set_page_config(page_title="Production-Ready RAG System")

st.title("Production-Ready RAG System")
st.caption("Enterprise-style Retrieval-Augmented Generation demo")

question = st.text_input("Ask a question about the knowledge base")

if st.button("Submit") and question:
    with st.spinner("Generating answer..."):
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
        st.error("API request failed")
