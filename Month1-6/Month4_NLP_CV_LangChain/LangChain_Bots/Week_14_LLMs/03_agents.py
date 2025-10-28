from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper
from langchain.utilities import PythonREPL
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

search = SerpAPIWrapper(serpapi_api_key=SERPAPI_API_KEY)
calculator = PythonREPL()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for when you need to answer questions about current events or the world."
    ),
    Tool(
        name="Calculator",
        func=calculator.run,
        description="Useful for math calculations."
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.invoke({"input": "What is the square root of the current population of Pakistan?"})
print("🤖 Agent:", response["output"])
