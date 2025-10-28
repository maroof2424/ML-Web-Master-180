from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# 🔹 Load API key
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 🔹 Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# 🔹 Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 🔹 Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.
Previous conversation:
{chat_history}
User Question:
{question}
""")

# 🔹 Chain that links LLM + Memory + Prompt
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

# 🔹 Example Conversation
user_inputs = [
    "Hello! Who created LangChain?",
    "Can you explain it in simple words?",
    "Give me a short example?"
]

for question in user_inputs:
    response = chain.run(question=question)
    print(f"\n🧠 User: {question}")
    print(f"🤖 Bot: {response}")
