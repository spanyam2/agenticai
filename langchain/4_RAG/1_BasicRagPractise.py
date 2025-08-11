from pyexpat import model
from xml.dom.minidom import Document
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma  import Chroma
from langchain_community.document_loaders import TextLoader 
from langchain_openai import OpenAIEmbeddings
import os



load_dotenv()
model = OpenAI(model="gpt-4o")

# Define the directory containing the text file and the persistent directory
os.curdir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(os.curdir, "documents", "lord_of_the_rings.txt")
persistent_directory = os.path.join(os.curdir, "db", "chroma_db")
# Check if the Chroma vector store already exists

if not os.path.exists(persistent_directory):
    #Read the text contents from the file
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50) 
    docs = text_splitter.split_documents(documents)

    print("")
else:
    print("vectors store already exists, no need to initialize db")


