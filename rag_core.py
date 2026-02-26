from dotenv import load_dotenv
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

# -----------------------------
# Load Documents
# -----------------------------
def load_documents(folder_path="data"):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            loader = TextLoader(path)
            documents.extend(loader.load())

        elif file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

    return documents


# -----------------------------
# Chunk Documents
# -----------------------------
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)


# -----------------------------
# Create Vector Store
# -----------------------------
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(chunks, embeddings)


# -----------------------------
# Retrieve Chunks
# -----------------------------
def retrieve_chunks(vector_store, query):
    retriever = vector_store.as_retriever()
    return retriever.invoke(query)


# -----------------------------
# Generate Answer using Groq
# -----------------------------
def generate_answer(query, retrieved_docs):
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

    prompt = ChatPromptTemplate.from_template("""
You are a maintenance assistant.

Answer using ONLY the provided context.
If a direct definition is not present, summarize the relevant information from the context.

Context:
{context}

Question:
{question}
""")

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": query
    })

    return response.content