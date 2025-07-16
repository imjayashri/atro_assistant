import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.agents import Tool, initialize_agent
from astro_tools import get_daily_horoscope

load_dotenv()

llm = OpenAI(
    temperature=0.6,
    api_key=os.getenv("OPENAI_API_KEY")
)

tools = [
    Tool(
        name="Daily Horoscope",
        func=get_daily_horoscope,
        description="Get today's horoscope for a given zodiac sign"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def ask_astrology_agent(question: str) -> str:
    return agent.run(question)