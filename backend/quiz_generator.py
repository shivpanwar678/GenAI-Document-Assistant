from transformers import pipeline

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_logic_questions(text):
    prompt = f"""
Generate 3 different logic-based questions from the following text. Only return the questions as a list. No answers.

{text[:3000]}
"""
    response = qa_pipeline(prompt, max_length=256, do_sample=False)[0]["generated_text"]

    # Split into separate questions (ensure list output)
    questions = [q.strip() for q in response.split("\n") if q.strip()]
    return questions[:3]  # return only first 3 questions
