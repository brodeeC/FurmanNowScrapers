FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to cache dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY backend/app/ .

# Expose the port your app runs on
EXPOSE 8080

# Command to run your app, change as needed
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080"]