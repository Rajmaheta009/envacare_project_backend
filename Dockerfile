# Use the official Python slim image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to keep output unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install essential dependencies first
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

# Install WeasyPrint dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf-xlib-2.0-0 \
    libcairo2

# Install libffi and libglib dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libffi-dev \
    libglib2.0-0

# Install mime-info and PostgreSQL libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    shared-mime-info \
    libpq-dev

# Clean up to reduce image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies with no cache to reduce image size
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy only necessary application code, excluding unnecessary files (use .dockerignore)
COPY . .

# Expose the port the app will run on
EXPOSE 8000

# Default command to run the application using Uvicorn in development mode (with auto-reload)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
