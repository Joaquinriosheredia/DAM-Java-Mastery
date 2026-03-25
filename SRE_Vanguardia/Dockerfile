```Dockerfile
# Use the official lightweight Python image.
FROM python:3.9-slim

# Set environment variables for FastAPI and Pydantic models.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies from requirements.txt file.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code to /app directory in container.
WORKDIR /app
COPY . .

# Expose port for FastAPI service.
EXPOSE 8000

CMD ["python", "vllm_server.py"]
```