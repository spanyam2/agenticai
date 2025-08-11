from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.runnables import RunnableLambda

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

animal_facts_template = ChatPromptTemplate.from_messages(
		[
		("system", "You are a facts expert who knows facts about {animal}."),
		("human", "Tell me {fact_count} facts."),
	]
)

translation_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator and convert the provided text into {language}."),
        ("human", "Translate the following text to {language}: {text}"),
    ]
)


chain = animal_facts_template | model | StrOutputParser()

result = chain.invoke({"animal": "dog", "fact_count": 4})

print(result)

chain2 = translation_template | model | StrOutputParser()
result2 = chain2.invoke({"language": "French", "text": result})
print(result2)
# Define a prompt template for translation to French

