# 🧠 **Day 3 — LangChain Agents & Tools**

📁 File: `03_agents.ipynb`
🎯 **Goal:** Learn how Agents use Tools like Search, Calculator, or APIs and build your first custom agent.

---

## 🧩 **1. What Are Agents?**

> Agents = LLM + Tools + Reasoning Logic

An **Agent** ek AI system hota hai jo:

* User ke input ko samajhta hai
* Decide karta hai kaunsa **tool** use karna hai
* Step-by-step reasoning karta hai (chain of thought)
* Aur phir correct output return karta hai

🧠 Example:
**User:** “What’s the square root of Pakistan’s population?”
**Agent:**

1. Use `Search` tool → finds population
2. Use `Calculator` tool → computes square root
3. Returns final result

---

## ⚙️ **2. Agent Components**

| Component     | Description               | Example                         |
| ------------- | ------------------------- | ------------------------------- |
| **LLM**       | Decision maker            | `ChatGoogleGenerativeAI`        |
| **Tools**     | Functions the LLM can use | Search, Calculator, Weather API |
| **Agent**     | LLM + Tools combo         | `initialize_agent`              |
| **AgentType** | Defines how agent thinks  | `ZERO_SHOT_REACT_DESCRIPTION`   |

---

## 🧠 **3. Workflow**

```
User Query → LLM → Chooses Tool → Executes → Returns Answer
```

---

## 🧩 **4. Example Code: Gemini Agent with Tools**

```python
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper, PythonREPL
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# 1️⃣ Initialize Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# 2️⃣ Define Tools
search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
calculator = PythonREPL()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Use for answering world or current event questions."
    ),
    Tool(
        name="Calculator",
        func=calculator.run,
        description="Use for math or logic-based calculations."
    )
]

# 3️⃣ Create the Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# 4️⃣ Ask a Question
response = agent.invoke({
    "input": "What is the square root of the current population of Pakistan?"
})
print("🤖 Agent:", response["output"])
```

---

## 🧰 **5. How It Works**

1. LLM receives question
2. Thinks: “Hmm, I need data → use Search”
3. Executes Search tool
4. Thinks: “Now need to compute → use Calculator”
5. Combines both results → gives final answer ✅

---

## 💡 **6. Best Practices**

* Keep each tool **simple** and **specific**
  ✅ One tool = One function
* Always add **clear descriptions** in your tools
* Use `verbose=True` while debugging
* Use **Google GenAI (Gemini)** or **OpenAI** as LLMs interchangeably

---

## 🧠 **Summary Tip**

> “An Agent is like an intelligent manager —
> it doesn’t do everything itself, it just knows which expert (tool) to call.”

---
