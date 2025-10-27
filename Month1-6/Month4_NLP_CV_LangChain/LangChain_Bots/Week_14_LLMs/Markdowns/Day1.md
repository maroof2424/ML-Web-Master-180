

# 🧠 **LangChain Day 1 – Gemini Setup & First Chain**

### 🎯 **Goal:**

Understand how to:

* Setup LangChain with **Gemini**
* Use **PromptTemplate**
* Run your **first LLM Chain**

---

## ⚙️ **Setup Instructions**

### 1️⃣ Install required packages

```bash
pip install langchain langchain-core langchain-google-genai google-generativeai python-dotenv
```

---

### 2️⃣ Create `.env` file

Inside your project folder:

```
GOOGLE_API_KEY=your_gemini_api_key_here
```

👉 Get API key from:
[https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

### 3️⃣ Project structure

```
📦 Week_14_LLMs/
 ┣ 📜 01_intro_langchain_gemini.py
 ┗ 📜 .env
```

---

## 💻 **Code: `01_intro_langchain_gemini.py`**

```python
# =======================
# 01_intro_langchain_gemini.py
# =======================

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # or "gemini-pro"
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    "You are a helpful AI assistant. Answer clearly:\n\n{question}"
)

# Parser + Chain
parser = StrOutputParser()
chain = prompt | llm | parser

# Run the chain
response = chain.invoke({"question": "What is LangChain?"})

print("\n🤖 Response:\n", response)
```

---

## 🧾 **Expected Output**

```
🤖 Response:
LangChain is a framework that helps developers build applications using large language models...
```

---

## 💡 **Tips**

* Gemini ke `gemini-1.5-flash` model is **fast and free**, perfect for students.
* Use `.env` to keep keys safe.
* Avoid committing `.env` to GitHub.

---

## 🔥 **Next Day (Day 2 Preview)**

Learn about:

* **Memory**
* **Sequential Chains**
* Building your first **Conversational Bot**

---