# ✅ **Day7 — Review + Deployment (Streamlit / FastAPI / HF Spaces)**

File: `07_review.ipynb`

---

# 🎯 **Aaj ka Goal**

* Week 14 ka **full revision**
* Apna **QA RAG Chatbot** deploy karna
* Simple → Professional → Public-level deployment ka flow samajhna
* Bonus: HuggingFace Spaces hosting

---

# 🧠 **1. Review Checklist (Your Week 14 Concepts)**

### ✅ **Day 1 — LLM Basics**

* LLM prompt → output
* Basic chain = Prompt → LLM → Parser

### ✅ **Day 2 — Memory**

* ConversationBufferMemory
* Chat history injection
* Stateful chatbot

### ✅ **Day 3 — Agents & Tools**

* Agent = LLM + Tools
* ReAct logic
* Tools: Search, Calculator, custom tools

### ✅ **Day 4 — HuggingFace Intro**

* Transformers
* Pipelines
* Models tried: DistilBERT, Flan-T5

### ✅ **Day 5 — HF + LangChain**

* HuggingFace LLM inside LangChain
* Embeddings + retriever integration

### ✅ **Day 6 — QA RAG Chatbot**

* Load → Embed → Index → Retrieve → Answer
* FAISS store
* Flan-T5 / Gemini pipeline

---

# ✅ **2. Aaj kya karna hai? (Very Clean Roadmap)**

| Step | Task                              | Output        |
| ---- | --------------------------------- | ------------- |
| 1    | Revision notebook                 | Summary notes |
| 2    | Convert RAG chatbot into function | `ask(query)`  |
| 3    | Deploy via Streamlit              | Local web app |
| 4    | Deploy via FastAPI                | API endpoint  |
| 5    | Upload to HuggingFace Spaces      | Public app    |

---

# ✅ **3. Convert Chatbot into Reusable Function**

```python
def build_qa():
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    from langchain.embeddings import HuggingFaceEmbeddings
    from langchain.chains import RetrievalQA
    from langchain_community.llms import HuggingFacePipeline
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

    # Load Docs
    loader = PyPDFLoader("docs/myfile.pdf")
    docs = loader.load()

    # Embeddings
    embed = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # FAISS
    db = FAISS.from_documents(docs, embed)
    retriever = db.as_retriever()

    # LLM
    model_name = "google/flan-t5-base"
    tok = AutoTokenizer.from_pretrained(model_name)
    mod = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    pipe = pipeline("text2text-generation", model=mod, tokenizer=tok)
    llm = HuggingFacePipeline(pipeline=pipe)

    # QA chain
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa
```

Usage:

```python
qa = build_qa()
qa.invoke("Summarize page 1")["result"]
```

---

# ✅ **4. Deployment Method 1: Streamlit App**

📁 `app.py`

```python
import streamlit as st
from chatbot import build_qa

st.title("📚 RAG QA Chatbot")

qa = build_qa()

question = st.text_input("Ask something from the document:")

if st.button("Ask"):
    if question:
        ans = qa.invoke(question)["result"]
        st.write("### ✅ Answer:")
        st.write(ans)
```

Run:

```bash
streamlit run app.py
```

👉 Within 30 seconds, your chatbot is a **full UI web app**.

---

# ✅ **5. Deployment Method 2: FastAPI**

📁 `main.py`

```python
from fastapi import FastAPI
from chatbot import build_qa

app = FastAPI()
qa = build_qa()

@app.get("/ask")
async def ask(query: str):
    result = qa.invoke(query)["result"]
    return {"answer": result}
```

Run:

```bash
uvicorn main:app --reload
```

Test:

```
http://127.0.0.1:8000/ask?query=summary
```

---

# ✅ **6. Deployment Method 3: HuggingFace Spaces (Free)**

📁 Required files:

* **app.py** (Streamlit app)
* **requirements.txt**
* **docs/** folder
* **model files** (optional)

Example `requirements.txt`:

```
streamlit
sentence-transformers
faiss-cpu
transformers
langchain
langchain-community
pypdf
```

Upload → Select **Streamlit** → Run
Your chatbot becomes **public URL** ✅

---

# ✅ **7. Best Practices (Mentor-Advice Mode)**

* Bro, RAG deployments me **embeddings sabse important** hotay.
* Flan-T5 ko zyada load mat do; answers short and crisp rakho.
* FAISS ko folder me save kar sakte ho for faster loading.
* Deployment me logs on rakho → errors quickly catch hotay.
* HF Spaces = perfect free hosting for students.

---

# ✅ **8. One-Minute Summary**

* Day 7 = Revision + Deployment
* Chatbot function banao → UI (Streamlit) → API (FastAPI) → Public app (HF Spaces)
* Tumhara first **end-to-end RAG AI app** ready 🎉

---
