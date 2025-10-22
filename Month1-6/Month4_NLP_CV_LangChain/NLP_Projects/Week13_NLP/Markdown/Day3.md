# Day3

📘 Notebook: `03_tfidf_vectorization.ipynb`
🎯 Goal: Convert text into **numerical feature vectors** using **Bag of Words (BoW)** and **TF-IDF**.

---

## 🧠 Concept Overview

### 🔹 1. Bag of Words (BoW)

It represents text as a **collection of words**, ignoring order but counting frequency.

Example:

| Sentence           | Representation             |
| ------------------ | -------------------------- |
| “I love Python”    | {I:1, love:1, Python:1}    |
| “Python loves NLP” | {Python:1, loves:1, NLP:1} |

---

### 🔹 2. TF-IDF (Term Frequency–Inverse Document Frequency)

It improves BoW by reducing weight of common words (like “the”, “is”).

Formula:
[
\text{TF-IDF} = \text{TF}(word) \times \log\left(\frac{N}{DF(word)}\right)
]
Where:

* TF = frequency of word in document
* DF = number of documents containing word
* N = total number of documents

---

## 💻 Code Implementation (Step-by-Step)

```python
# 🧠 Week 13 - Day 3: Bag of Words & TF-IDF

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd
```

---

### 🧾 Step 1: Sample Corpus

```python
corpus = [
    "I love Natural Language Processing",
    "Language models are powerful for NLP tasks",
    "I love using Python for text processing"
]
```

---

### 🧩 Step 2: Bag of Words (BoW)

```python
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(corpus)

print("🔹 Feature Names:")
print(vectorizer.get_feature_names_out())

print("\n🔹 BoW Matrix:")
print(pd.DataFrame(X_bow.toarray(), columns=vectorizer.get_feature_names_out()))
```

🧾 **Explanation:**

* `CountVectorizer()` converts text into numeric counts.
* Each row = document, each column = word frequency.

---

### 📊 Step 3: TF-IDF Vectorization

```python
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)

print("🔹 TF-IDF Feature Names:")
print(tfidf.get_feature_names_out())

print("\n🔹 TF-IDF Matrix:")
print(pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out()).round(3))
```

🧠 **Observation:**
Common words have **lower TF-IDF scores** compared to unique, meaningful words.

---

### ⚙️ Step 4: Compare BoW vs TF-IDF

| Feature    | BoW                             | TF-IDF                           |
| ---------- | ------------------------------- | -------------------------------- |
| Simplicity | ✅ Simple counts                 | ⚙️ Weighted values               |
| Context    | ❌ Ignores importance            | ✅ Considers uniqueness           |
| Use Case   | Text classification, simple NLP | Information retrieval, ML models |

---

### 📈 Step 5: Visualize Top TF-IDF Scores

```python
import numpy as np
import matplotlib.pyplot as plt

tfidf_df = pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out())
avg_scores = tfidf_df.mean().sort_values(ascending=False).head(10)

plt.barh(avg_scores.index, avg_scores.values)
plt.title("Top 10 TF-IDF Words")
plt.xlabel("Average TF-IDF Score")
plt.gca().invert_yaxis()
plt.show()
```

---

## 🏁 Mini Task

> Create a small dataset of 5–10 text reviews (positive + negative).
>
> * Convert it to BoW and TF-IDF
> * Compare which words are most important in positive vs negative reviews

---

### 🧩 Summary Table

| Step | Concept       | Library           | Output                 |
| ---- | ------------- | ----------------- | ---------------------- |
| 1    | Create corpus | —                 | List of texts          |
| 2    | Bag of Words  | `CountVectorizer` | Word count matrix      |
| 3    | TF-IDF        | `TfidfVectorizer` | Weighted matrix        |
| 4    | Visualization | `matplotlib`      | Bar chart of top terms |

---

