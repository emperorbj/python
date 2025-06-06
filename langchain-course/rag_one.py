
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter



load_dotenv()
embeddings = CohereEmbeddings(
    model="embed-v4.0",
    cohere_api_key= os.getenv("COHERE_API_KEY")
)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,"docs.txt")
persistent_path = os.path.join(current_dir,"faiss_index")

if not os.path.exists(persistent_path):
    print("Path cannot be found")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"this {file_path} cannot be found"
        )
        
    document = TextLoader(file_path).load()
    
    docs = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(document)

    print("\n----Document Embedding and Indexing----")
    print(f"\nNumber of chunks of document: {len(docs)}")
    print(f"Sample chunk:\n---\n{docs[0].page_content}\n---")
    
    # dummy_text_embedding = embeddings.embed_query("test")
    # embedding_dimension = len(dummy_text_embedding)
    
    
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local(persistent_path)
else:
    print("FAISS vector db exists. No need to initialize")
    vector_store = FAISS.load_local(persistent_path, embeddings, allow_dangerous_deserialization=True)