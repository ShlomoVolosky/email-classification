"""
utils.py

Contains helper functions, label mappings, and common utilities.
"""
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Example label maps for 3 categories and 3 priorities
category_map = {
    0: "HR",
    1: "Finance",
    2: "Support"
    # Extend as needed
}

priority_map = {
    0: "Low",
    1: "Medium",
    2: "High"
}

def load_models(model_path: str):
    """
    Loads a tokenizer and model from the given path.
    Adjust or expand error handling, device usage (GPU vs CPU), etc.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    return tokenizer, model

def text_cleanup(text: str) -> str:
    """
    Example text cleanup function for advanced logic.
    Could handle Hebrew/English detection, punctuation removal, etc.
    """
    # Implement advanced normalization if needed
    return text.strip()
