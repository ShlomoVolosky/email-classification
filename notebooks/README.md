# Notebooks Folder

This folder contains Jupyter notebooks that detail the step-by-step process of developing and evaluating the email classification system.

## Structure

- **`01_data_preparation.ipynb`**  
  - Scripts for cleaning, normalizing, and splitting the raw dataset into training and test sets.
- **`02_model_finetuning.ipynb`**  
  - Code to fine-tune the chosen transformer models (e.g., multilingual BERT or XLM-R) on the preprocessed dataset.
- **`03_evaluation.ipynb`**  
  - Evaluation scripts that calculate metrics like accuracy, precision, recall, and F1-score on the test set.
- (Optional) **`04_feedback_retraining.ipynb`**  
  - A notebook that demonstrates how to re-train or fine-tune the model using user feedback data (if implemented).

## Usage

1. **Run Notebooks in Order**  
   - Typically, start with `01_data_preparation.ipynb`, then proceed to the training and evaluation notebooks.
2. **Dependencies**  
   - Make sure to install the required libraries as listed in the project’s `requirements.txt`.
3. **Documentation**  
   - Each notebook should contain markdown cells explaining the purpose of each code block and results.

## Best Practices

- Keep notebooks well-documented with **markdown cells** explaining your steps.
- Use **version control** for notebooks; commit them after major changes or improvements.
- **Parameterize** notebooks (if possible) for reusability and reproducibility.
