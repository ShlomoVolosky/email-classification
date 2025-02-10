# `src` Folder

This folder contains the **source code** for the email classification application and related logic.

## Main Files

1. **`app.py`**  
   - The entry point for the Flask (or Streamlit) application.
   - Manages routes for:
     - Classifying emails (category and priority)
     - Receiving user feedback
     - (Optional) Integration with advanced features like agentic AI
2. **`feedback.py`**  
   - A dedicated module for storing user feedback in a local or external database.
   - Helps keep `app.py` cleaner by separating concerns.
3. **`agent.py`** (Optional/Advanced)  
   - Demonstrates how to integrate Retrieval Augmented Generation (RAG) or advanced AI agents (e.g., with LangChain).
   - Could be used for multi-step reasoning, answering user queries, or referencing knowledge bases.
4. **`utils.py`**  
   - Houses shared utilities such as label mappings, tokenizer/model loading, text normalization functions, etc.

## Folder Organization

You can further split your code by topics:
- **`routes/`** or `controllers/` if you have many API endpoints
- **`services/`** for business logic
- **`db/`** for database handling

## How to Run the Application

1. **Install Dependencies**  
   ```bash
   pip install -r ../requirements.txt
