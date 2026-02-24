🏠 AI Real Estate Quiz Bot (RAG-Based)
📌 Overview

This project is an AI-powered Real Estate Quiz Bot built using:
Streamlit for the frontend
Google Gemini API for question generation and evaluation
Sentence Transformers for embeddings
Vector Database (FAISS/Chroma) for semantic retrieval
The system uses a Retrieval-Augmented Generation (RAG) approach to generate context-aware quiz questions based on property listings.


🚀 Features: 
🧠 AI-generated real estate questions
📚 Context-aware question generation using vector search
✍️ User answer evaluation
🔎 Semantic similarity-based retrieval
📝 Multi-question quiz flow with “Next Question” option


🏗️ How It Works (Architecture)

The system follows a Retrieval-Augmented Generation (RAG) pipeline:

1️⃣ Property listings (from housing.csv) are converted into embeddings.
2️⃣ Embeddings are stored in a vector database.
3️⃣ When a quiz starts:

Relevant property data is retrieved using similarity search.

The retrieved context is passed to the Gemini model.
4️⃣ The LLM generates a question based on the retrieved property data.
5️⃣ The user submits an answer.
6️⃣ The system evaluates and provides feedback.

🔄 Workflow

User → Query → Vector Search → Retrieved Property Context → Gemini LLM → Question → User Answer → Evaluation

📂 Project Structure
project/
│
├── app.py                # Streamlit application
├── vector_db.py          # Vector database setup and search
├── housing.csv           # Property dataset
├── requirements.txt
🛠️ Installation

1️⃣ Clone the Repository
git clone <your-repo-link>
cd project-folder
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set API Key

Windows:
set GEMINI_API_KEY=your_api_key_here

Mac/Linux:
export GEMINI_API_KEY=your_api_key_here

5️⃣ Run the App
streamlit run app.py

🔍 Technologies Used
Python
Streamlit
Google Gemini (google-genai SDK)
SentenceTransformers (all-MiniLM-L6-v2)
FAISS / Chroma

🎯 Purpose of the Project
This project demonstrates:
Integration of LLM APIs
Implementation of semantic vector search
Building a basic RAG pipeline
Optimizing API calls
Developing an interactive AI-based quiz system


📈 Future Improvements
Add performance tracking
Improve UI styling
Deploy to cloud
Add authentication
Generate quiz reports


🧠 Learning Outcomes
Through this project, I learned:
How vector databases improve LLM accuracy
How to implement Retrieval-Augmented Generation
How to structure an AI-powered application
