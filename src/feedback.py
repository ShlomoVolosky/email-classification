# src/feedback.py

import sqlite3
import time

def store_feedback(subject, body, original_prediction, user_feedback, correct_category):
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
    """, (
        int(time.time()), 
        subject, 
        body, 
        original_prediction, 
        user_feedback, 
        correct_category
    ))
    conn.commit()
    conn.close()
