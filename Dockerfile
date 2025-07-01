FROM python:3.10-slim

WORKDIR /app

# Copy requirements.txt separately first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/test_app /app

CMD ["python", "main.py"]
