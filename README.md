🔹 Overview

The AI-Powered Real Estate Quiz Bot is an intelligent learning system designed to generate context-aware real estate questions using Large Language Models (LLMs) combined with semantic vector search.

The application leverages Retrieval-Augmented Generation (RAG) architecture to enhance question relevance and reduce hallucination by grounding responses in real property data.

The system is built using Streamlit for the user interface, Google Gemini API for natural language generation, and a vector database for semantic retrieval.

🚀 Key Features

AI-generated real estate quiz questions

Context-aware question generation using vector search

Intelligent answer evaluation

Multi-question quiz flow

Optimized API usage

RAG-based architecture implementation

🛠 Installation & Setup
Step 1: Clone Repository
git clone <repository-link>
cd project-folder
Step 2: Create Virtual Environment
python -m venv venv
venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Set API Key

Windows:

set GEMINI_API_KEY=your_api_key

Mac/Linux:

export GEMINI_API_KEY=your_api_key
Step 5: Run Application
streamlit run app.py
🏗 Project Structure
project/
│
├── app.py
├── vector_db.py
├── housing.csv
├── requirements.txt
└── README.md

🔍 Technologies Used

Python

Streamlit

Google Gemini (google-genai SDK)

SentenceTransformers (all-MiniLM-L6-v2)

FAISS / Chroma Vector Database
