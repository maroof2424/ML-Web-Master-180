# **Week 14**

## 🧠 **LangChain + Hugging Face Week Overview**

### 📍 **Goal:**

Learn how **LLMs**, **chains**, **agents**, and **memory** work,
then build a **LangChain-based QA Chatbot** using **OpenAI** or **Hugging Face** models.

---

| **Day**   | **Topic**                    | **Notebook**                 | **You’ll Learn / Build**                                                                                                 |
| --------- | ---------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Day 1** | LangChain setup & components | `01_intro_langchain.ipynb`   | Install `langchain`, understand `PromptTemplate`, and run your **first LLMChain** using `OpenAI` or `HuggingFaceHub`.    |
| **Day 2** | Chains and Memory            | `02_chains_memory.ipynb`     | Build **sequential chains** and **conversation memory** (e.g., `ConversationBufferMemory`, `ConversationSummaryMemory`). |
| **Day 3** | Agents & Tools               | `03_agents.ipynb`            | Learn how **agents** use tools like `Search`, `Calculator`, or APIs; create your **first custom agent**.                 |
| **Day 4** | Hugging Face intro           | `04_huggingface_intro.ipynb` | Learn **Transformers**, pipelines, and try local models (`distilbert-base-uncased`, `flan-t5-base`).                     |
| **Day 5** | Combine HF + LangChain       | `05_hf_langchain.ipynb`      | Use a **HuggingFace LLM** inside LangChain; integrate embeddings for retrieval.                                          |
| **Day 6** | QA Chatbot Project           | `06_qa_chatbot.ipynb`        | Create a **knowledge-based chatbot**: upload documents → create embeddings → query via LangChain + LLM.                  |
| **Day 7** | Review + Deployment          | `07_review.ipynb`            | Review all concepts; deploy chatbot with **Streamlit or FastAPI** + optional **HuggingFace Spaces** hosting.             |

---

## 🎯 **Final Project**

> **LangChain QA Chatbot**

* Input: `.txt` / `.pdf` knowledge base (like “AI_notes.txt”)
* Output: Chatbot answers questions contextually.
* Stack: `LangChain` + `HuggingFaceHub` + `FAISS` (vector DB) + `Streamlit`.

---

## 🧩 **Optional Enhancements**

* Add **memory** (conversation context retention).
* Try **local LLMs** with `transformers` (e.g., `Mistral`, `Flan-T5`).
* Add **speech input/output** using `gTTS` + `SpeechRecognition`.
* Deploy via **HuggingFace Spaces** or **Render**.

---