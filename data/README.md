# Data Folder

This folder contains all datasets and related files for the project. Its structure is typically divided into two main subfolders:

1. **`raw/`**  
   - Contains the original, unmodified datasets (e.g., CSV, JSON, or any other format).
   - Do not alter these files to maintain a reference to the original data.

2. **`processed/`**  
   - Contains cleaned and preprocessed datasets that are ready for model training and evaluation.
   - For example, you might have:
     - `train.csv` – The training set
     - `test.csv` – The test set
     - Additional files with intermediate processing steps (if needed)

## Guidelines

- **Data Security**: Ensure no sensitive or personal identifiable information (PII) is inadvertently shared or committed to version control.
- **Versioning**: If you are modifying or splitting datasets frequently, consider naming convention like `train_v1.csv`, `train_v2.csv` to keep track of changes.
- **Size Constraints**: Large files may require using Git LFS or storing data externally (e.g., cloud storage) to avoid ballooning the repository size.

## Typical Workflow

1. **Add raw data** to `raw/`.
2. **Run preprocessing notebooks** (in the `notebooks/` folder). 
3. **Output cleaned files** to `processed/`.
4. **Train/test splits** are typically placed in `processed/`.

Contact the data team if you need additional datasets or clarifications.
