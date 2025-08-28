import os
from dotenv import load_dotenv
from langchain_community.document_loaders import  CSVLoader, DirectoryLoader, UnstructuredExcelLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

## Uncomment the following files if you're not using pipenv as your virtual environment manager
#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv())

load_dotenv()
# Step 1: Load raw PDFx(s)
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH= current_dir + "/data/"

def load_csv_files(data):
    loader = DirectoryLoader(data,
                             glob='*.csv',
                             loader_cls=CSVLoader,
                             loader_kwargs= {'encoding': 'utf-8'})
    
    documents=loader.load()
    return documents
#documents=load_pdf_files(data=DATA_PATH)
documents=load_csv_files(data=DATA_PATH)
print("Length of CSV content: ", len(documents))


# Step 2: Create Chunks
def create_chunks(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,
                                                 chunk_overlap=50)
    text_chunks=text_splitter.split_documents(extracted_data)
    return text_chunks

text_chunks=create_chunks(extracted_data=documents)
print("Length of Text Chunks: ", len(text_chunks))

# Step 3: Create Vector Embeddings 

def get_embedding_model():
    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

print("prior to get Embedding model")

embedding_model=get_embedding_model()
print("after Embedding model is called")

# Step 4: Store embeddings in FAISS
DB_FAISS_PATH= "C:/langchain/8_chatbot/vectorstore/db_faiss"
print("here's the path"+ DB_FAISS_PATH)
db=FAISS.from_documents(text_chunks, embedding_model)
print("before")
try:
    db.save_local(DB_FAISS_PATH)
except:
    print("something happened here")
print("after")
