from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

# template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# prompt_template = ChatPromptTemplate.from_template(template)
# x sk-proj--9cpgxTk_Czb4dVEA


# prompt =  prompt_template.invoke({
#     "tone": "energetic", 
#     "company": "samsung", 
#     "position": "AI Engineer", 
#     "skill": "AI"
# })

# Example 2: Prompt with System and Human Messages (Using Tuples)
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]

messages = [ ("system", "you are a comedian {name} who tells jokes about {topic}"),
             ("human", "tell me {count} jokes")]
prompt_tempalte = ChatPromptTemplate.from_messages(messages)
prompt = prompt_tempalte.invoke({"name": "maniscalco", "topic": "adult", "count": 3})

result = llm.invoke(prompt)
print(result)