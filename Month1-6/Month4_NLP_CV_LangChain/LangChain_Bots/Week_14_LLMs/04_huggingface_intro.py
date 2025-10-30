from transformers import pipeline

sent_clf = pipeline("sentiment-analysis")
print(sent_clf("I really like learning new AI stuff!"))

summarizer = pipeline("summarization")
print(summarizer("Write a 2 line summary for this paragraph..."))

gen = pipeline("text-generation", model="gpt2")
print(gen("Machine learning is", max_length=40))

qa = pipeline("text2text-generation", model="google/flan-t5-base")
print(qa("Question: What is AI? Answer:"))