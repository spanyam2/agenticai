from email import message
import dotenv
from langchain_core.messages import AIMessage, SystemMessage
#from langchain_google_firestore import FireStoreChatMessageHistory
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


PROJECT_ID = "langchainsai"
SESSION_ID = "user_session_new"  # This could be a username or a unique ID
COLLECTION_NAME = "chat_history"
# Initialize Firestore Client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)



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