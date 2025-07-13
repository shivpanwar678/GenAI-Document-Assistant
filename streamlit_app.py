import streamlit as st
import os
from dotenv import load_dotenv
from backend import parser, splitter, embedder, qa_rag, summarizer, quiz_generator

load_dotenv()

st.set_page_config(page_title="GenAI Assistant")
st.title("📄 GenAI Document Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    text = parser.extract_text(uploaded_file)
    st.success("✅ Document uploaded and parsed")

    st.subheader("Auto Summary")
    st.write(summarizer.generate_summary(text))

    st.subheader("Ask Anything")
    chunks = splitter.split_text(text)
    db = embedder.create_vector_db(chunks)
    rag_chain = qa_rag.build_rag_chain(db)

    question = st.text_input("Type your question here")
    if question:
        answer, sources = qa_rag.ask_question(question, rag_chain)
        st.markdown(f"**Answer:** {answer}")
        with st.expander("📚 Source References"):
            for doc in sources:
                st.markdown(f"- {doc.page_content[:300]}...")

    st.subheader("🎯 Challenge Me")
    if st.button("Generate Quiz Questions"):
        quiz_questions = quiz_generator.generate_logic_questions(text)

        if quiz_questions:
            st.markdown("### 🧩 Quiz Questions")
            for idx, question in enumerate(quiz_questions, 1):
                st.markdown(f"**Q{idx}: {question}**")
                st.text_input(f"Your Answer for Q{idx}:", key=f"answer_{idx}")
