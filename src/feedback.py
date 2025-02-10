"""
feedback.py

Module for storing user feedback in a local database or external DB.
"""
import sqlite3
import time
import os

def store_feedback(subject, body, predicted_category, predicted_priority,
                   user_feedback, correct_category='', correct_priority=''):
    """
    Store user feedback in a local SQLite DB. 
    Adjust as needed for other databases (PostgreSQL, etc.)

    Args:
        subject (str)
        body (str)
        predicted_category (str)
        predicted_priority (str)
        user_feedback (str)   # 'up', 'down', or 'correction'
        correct_category (str) # user-corrected category if any
        correct_priority (str) # user-corrected priority if any
    """

    # We can store feedback.db in the current directory or data folder
    db_path = os.getenv("FEEDBACK_DB_PATH", "feedback.db")

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            subject TEXT,
            body TEXT,
            predicted_category TEXT,
            predicted_priority TEXT,
            user_feedback TEXT,
            correct_category TEXT,
            correct_priority TEXT
        )
    """)

    c.execute("""
        INSERT INTO feedback (
            timestamp, subject, body,
            predicted_category, predicted_priority,
            user_feedback, correct_category, correct_priority
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        int(time.time()),
        subject,
        body,
        predicted_category,
        predicted_priority,
        user_feedback,
        correct_category,
        correct_priority
    ))
    conn.commit()
    conn.close()
