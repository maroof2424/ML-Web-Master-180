
# 🧠Day 1: Text Preprocessing
# -------------------------------------

# Install required packages (if not already installed)
```
!pip install nltk
```
# Import libraries
```
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
```
# Download NLTK data (only first time)
```
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

# 📄 Sample text
```
text = "Natural Language Processing (NLP) helps computers understand human language. It's awesome!"

print("🔹 Original Text:\n", text)
```

---

### Step 1️⃣: Lowercasing and Removing Punctuation

```python
# Lowercase
text_lower = text.lower()

# Remove punctuation
text_clean = "".join([ch for ch in text_lower if ch not in string.punctuation])

print("✅ Cleaned Text:\n", text_clean)
```

---

### Step 2️⃣: Tokenization

```python
tokens = word_tokenize(text_clean)
print("🧩 Tokens:\n", tokens)
```

---

### Step 3️⃣: Remove Stopwords

```python
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w not in stop_words]

print("🚫 After Stopword Removal:\n", filtered_tokens)
```

---

### Step 4️⃣: Stemming (Reduce to Root Form)

```python
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

print("🌱 After Stemming:\n", stemmed_tokens)
```

---

### Step 5️⃣: Lemmatization (Better than Stemming)

```python
lemmatizer = WordNetLemmatizer()
lemm_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

print("🧠 After Lemmatization:\n", lemm_tokens)
```

---

### 🧾 Combine Steps into a Function

```python
def preprocess_text(text):
    text = text.lower()
    text = "".join([ch for ch in text if ch not in string.punctuation])
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens

sample = "NLTK is a powerful Python library for text processing!"
print("✅ Final Output:", preprocess_text(sample))
```

---

### 📊 Output Example:

```
🔹 Original Text:
Natural Language Processing (NLP) helps computers understand human language. It's awesome!

✅ Cleaned Text:
natural language processing nlp helps computers understand human language its awesome

🧩 Tokens:
['natural', 'language', 'processing', 'nlp', 'helps', 'computers', 'understand', 'human', 'language', 'its', 'awesome']

🚫 After Stopword Removal:
['natural', 'language', 'processing', 'nlp', 'helps', 'computers', 'understand', 'human', 'language', 'awesome']

🌱 After Stemming:
['natur', 'languag', 'process', 'nlp', 'help', 'comput', 'understand', 'human', 'languag', 'awesom']

🧠 After Lemmatization:
['natural', 'language', 'processing', 'nlp', 'help', 'computer', 'understand', 'human', 'language', 'awesome']
```

---

### 💡 Summary

| Step               | Purpose           | Library             |
| ------------------ | ----------------- | ------------------- |
| Lowercasing        | Normalize text    | Python built-in     |
| Remove punctuation | Remove noise      | `string`            |
| Tokenization       | Split into words  | `nltk.tokenize`     |
| Stopword removal   | Drop common words | `nltk.stopwords`    |
| Stemming           | Crude root        | `PorterStemmer`     |
| Lemmatization      | Smart root        | `WordNetLemmatizer` |

---
