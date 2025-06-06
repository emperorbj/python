from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
from langchain_core.prompts import ChatPromptTemplate 
from langchain_cohere import CohereEmbeddings
from langchain_community.document_loaders import PyPDFium2Loader
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain # For combining docs
from langchain.chains import create_retrieval_chain # For the full RAG chain
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

co_embedder = CohereEmbeddings(
    model="embed-v4.0",
    cohere_api_key=os.getenv("COHERE_API_KEY")
)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir,"devops.pdf")
persistent_path = os.path.join(current_dir,"new_docs")

if not os.path.exists(persistent_path):
    print(f"""this file path {persistent_path} does not exist""")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"this directory {file_path} cannot be found")
    
    document = PyPDFium2Loader(file_path).load()
    docs = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 0).split_documents(document)
    
    print("\n ----------Loading and Splitting Characters----------")
    print(f"Docs Chunk Number {len(docs)}")
    print(f"Document content:\n {docs[0].page_content}")
    
    vector_store = FAISS.from_documents(docs,co_embedder)
    vector_store.save_local(persistent_path)
    
else:
    print('The vector DB embedding has been created')
    vector_store = FAISS.load_local(persistent_path,co_embedder, allow_dangerous_deserialization=True)
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)
    
    print("initializing GenAi....")
    
    retriever = vector_store.as_retriever(search_kwargs={"k":3})
    
    prompt = ChatPromptTemplate.from_template("""
    You are an AI assistant tasked with answering questions based on the provided context.
    Carefully read the context and use only the information within it to answer the question.
    If the answer cannot be found in the context, state that clearly and do not make up information.
    <context>
    {context}
    </context>

    Question: {input}
    """)
    
    document_chain = create_stuff_documents_chain(llm,prompt)
    rag_chain = create_retrieval_chain(retriever,document_chain)
    
    print("initializing rag chain....")
    
    while True:
        query = input("Ask anything(or type exit):").strip()
        if query.lower() == "exit":
            print("Thanks for asking see you later 😘")
            break
        if not query:
            print("please you need to ask something")
            continue
        print("processing response...🏃")
        response = rag_chain.invoke({"input":query})
        
        print("\n Generated Response:\n")
        print(response["answer"])
        print("-"*50)