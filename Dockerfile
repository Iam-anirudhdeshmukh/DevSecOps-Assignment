FROM python:3.10-slim

WORKDIR /app
COPY src/test_app /app

CMD ["python", "main.py"]
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt