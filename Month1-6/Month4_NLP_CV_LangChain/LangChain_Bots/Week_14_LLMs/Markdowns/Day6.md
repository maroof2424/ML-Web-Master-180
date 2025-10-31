# ✅ **Day6.md — QA Chatbot Project (Knowledge-Based RAG Chatbot)**

**File:** `06_qa_chatbot.ipynb`

---

# 🎯 **Aaj ka Goal**

Aaj hum ek **QA Chatbot** banayenge jo:

✅ User se documents lega (PDF, TXT, MD)
✅ Embeddings banayega
✅ Vector store me save karega
✅ Query ko samajh kar relevant text retrieve karega
✅ LLM se final answer generate karayega

Yani full **RAG Chatbot** (Retrieval-Augmented Generation).

Ye real-world project hai — companies exactly यही use karti hain internal docs, policies, SOPs, FAQs ke liye.

---

# 🧠 **1. RAG Chatbot Flow (Simple Urdu + Diagram Style)**

```
User Question
       ↓
Retriever (FAISS)
       ↓ relevant docs
LLM (HF / Gemini)
       ↓
Final Answer
```

Agar koi concept ya context missing ho toh **LLM hallucinate nahi karta**, balki FAISS se original lines utha kar correct answer deta.

---

# ⚙️ **2. Install Required Packages**

```bash
pip install langchain langchain-core langchain-community
pip install sentence-transformers faiss-cpu
pip install pypdf transformers accelerate
```

---

# 📂 **3. Step-by-Step Project (Very Clear Flow)**

---

# ✅ **Step 1 — Imports**

```python
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
```

---

# ✅ **Step 2 — Load Documents**

### **PDF Example**

```python
loader = PyPDFLoader("docs/myfile.pdf")
documents = loader.load()
```

### **Text Example**

```python
loader = TextLoader("docs/notes.txt")
documents = loader.load()
```

---

# ✅ **Step 3 — Embeddings Model**

Fast + accurate:

```
all-MiniLM-L6-v2
```

```python
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

---

# ✅ **Step 4 — Convert Docs → Vector Store**

```python
db = FAISS.from_documents(documents, embedding)
retriever = db.as_retriever()
```

---

# ✅ **Step 5 — LLM Setup (Flan-T5)**

```python
model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=300
)

llm = HuggingFacePipeline(pipeline=pipe)
```

---

# ✅ **Step 6 — Build QA Chain (RAG Brain)**

```python
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)
```

---

# ✅ **Step 7 — Ask Questions**

```python
query = "What is the main idea of this document?"
response = qa_chain.invoke(query)

print(response["result"])
```

---

# ✅ **Step 8 — Loop Chatbot (Optional)**

```python
while True:
    user_q = input("Ask: ")
    if user_q.lower() == "exit":
        break
    ans = qa_chain.invoke(user_q)
    print("\nBot:", ans["result"], "\n")
```

---

# 🏗️ **Full Script (06_qa_chatbot.py)**

```python
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# --- 1) Load Docs
loader = PyPDFLoader("docs/myfile.pdf")
documents = loader.load()

# --- 2) Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# --- 3) Vector Store
db = FAISS.from_documents(documents, embedding)
retriever = db.as_retriever()

# --- 4) LLM
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
llm = HuggingFacePipeline(pipeline=pipe)

# --- 5) QA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# --- 6) Ask
print(qa_chain.invoke("Summarize this document")["result"])
```

---

# 🧑‍🏫 **Mentor-Style Advice**

* Bro, yeh **Day 6 project** tumhare future RAG apps ki backbone hai.
* Ek advice:
  **LLM ko heavy mat banao — embeddings strong karo.**
* Documents zyada hue toh FAISS best hai; Chroma bhi try kar sakte ho.
* Aage Agents + Tools + Memory add karke aap **full enterprise-grade chatbot** bana sakte ho.

---

# ✅ **1-Min Summary**

* Document load karo (PDF/TXT)
* Embeddings banao
* FAISS vector store create karo
* Retriever se relevant docs lao
* LLM se final answer generate karo
* Yeh pura workflow = **RAG chatbot**

---
