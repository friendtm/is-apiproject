# Use the official Python 3.12.3 image as a base
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose only the port relevant to this service
EXPOSE 5000

# Default command (this should be adjusted per service Dockerfile)
CMD ["python", "rest_api.py"]
