# Email Classification & Prioritization System

![Email Classification Dashboard](./images/email_classification.jpg)

A comprehensive solution that **automatically classifies** and **prioritizes** emails in real-time. This project leverages **state-of-the-art NLP** and **Generative AI** models to boost productivity and ensure critical emails get the attention they deserve.

## Overview

- **Multi-Lingual Support**: Built with multilingual transformers (e.g., mBERT, XLM-R), enabling classification for both English and Hebrew emails out of the box.  
- **Category & Priority Classification**: Classifies emails into user-defined categories (e.g., HR, Finance, Support) and assigns priority levels (High, Medium, Low).  
- **Human-in-the-Loop Feedback**: Provides a web-based interface for users to correct misclassifications, feeding back into the training loop to continuously improve the model.  
- **Agentic AI & Retrieval Augmentation (Optional)**: Integrates advanced retrieval-based techniques (LangChain/LangGraph) for context-aware classifications and rich, explainable results.

## Features

1. **Data Prep & Model Training**  
   - Jupyter notebooks guide you through collecting, cleaning, and splitting email data.  
   - Fine-tuning notebooks for category and priority classification (either separate or multi-task approaches).

2. **Evaluation & Metrics**  
   - Automatic calculation of accuracy, precision, recall, F1-score.  
   - Confusion matrices for detailed analysis of misclassifications.

3. **UI/Chatbot & Feedback**  
   - A Flask-based web application where users can input email subject/body and see instant classification results.  
   - Thumbs up/down or corrected labels are stored for retraining, enabling active learning.

4. **Cloud & Real-Time Integration**  
   - Container-ready with Dockerfile for easy deployment (GCP, Azure, or on-prem).  
   - Potential integration with streaming platforms (Kafka, Flink) for real-time email ingestion.

## Quick Start

1. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
