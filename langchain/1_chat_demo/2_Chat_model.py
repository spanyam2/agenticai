from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

result = llm.invoke("what is the capital of france?")
print("sample....")
print(result.content)  # Output: "The capital of France is Paris.")