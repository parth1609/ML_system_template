# Use the official Python image as the base image
FROM python:3.11-slim

# Update the package lists and upgrade packages
RUN apt-get update && apt-get upgrade -y

# Set the working directory to /workspace
WORKDIR /workspace

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

 v