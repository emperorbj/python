from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap,RunnableLambda,RunnableParallel
import os
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import TextLoader

load_dotenv()

embeddings = CohereEmbeddings(
    model="embed-v4.0",
    cohere_api_key="JNSFlaZw8ccLGXnxzfL4x8e0wRkDxCRpMRgfTGWv"
)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,"docs.txt")
persistent_path = os.path.join(current_dir,"chromadb")

if not os.path.exists(persistent_path):
    print("Path cannot be found")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"this {file_path} cannot be found"
        )
    
    loader = TextLoader(file_path)
    document = loader.load()