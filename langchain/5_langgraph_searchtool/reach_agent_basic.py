from json import load
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent,tool
from langchain_community.tools import TavilySearchResults

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

search_tool = TavilySearchResults(search_depth = "basic")

@tool
def get_system_time():
    """Get the current system time."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


tools = [search_tool, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

result = agent.invoke("Give me a funny joke about today's weather of France?")
print("Result:", result) 