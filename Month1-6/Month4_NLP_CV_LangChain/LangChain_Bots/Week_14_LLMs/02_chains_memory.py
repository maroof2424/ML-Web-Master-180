from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

# Memory
memory = ConversationBufferMemory(memory_key="chat_history")

# Prompt
prompt = ChatPromptTemplate.from_template(
    "You are a helpful AI assistant.\nPrevious conversation:\n{chat_history}\nUser Question:\n{question}"
)

# Output parser
parser = StrOutputParser()

# Chain (Prompt → Model → Parser)
chain = prompt | llm | parser

# Example conversation
user_inputs = [
    "Hello! Who created LangChain?",
    "Can you explain it in simple words?",
    "Give me a short example?"
]

for question in user_inputs:
    context = memory.load_memory_variables({})["chat_history"]
    response = chain.invoke({"question": question, "chat_history": context})
    print(f"\nUser: {question}")
    print(f"🤖 Bot: {response}")
    # Update memory
    memory.save_context({"question": question}, {"answer": response})
