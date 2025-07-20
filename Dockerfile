FROM python:3.13-slim

WORKDIR /app

# Copy requirements separately for better caching
COPY requirements.txt /app/

# Upgrade pip and install dependencies with no cache and no recommended packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/test_app /app

# Use explicit entrypoint CMD
CMD ["python", "main.py"]
