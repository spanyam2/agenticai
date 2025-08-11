from email import message
import dotenv
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(model="gpt-4o")

chat_history = []

system_message = SystemMessage("You are a helpful AI assistant")

chat_history.append(system_message)

while True:
    user_input = input("You: ")

    if (user_input.lower() == "exit"):
        print("Exiting the chat. bye!")
        break

    chat_history.append(HumanMessage(content = user_input))

    result = llm.invoke(chat_history)
    response =  result.content
    print("AI: " + response)
    chat_history.append(AIMessage(content=response))
   # print("new chat history: " + )
print("Chat history:" + str(chat_history))