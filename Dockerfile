FROM python:3.11-slim

WORKDIR /app

# Copy requirements separately for better cache efficiency
COPY requirements.txt .

# Upgrade pip and install dependencies without cache
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/test_app/ .

# Use explicit CMD to run the application
CMD ["python", "main.py"]
