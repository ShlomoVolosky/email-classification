# Model Output Folder

This folder stores **trained model artifacts** and intermediate checkpoints resulting from the training/fine-tuning process.

## Typical Contents

1. **Model Weights** (e.g., `pytorch_model.bin`, `tf_model.h5`)  
   - Contains the learned parameters after the training phase.
2. **Configuration Files** (e.g., `config.json`)  
   - Includes the model architecture, such as hidden size and number of transformer layers.
3. **Tokenizer Files**  
   - Files such as `vocab.txt`, `tokenizer_config.json`, or `sentencepiece.model` that define how text is tokenized for the model.
4. **Checkpoints** (e.g., `checkpoint-1000`, `checkpoint-2000`)  
   - Subfolders created during training to allow resuming or rolling back to previous states.
5. **Saved Model Folders**  
   - Named directories like `category_model`, `priority_model`, or `multitask_model`, each containing the final or intermediate model artifacts.

## Usage

- **Loading the Model**: Use libraries (e.g., Hugging Face `transformers`) and point them to these folders for inference or further fine-tuning.
- **Checkpoints**: If you have multiple checkpoints, decide which best fits your performance criteria or largest metric gains.
- **Versioning**: Large files may require Git LFS or separate storage (like an S3 bucket). If so, remember to keep references here.

## Example Directory Structure

