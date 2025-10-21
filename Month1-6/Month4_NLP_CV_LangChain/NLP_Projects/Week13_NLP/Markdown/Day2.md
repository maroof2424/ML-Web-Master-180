# 🧠 Week 13 - Day 2: Tokenization & Word Frequency

## Run in CMD 
```cmd
!pip install nltk
```
## Importing Libraries

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt

nltk.download('punkt_tab')
```

---

### 🧾 Step 1: Example Text

```python
text = """
Natural Language Processing (NLP) enables computers to understand human language.
NLP tasks include tokenization, sentiment analysis, and named entity recognition.
Python and libraries like NLTK and SpaCy make NLP easy and powerful.
"""
```

---

### ✂️ Step 2: Sentence Tokenization

Break text into **sentences**.

```python
sentences = sent_tokenize(text)
print("🔹 Sentences:\n", sentences)
print("\nTotal Sentences:", len(sentences))
```

---

### 🔡 Step 3: Word Tokenization

Split into **words**.

```python
words = word_tokenize(text)
print("🔹 First 20 Tokens:\n", words[:20])
print("\nTotal Tokens:", len(words))
```

---

### 🧹 Step 4: Clean Tokens (remove punctuation + lowercase)

```python
import string

clean_tokens = [w.lower() for w in words if w.isalpha()]
print("✅ Clean Tokens:\n", clean_tokens[:20])
```

---

### 🔢 Step 5: Word Frequency (Counting)

```python
word_freq = Counter(clean_tokens)

print("📊 Top 10 Most Common Words:")
print(word_freq.most_common(10))
```

---

### 📈 Step 6: Plot Word Frequencies

```python
top_words = dict(word_freq.most_common(10))

plt.bar(top_words.keys(), top_words.values())
plt.xticks(rotation=45)
plt.title("Top 10 Word Frequencies")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
```

---

### 🧩 Step 7: Build a Vocabulary

```python
vocab = sorted(set(clean_tokens))
print("🗂️ Vocabulary Size:", len(vocab))
print("Sample Vocabulary:", vocab[:20])
```

---

## 🧠 Summary Table

| Step | Task                  | Tool                          |
| ---- | --------------------- | ----------------------------- |
| 1    | Sentence Tokenization | `nltk.sent_tokenize`          |
| 2    | Word Tokenization     | `nltk.word_tokenize`          |
| 3    | Clean Tokens          | Remove punctuation, lowercase |
| 4    | Word Frequency        | `collections.Counter`         |
| 5    | Vocabulary            | Unique set of words           |

---

### 🏁 Mini Task

> Take any text dataset (e.g., tweets, news articles)
> Tokenize → clean → count → visualize top 10 frequent words.

---
