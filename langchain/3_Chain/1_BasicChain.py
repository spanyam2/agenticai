from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser


load_dotenv()

model = ChatOpenAI(model = "gpt-4o")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a facts expert who knows facts about {animal}."),
        ("human", "Tell me {fact_count} facts."),
    ]
)

chain = prompt_template | model | StrOutputParser ()

result = chain.invoke({ "animal": "dog", "fact_count": 4})
print(result)
