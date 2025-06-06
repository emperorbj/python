from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

co_embedder = CohereEmbeddings(
    model="embed-v4.0",
    cohere_api_key=os.getenv("COHERE_API_KEY")
)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,"devops,.pdf")
persistent_path = os.path.join(current_dir,"new_docs")

