# Use the official Python image from the Docker Hub
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . /app/

# Ensure .env file is present
COPY .env /app/

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
CMD ["python3", "app.py"]
