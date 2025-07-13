# GenAI Assistant

An intelligent assistant that performs document-based Question Answering, Summarization, and Quiz Generation using Retrieval-Augmented Generation (RAG) and Hugging Face models — all accessible through an interactive Streamlit interface.

---

## Setup Instructions

### Prerequisites

- Python 3.10 or above
- Git installed
- Hugging Face access token (for model APIs)
- (Recommended) Virtual environment (`venv` or `conda`)

---

### Installation Steps

1. Clone the repository

   git clone https://github.com/shivpanwar678/genai-assistant.git
   cd genai-assistant

2. Create and activate virtual environment

   python -m venv venv
   venv\Scripts\activate          # On Windows

3. Install dependencies

   pip install -r requirements.txt

4. Set up environment variables

   Create a `.env` file in the root folder and add:

5. Run the Streamlit app

   streamlit run streamlit_app.py

---

## Architecture / Reasoning Flow

This system processes PDFs and allows users to query the content or generate summaries/quizzes. Here's how the flow works:

          ┌────────────┐
          │   Upload   │
          │    PDF     │
          └─────┬──────┘
                ↓
         ┌──────────────┐
         │ Text Parsing │ ← Extract raw text
         └─────┬────────┘
               ↓
       ┌──────────────────┐
       │ Text Chunking    │ ← Split into smaller chunks
       └─────┬────────────┘
             ↓
    ┌───────────────────────┐
    │ Embedding Generation  │ ← Hugging Face models
    └─────┬─────────────────┘
          ↓
    ┌───────────────────────┐
    │ FAISS Vector Database │ ← Store & search by similarity
    └─────┬─────────────────┘
          ↓
 ┌─────────────────────────────┐
 │ Question Answering          │ ← generate answers
 ├─────────────────────────────┤
 │ Summarizer / Quiz Generator │
 └─────┬───────────────────────┘
       ↓
 ┌──────────────────────────────┐
 │        Streamlit UI          │ ← Upload PDFs, ask questions, view output
 └──────────────────────────────┘

---

## Project Structure

genai-assistant/
├── backend/
│   ├── embedder.py
│   ├── parser.py
│   ├── qa_rag.py
│   ├── summarizer.py
│   ├── splitter.py
│   └── quiz_generator.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── .env              ← (Ignored by Git)

---

## Author

**Shiv Panwar**  
GitHub: https://github.com/shivpanwar678




