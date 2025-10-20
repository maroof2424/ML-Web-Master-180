
# 🧠 Week 13 – NLP Basics

Welcome to **Week 13** of your Machine Learning & AI journey!  
This week, we dive into **Natural Language Processing (NLP)** — how machines understand and analyze human language.

---
### 📁 Folder Structure

```
Month4_AI_Apps/
└── Week13_NLP/
    ├── 01_text_preprocessing.ipynb
    ├── 02_tokenization.ipynb
    ├── 03_tfidf_vectorization.ipynb
    ├── 04_sentiment_model.ipynb
    ├── 05_spacy_intro.ipynb
    ├── 06_nlp_mini_project.ipynb
    ├── 07_review.ipynb
    └── README.md
```

---

## 🎯 Learning Objectives
By the end of this week, you will be able to:
- Clean and preprocess text data (tokenization, stopword removal, lemmatization)
- Convert text into numerical features using **Bag of Words** and **TF-IDF**
- Build a **sentiment classifier** using Scikit-learn
- Explore **SpaCy** and **NLTK** for NLP tasks like POS tagging and Named Entity Recognition (NER)

---

## 📅 Day-wise Plan

| Day | Topic | Notebook | Key Concepts |
|-----|--------|-----------|---------------|
| **Day 1** | Text Preprocessing | `01_text_preprocessing.ipynb` | Lowercasing, punctuation removal, stopwords, stemming, lemmatization |
| **Day 2** | Tokenization & Word Frequency | `02_tokenization.ipynb` | Tokenize text, count words, build vocabulary |
| **Day 3** | Bag of Words & TF-IDF | `03_tfidf_vectorization.ipynb` | Convert text → numeric features |
| **Day 4** | Sentiment Analysis | `04_sentiment_model.ipynb` | Build Naive Bayes / Logistic Regression sentiment model |
| **Day 5** | SpaCy Intro | `05_spacy_intro.ipynb` | POS tagging, NER, sentence parsing |
| **Day 6** | Mini Project | `06_nlp_mini_project.ipynb` | Sentiment classifier using TF-IDF |
| **Day 7** | Review | `07_review.ipynb` | Summary + Quiz |

---

## 🧩 Datasets
You can use:
- `nltk.corpus.movie_reviews`
- [Kaggle IMDb Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- `sklearn.datasets.fetch_20newsgroups`

---

## ⚙️ Requirements
```bash
pip install nltk spacy scikit-learn pandas matplotlib
python -m spacy download en_core_web_sm
````

---

## 🚀 Mini Project

**🎯 Sentiment Classifier**

* Preprocess raw text
* Convert to TF-IDF
* Train Logistic Regression model
* Evaluate using Accuracy, Precision, Recall
* Save model for deployment later

---

## 💡 Outcome

After completing Week 13:

* You’ll be confident in **text preprocessing** and **feature extraction**.
* You’ll understand **how ML models read and classify text.**
* You’ll be ready to move into **LangChain and LLM applications** (Week 14).

---

🧠 *“Language is the bridge between humans and machines — mastering NLP means mastering that bridge.”*



---


