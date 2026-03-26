# 🤖 AI Resume Screening & Candidate Ranking System (RAG + Chatbot)

An end-to-end AI-powered system that automates resume screening, ranks candidates based on job descriptions, and enables intelligent querying of resumes using a Retrieval-Augmented Generation (RAG) chatbot.

---

## 🚀 Features

* 🔐 **Authentication System**

  * JWT-based login & registration
  * Secure password hashing
  * PostgreSQL-backed user storage

* 📄 **Resume Upload & Processing**

  * Upload PDF resumes
  * Automatic text extraction
  * Intelligent chunking for semantic search

* 🧠 **RAG-based Chatbot**

  * Ask questions about resumes
  * Context-aware answers using FAISS + OpenAI
  * Eliminates hallucinations using retrieval

* 📊 **AI Candidate Ranking**

  * Semantic similarity between job description & resumes
  * Cosine similarity-based ranking
  * Returns ranked candidates with scores

* ⚡ **Vector Search (FAISS)**

  * Fast similarity search
  * In-memory vector indexing
  * Optimized for real-time querying

* 🖥️ **Streamlit UI**

  * Interactive frontend
  * Upload resumes, rank candidates, chat with system
  * Clean and simple interface

---

## 🏗️ Architecture

```
Streamlit UI
     ↓
FastAPI Backend
     ↓
---------------------------------
| PostgreSQL  |  FAISS  | OpenAI |
---------------------------------
```

---

## 🛠️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Backend    | FastAPI               |
| Frontend   | Streamlit             |
| Database   | PostgreSQL            |
| Vector DB  | FAISS                 |
| Embeddings | Sentence Transformers |
| LLM        | OpenAI API            |
| Auth       | JWT                   |

---

## 📂 Project Structure

```
AI-Resume-Screening-Ranking-RAG-Chatbot/
│
├── app/
│   ├── auth/          # Authentication (JWT)
│   ├── ingestion/     # Parsing, chunking, embeddings
│   ├── ranking/       # Candidate ranking logic
│   ├── rag/           # RAG pipeline
│   ├── resume/        # Resume upload & processing
│   ├── db/            # Database + FAISS store
│   └── core/          # Config & security
│
├── ui/
│   └── app.py         # Streamlit frontend
│
├── data/resumes/      # Uploaded resumes
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/AI-Resume-Screening-Ranking-RAG-Chatbot.git
cd AI-Resume-Screening-Ranking-RAG-Chatbot
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/your_db
```

---

### 5️⃣ Run Backend

```
uvicorn app.main:app --reload
```

👉 API Docs: http://127.0.0.1:8000/docs

---

### 6️⃣ Run Frontend

```
streamlit run ui/app.py
```

👉 UI: http://localhost:8501

---

## 🧪 How It Works

### 🔹 Resume Processing

1. Upload PDF
2. Extract text
3. Chunk into smaller pieces
4. Generate embeddings
5. Store in FAISS

---

### 🔹 RAG Chatbot

1. User asks query
2. Relevant chunks retrieved via FAISS
3. Context passed to LLM
4. Answer generated

---

### 🔹 Candidate Ranking

1. Convert job description → embedding
2. Compare with resume embeddings
3. Compute cosine similarity
4. Return ranked results

---

## 📊 Example Use Case

* Upload multiple resumes
* Enter job description
* Get top candidates ranked by relevance
* Ask:

  * "Does this candidate know Python?"
  * "What projects has this candidate worked on?"

---

## ⚠️ Challenges Solved

* Fixed vector store lifecycle issues (in-memory persistence)
* Resolved JSON serialization errors from NumPy types
* Handled authentication mismatch between Swagger & frontend
* Improved RAG accuracy by refining chunking strategy

---

## 🚀 Future Improvements

* Persistent vector database (e.g., Pinecone, Weaviate)
* Resume skill extraction & tagging
* Better UI with React
* Multi-user resume isolation
* Caching for faster responses

---

## 🧠 Key Learnings

* End-to-end ML system design
* RAG architecture implementation
* Vector search using FAISS
* API design with FastAPI
* Database integration with PostgreSQL
* Debugging real-world production issues

---

## 👨‍💻 Author

**Apoorva Krishna**

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork!

