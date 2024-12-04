FROM python:3.9-slim-buster

WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the source code
COPY src/ ./src/

# Command to run the application
CMD ["python", "-m", "src.scribe_data.parsing"] 