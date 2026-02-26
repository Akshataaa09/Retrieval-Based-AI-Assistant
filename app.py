import streamlit as st
from rag_core import (
    load_documents,
    chunk_documents,
    create_vector_store,
    retrieve_chunks,
    generate_answer
)

st.title("Maintenance RAG Assistant (Groq Free Version)")

# Create vector store once
if "vector_store" not in st.session_state:
    docs = load_documents("data")
    chunks = chunk_documents(docs)
    st.session_state.vector_store = create_vector_store(chunks)

query = st.text_input("Ask a maintenance-related question:")

if query:
    retrieved_docs = retrieve_chunks(st.session_state.vector_store, query)
    answer = generate_answer(query, retrieved_docs)

    st.subheader("AI Response")
    st.write(answer)