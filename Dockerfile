# Stage 1: Build stage
FROM python:3.11-alpine AS build

RUN apk add --no-cache build-base libffi-dev openssl-dev

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Stage 2: Final runtime stage
FROM python:3.11-alpine

# Create appuser group and user
RUN addgroup -g 1001 appgroup && adduser -u 1001 -G appgroup -D -s /bin/sh appuser

WORKDIR /app

COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app /app

RUN chown -R appuser:appgroup /app && chmod -R 750 /app

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
