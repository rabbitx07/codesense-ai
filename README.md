# 🚀 CodeSense AI

An AI-powered GitHub Repository Analyzer that lets you chat with any codebase using Retrieval-Augmented Generation (RAG).

CodeSense AI automatically clones a GitHub repository, indexes its source code using embeddings and vector search, and answers repository-specific questions using Google's Gemini models.

---

## ✨ Features

* 📂 Load any public GitHub repository
* 🔍 Semantic code search using vector embeddings
* 🤖 Repository-aware AI assistant powered by Gemini
* 📚 Source citations for every answer
* 💬 Interactive chatbot interface
* 🧩 Automatic code chunking and indexing
* ⚡ Fast retrieval with ChromaDB
* 🎨 Modern Streamlit UI

---

## 🏗️ Architecture

```text
GitHub Repository
        ↓
Repository Cloner
        ↓
File Loader
        ↓
Text Chunking
        ↓
Embeddings
        ↓
ChromaDB Vector Store
        ↓
Semantic Retrieval
        ↓
Gemini LLM
        ↓
Natural Language Answers
```

---

## 🛠️ Tech Stack

### Backend

* Python

### AI & RAG

* LangChain
* ChromaDB
* Sentence Transformers
* Gemini API

### Frontend

* Streamlit

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
codesense-ai/

├── app.py
├── streamlit_app.py
├── repo_loader.py
├── chunker.py
├── embedder.py
├── vector_store.py
├── search.py
├── llm.py
├── qa.py
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/rabbitx07/codesense-ai.git
cd codesense-ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your Gemini API key from Google AI Studio.

---

## ▶️ Run Application

```bash
streamlit run streamlit_app.py
```

---

## 💡 Example Questions

* Explain this repository.
* What technologies are used?
* How is the model trained?
* Which file contains the recommendation logic?
* Explain the architecture.
* How are predictions generated?

---



## 👩‍💻 Author

**Anshika**

BCA (AI & Data Science) Student
Graphic Era University

---

