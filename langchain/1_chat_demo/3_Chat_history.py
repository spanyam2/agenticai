import dotenv
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model="gpt-4o")


messages = [
     SystemMessage(content = "you are an expert in social media content strategy and marketing. "),
     HumanMessage(content="what are the best practices for creating engaging posts on instagram?")
    ]

result = llm.invoke(messages)
print(result.content)