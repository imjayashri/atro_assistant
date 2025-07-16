
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from astro_tools import get_daily_horoscope

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

tool = Tool(
    name="Daily Horoscope Tool",
    func=get_daily_horoscope,
    description="Gets today's horoscope for a given sun sign"
)

llm = ChatOpenAI(temperature=0.6, openai_api_key=os.getenv("OPENAI_API_KEY"))

agent = initialize_agent(
    tools=[tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def ask_astrology_agent(query):
    return agent.run(query)
