from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_summary(text):
    # Hugging Face models typically handle up to 1024 tokens; truncate long inputs
    text = text[:3000]
    summary = summarizer_pipeline(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']