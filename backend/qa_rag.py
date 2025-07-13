from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.chains import RetrievalQA

def build_rag_chain(vectorstore):
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")
    llm = HuggingFacePipeline(pipeline=qa_pipeline)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def ask_question(question, qa_chain):
    result = qa_chain.run(question)
    return result, []
