# 🔧 Maintenance RAG Assistant
### Retrieval-Augmented AI Assistant for Maintenance Queries

An end-to-end RAG project that answers maintenance-related questions using PDF or text documents as a knowledge base.  

This project covers:  
- Document Loading (PDF/TXT)  
- Document Chunking  
- Embeddings Generation (Sentence Transformers)  
- Vector Database Storage (FAISS)  
- Semantic Retrieval  
- LLM-Based Answer Generation (Groq Free Model)  
- Streamlit Web App Deployment

## Minimal Setup Instructions

-**Clone the repository:** git clone <your-github-repo-link> && cd Maintenance-RAG-Assistant

-Create and activate a virtual environment:

-**Windows:** python -m venv venv && venv\Scripts\activate

-**Mac/Linux:** python3 -m venv venv && source venv/bin/activate

-Install required packages: pip install -r requirements.txt

-**Prepare your data:** create a folder named data/ and place your PDFs or TXT files inside (e.g., data/operation-and-maintenance.pdf)

-**Run the Streamlit app:** streamlit run app.py

-Tips: ask maintenance-related questions in the input box, ensure PDFs are readable text, the app retrieves relevant chunks and generates grounded answers.

---

## 📌 Objective

Build a retrieval-based AI assistant that answers maintenance-related questions strictly based on provided documents.  

The assistant should:  
- Retrieve relevant document chunks  
- Generate answers grounded only in retrieved content  
- Log or display retrieved chunks for traceability  

---

## 📊 Dataset

Dataset Used:  
**Maintenance Manuals / Operational PDFs**  

Example document:  
`data/operation-and-maintenance.pdf`  

- Users can upload multiple PDFs or TXT files.  
- Documents contain operational, safety, and maintenance procedures for industrial equipment.  

---

## ⚙️ Project Workflow

1. **Document Loading** – Read PDFs or TXT files from `data/` folder  
2. **Document Chunking** – Split long manuals into 1000-character chunks with overlap  
3. **Embeddings Generation** – Use Sentence Transformers embeddings  
4. **Vector Database Creation** – Store embeddings in FAISS  
5. **Query Retrieval** – Find top-k relevant chunks for user question  
6. **Answer Generation** – LLM generates answer strictly using retrieved context  
7. **Streamlit Deployment** – Web interface to ask questions  

---

## 🧹 Data Preprocessing & Chunking

- Supports multiple files  
- Chunk size: 1000 characters, overlap: 200  
- Ensures large manuals can be retrieved efficiently  

---

## 🤖 Models & Tools Used

- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`  
- **Vector Store:** FAISS (local)  
- **LLM:** Groq Free Model (`llama-3.3-70b-versatile`)  
- **Web App:** Streamlit  

---

## 📈 Sample Input & Output

**Question:** How should the generator set be lifted?  

**AI Response:**  
The generator set should be lifted by first lowering the forklift forks to minimum/ground level and driving them into the forklift pockets under the baseframe of the generator set slowly and carefully. Then, raise the level of the forklift forks slowly around 15-20 cm to lift the generator set from the ground. Guide ropes or equivalents should be used to prevent rotation or swing action, and the operation should be done with caution, avoiding strong winds and keeping people at a safe distance.  

---

## 🏗️ Project Structure

Maintenance-RAG-Assistant/
│

├── app.py             → Streamlit web app

├── rag_core.py        → Core RAG functions

├── requirements.txt

├── README.md

├── data/              → PDF/TXT knowledge base

│     └── operation-and-maintenance.pdf

└── shortnote.txt      → Design notes / assumptions / trade-offs


---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain Core & Community  
- FAISS  
- Groq Free LLM  
- Sentence Transformers  

---

## 💡 Business Impact

- Improves maintenance efficiency  
- Reduces errors or missed steps  
- Provides instant answers to operational queries  
- Ensures safety procedures are followed  

---
