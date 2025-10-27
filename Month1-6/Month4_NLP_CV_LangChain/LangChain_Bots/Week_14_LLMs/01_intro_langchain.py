from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
    "You are a helpful AI assistant. Answer clearly:\n\n{question}"
)

parser = StrOutputParser()
chain = prompt | llm | parser

response = chain.invoke({"question": "What is LangChain?"})
print("\n🤖 Response:\n", response)

