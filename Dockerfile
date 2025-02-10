# Dockerfile
FROM python:3.9-slim

# Create working directory
WORKDIR /email-classification

# Copy requirements
COPY requirements.txt /email-classification/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /email-classification

# Expose the Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
