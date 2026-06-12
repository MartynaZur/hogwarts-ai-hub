# Hogwarts AI Hub

Welcome to the **Hogwarts AI Hub** – an interactive, AI-powered application that brings the magic of the wizarding world into the realm of Artificial Intelligence! 

This project was built to demonstrate the practical integration of Large Language Models (LLMs) with custom knowledge bases using a **RAG (Retrieval-Augmented Generation)** architecture.

## Core Features:

* **The Sorting Hat (Conversational AI):** Chat with a sentient Sorting Hat that analyzes your personality through psychological questions and sorts you into your rightful Hogwarts House. Built with advanced Role Prompting, session state memory, and input guardrails (protecting against prompt injection).
* **The Great Library (RAG System):** Ask questions about the Harry Potter universe! The system searches through a custom local vector database (built from raw Fandom Wiki articles) to provide accurate, contextualized answers, ensuring *Grounded Generation*.

## Tech Stack and Architecture:

* **Frontend UI:** [Streamlit](https://streamlit.io/) (for rapid, interactive Python web apps)
* **AI Orchestration:** [LangChain](https://www.langchain.com/) 
* **Language Model (LLM):** Meta's `Llama-3.1-8B` running on [Groq API](https://groq.com/) (utilizing LPU technology for ultra-low latency inference).
* **Embeddings:** `all-MiniLM-L6-v2` via HuggingFace (efficient semantic representations).
* **Vector Database:** [ChromaDB](https://www.trychroma.com/) (embedded locally for fast similarity search).

## How to Run Locally:

Follow these steps to explore project on your own machine:

**1. Clone the repository:**

```bash
git clone https://github.com/MartynaZur/hogwarts-ai-hub.git
cd hogwarts-ai-hub
```

**2. Install dependencies:**

Make sure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

**3. Set up Environment Variables:**

Create a .env file in the root directory and add your Groq API key:

```bash
GROQ_API_KEY=your_api_key_here
```

**4. Initialize the Vector Database:**
Before using the Library, you must process the raw text files from the data/ folder into vectors:

```bash
python knowledge_base.py
```

This will generate a local chroma_db/ folder.

**5. Run the Application:**
Launch the Streamlit server:

```bash
streamlit run app.py
```