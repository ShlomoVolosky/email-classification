"""
app.py

Main Flask application that exposes endpoints for:
- Classifying emails (subject + body).
- Displaying a simple UI for user input.
- (Optionally) displaying or integrating agentic AI responses.
- Delegating feedback storage to feedback.py.
"""

import os
import sqlite3
import time
from flask import Flask, request, render_template
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Import feedback handling function
from feedback import store_feedback

# Import any common utilities (label maps, etc.)
from utils import category_map, priority_map, load_models

app = Flask(__name__)

# ---------------------------------------------------
# Load models (category and priority), tokenizers
# ---------------------------------------------------
# Adjust these paths to your actual model locations
cat_model_path = os.getenv("CAT_MODEL_PATH", "../model_output/category_model")
pri_model_path = os.getenv("PRI_MODEL_PATH", "../model_output/priority_model")

cat_tokenizer, cat_model = load_models(cat_model_path)
pri_tokenizer, pri_model = load_models(pri_model_path)

# In case you prefer a multi-task single model, you'd load just one set of tokenizer/model.

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the main page with a form for subject/body.
    If POST request, performs classification for category and priority.
    """
    if request.method == 'POST':
        subject = request.form.get('subject', '')
        body = request.form.get('body', '')
        full_text = subject + " " + body

        # Category prediction
        cat_inputs = cat_tokenizer(full_text, return_tensors="pt", 
                                   truncation=True, max_length=256)
        with torch.no_grad():
            cat_logits = cat_model(**cat_inputs).logits
        cat_pred_id = torch.argmax(cat_logits, dim=1).item()
        predicted_category = category_map.get(cat_pred_id, "Unknown")

        # Priority prediction
        pri_inputs = pri_tokenizer(full_text, return_tensors="pt", 
                                   truncation=True, max_length=256)
        with torch.no_grad():
            pri_logits = pri_model(**pri_inputs).logits
        pri_pred_id = torch.argmax(pri_logits, dim=1).item()
        predicted_priority = priority_map.get(pri_pred_id, "Unknown")

        return render_template('index.html',
                               subject=subject,
                               body=body,
                               predicted_category=predicted_category,
                               predicted_priority=predicted_priority)
    else:
        # GET request => show empty form
        return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    """
    Endpoint to handle user feedback (thumbs up/down or corrected labels).
    Delegates to feedback.py for storage.
    """
    user_feedback = request.form.get('user_feedback', '')  # e.g. 'up', 'down', 'correction'
    correct_category = request.form.get('correct_category', '')
    correct_priority = request.form.get('correct_priority', '')
    predicted_category = request.form.get('predicted_category', '')
    predicted_priority = request.form.get('predicted_priority', '')
    subject = request.form.get('subject', '')
    body = request.form.get('body', '')

    # Call the feedback storage function
    store_feedback(subject, body, predicted_category, predicted_priority,
                   user_feedback, correct_category, correct_priority)

    return "Feedback received", 200

# (Optional) If you have an endpoint for agentic AI or RAG-based Q&A:
# from agent import run_agentic_query
# @app.route("/agentic", methods=['POST'])
# def agentic():
#     user_query = request.form.get("user_query", "")
#     response = run_agentic_query(user_query)
#     return {"response": response}

if __name__ == "__main__":
    # For local dev. In production, use gunicorn or similar WSGI server.
    app.run(debug=True, host='0.0.0.0', port=5000)
