

# ✅ **Day5.md — HuggingFace + LangChain (LLM + Embeddings + Retrieval)**

## 🎯 **Aaj ka Goal**

Aaj hum 2 cheezein combine karenge:

1. **HuggingFace LLM** ko LangChain ke LLM wrapper me run karna
2. **Embeddings + Vector Store + Retrieval** ka full pipeline banana

Ye bilkul waise hi hoga jaise RAG systems (Retrieval-Augmented Generation) ka workflow hota hai.

---

# 🧠 **1. HuggingFace LLM ko LangChain me use kyun karte hain?**

Simple words:

**HF models free + local hotey hain. LangChain inhe powerful bana deta hai**
— tools, memory, prompts, agents, chains … sab mil jata hai.

Yani HF + LangChain =
**"Free + Smart" Combo**

---

# ⚙️ **2. Install Required Packages**

```bash
pip install langchain langchain-core langchain-community transformers sentencepiece accelerate
```

*(Note: HF models run local → no API cost.)*

---

# 🏗️ **3. HuggingFace LLM inside LangChain (Step-by-Step)**

### ✅ Step 1: Import LLM

```python
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
```

### ✅ Step 2: Load Model + Tokenizer

Example: **google/flan-t5-base** (fast + smart)

```python
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=200
)

llm = HuggingFacePipeline(pipeline=pipe)
```

### ✅ Step 3: Ask the model something

```python
print(llm("What is machine learning?"))
```

---

# 🧩 **4. Embeddings + Vector Store + Retrieval**

Real-world apps (chatbots, document Q/A, assistants) **local embeddings** use karte hain.

Hum **Sentence Transformers** embeddings use karenge.

### ✅ Step 1: Install

```bash
pip install sentence-transformers faiss-cpu
```

### ✅ Step 2: Import

```python
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
```

### ✅ Step 3: Load Embedding Model

Fast + lightweight:

```
all-MiniLM-L6-v2
```

```python
emb_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

### ✅ Step 4: Some sample documents

```python
docs = [
    "Machine learning is the study of algorithms that improve automatically.",
    "LangChain is a framework to build LLM-powered applications.",
    "HuggingFace provides thousands of models for NLP and CV."
]
```

### ✅ Step 5: Create Vector Store

```python
db = FAISS.from_texts(docs, emb_model)
```

### ✅ Step 6: Build a Retriever

```python
retriever = db.as_retriever()
```

### ✅ Step 7: Query the retriever

```python
query = "What is LangChain used for?"
results = retriever.get_relevant_documents(query)
for r in results:
    print(r.page_content)
```

---

# 🔗 **5. Combine LLM + Retrieval → RAG Pipeline**

LangChain ka **RetrievalQA** ready-made solution:

```python
from langchain.chains import RetrievalQA

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

response = qa.invoke("Explain machine learning in simple words.")
print(response["result"])
```

Ye RAG ka minimum working version hai.

---

# ✅ **Final Script — 05_hf_langchain.py**

```python
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# --- 1) LLM (HF inside LangChain)
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# --- 2) Embeddings
emb_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = [
    "Machine learning is the study of algorithms that improve automatically.",
    "LangChain is a framework to build LLM-powered applications.",
    "HuggingFace provides thousands of models for NLP and CV."
]

db = FAISS.from_texts(docs, emb_model)
retriever = db.as_retriever()

# --- 3) RAG Pipeline
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

print(qa.invoke("What is LangChain?")["result"])
```

---

# 💡 **Mentor-Style Advice**

* Bro, HF models ko LangChain me wrap karna **API cost saving hack** hai.
* FAISS + MiniLM embeddings fast hote hain — laptop ke liye best.
* RAG pipeline tumhari **future chatbot projects ka seed** hai.
* Yahan se aage tum tools, agents aur memory add kar sakte ho.

---

# 📝 **1-Minute Summary**

* HF models ko LangChain me LLM wrapper se use karte hain.
* Embeddings = text → numbers
* FAISS = in numbers ko fast find karo
* Retriever = “sabse relevant” docs return karta
* RetrievalQA = LLM + Retriever → full RAG

---
