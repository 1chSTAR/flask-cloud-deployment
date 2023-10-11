# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and any other required packages
RUN pip install --no-cache-dir flask

# Make port 5000 available to the world outside this container.
EXPOSE 5000

# Define environment variable to ensure Flask runs in production mode
ENV FLASK_ENV=production

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
