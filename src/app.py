# src/app.py

from flask import Flask, request, render_template
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sqlite3
import time

app = Flask(__name__)

# Load model & tokenizer (already saved from training)
MODEL_PATH = "../model_output/multilingual_model"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

# Example label mapping (adjust to match your dataset)
label_map = {
    0: "HR",
    1: "Finance",
    2: "Support"
    # etc...
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form.get('subject', '')
        body = request.form.get('body', '')
        full_text = subject + " " + body
        
        # Predict category
        inputs = tokenizer(full_text, return_tensors="pt", truncation=True, max_length=256)
        with torch.no_grad():
            logits = model(**inputs).logits
        pred_id = torch.argmax(logits, dim=1).item()
        predicted_category = label_map[pred_id]
        
        return render_template('index.html', 
                               predicted_category=predicted_category,
                               subject=subject, 
                               body=body)
    else:
        return render_template('index.html')

@app.route('/feedback', methods=['POST'])
def feedback():
    """
    Endpoint to handle user feedback: 
    The user can provide thumbs up/down and corrected label if needed.
    """
    user_feedback = request.form.get('user_feedback')  # e.g., 'up' or 'down'
    correct_category = request.form.get('correct_category', '')  # e.g., "Finance"
    original_prediction = request.form.get('original_prediction', '')
    subject = request.form.get('subject', '')
    body = request.form.get('body', '')

    # Store feedback in a simple local SQLite DB or text file
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            subject TEXT,
            body TEXT,
            original_prediction TEXT,
            user_feedback TEXT,
            correct_category TEXT
        )
    """)
    c.execute("""
        INSERT INTO feedback (
            timestamp, subject, body, original_prediction, user_feedback, correct_category
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (int(time.time()), subject, body, original_prediction, user_feedback, correct_category))
    conn.commit()
    conn.close()

    return "Feedback received!", 200

if __name__ == "__main__":
    app.run(debug=True)
