# Use official Python base image
FROM python:3.10-slim

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy the entire project to the container
COPY . /app/

# Install pip and Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Run the FastAPI app via main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
