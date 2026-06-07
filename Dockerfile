# Use a minimal Python base image; change as needed for your project
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Python dependencies if provided
COPY requirements.txt .
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copy app sources
COPY . .

# Default command (change to your app entrypoint)
CMD ["python", "app.py"]
