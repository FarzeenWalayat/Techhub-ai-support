# TechHub AI Customer Support

An AI-powered customer support chatbot built with Streamlit, OpenAI, and LangChain.

## Features

- 24/7 automated customer support
- Intent classification and entity extraction
- Natural language responses based on knowledge base
- Handles shipping, returns, product info, and more

## Setup

1. Clone this repo
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Create `.env` with your OpenAI API key
6. Run: `streamlit run ui/app.py`

## Deployment

Deploy on Streamlit Cloud for free at https://streamlit.io/cloud

## Technology

- Python 3.10+
- Streamlit (UI)
- OpenAI GPT-4 (LLM)
- LangChain (orchestration)
- ChromaDB (vector storage)