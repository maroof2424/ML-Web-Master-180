

# 🧠 Day 2 — LangChain Chains & Memory

### 🎯 **Goal**

Learn how to:

* Build **sequential chains** (multi-step workflows)
* Use **conversation memory** so your chatbot “remembers” context

---

## 🚀 Step 1: What Are Chains?

In LangChain, a **Chain** means a **pipeline of components** —
you give an input, it passes through prompts → LLM → output parsers → memory.

**Example:**

```
User Question → Prompt → LLM → Output
```

A **Sequential Chain** = Multiple chains connected in sequence.

```
Input → Step1: Summarize → Step2: Explain → Step3: Answer
```

---

## ⚙️ Step 2: Memory in LangChain

Memory allows your LLM to **remember previous interactions**.

### 🧩 Types of Memory

| Type                             | Description                         | Use Case       |
| -------------------------------- | ----------------------------------- | -------------- |
| `ConversationBufferMemory`       | Stores last chat messages           | Short sessions |
| `ConversationSummaryMemory`      | Summarizes old chats to save memory | Long chats     |
| `ConversationBufferWindowMemory` | Keeps only the last N messages      | Medium chats   |

---

## 💡 Step 3: Setup Environment

### 🧰 Required Installs

```bash
pip install langchain
pip install langchain-google-genai
pip install google-generativeai==0.5.4
pip install python-dotenv
```

> ⚠️ Use version `google-generativeai==0.5.4` to avoid conflicts.

---

## 🔐 Step 4: Setup `.env`

Create a `.env` file in your project folder:

```bash
GOOGLE_API_KEY=your_actual_google_api_key_here
```

---

## 💻 Step 5: Example Code — Gemini + Memory

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# Initialize Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Create Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.
Conversation so far:
{chat_history}
User Question:
{question}
""")

# Output Parser
parser = StrOutputParser()

# Combine into a chain
chain = prompt | llm | parser

# Conversation flow
user_inputs = [
    "Hello! Who created LangChain?",
    "Explain it simply.",
    "Give me an example?"
]

for question in user_inputs:
    response = chain.invoke({
        "question": question,
        "chat_history": memory.load_memory_variables({})["chat_history"]
    })
    
    print(f"\n🧑 User: {question}")
    print(f"🤖 Bot: {response}")
    
    # Save in memory
    memory.save_context({"question": question}, {"answer": response})
```

---

## 🧠 Step 6: How It Works

1. `ConversationBufferMemory` stores previous chat.
2. Each new question adds to the memory.
3. The `prompt` always includes `{chat_history}` so the LLM “remembers”.
4. You can replace memory with `ConversationSummaryMemory` for long sessions.

---

## 🧩 Step 7: Bonus — Sequential Chain (Multi-Step Example)

```python
from langchain.chains import SequentialChain
from langchain_core.prompts import PromptTemplate

# Step 1: Summarize
summary_prompt = PromptTemplate.from_template("Summarize this text:\n{text}")
# Step 2: Make it simpler
explain_prompt = PromptTemplate.from_template("Explain this summary simply:\n{summary}")

chain1 = summary_prompt | llm | parser
chain2 = explain_prompt | llm | parser

seq_chain = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["text"],
    output_variables=["summary", "explanation"]
)

output = seq_chain.invoke({"text": "LangChain helps developers build LLM-powered apps using components like chains, memory, and agents."})
print(output)
```

---

## 🧩 Output Example

```
🧑 User: Hello! Who created LangChain?
🤖 Bot: LangChain was created by Harrison Chase in 2022.

🧑 User: Explain it simply.
🤖 Bot: It's a Python library that helps connect AI models together easily.
```

---

## ✅ Summary

| Concept         | Key Idea                    |
| --------------- | --------------------------- |
| Chain           | A workflow of LLM steps     |
| SequentialChain | Multiple chains in sequence |
| Memory          | Keeps conversation context  |
| BufferMemory    | Saves recent chats          |
| SummaryMemory   | Summarizes old chats        |

---

## 💬 Tip of the Day

> “Always add memory to your chatbot — bina memory ke AI bas ek calculator jaisa lagta hai 😉”

---
