FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all necessary files into the container
COPY consumer.py .

# Install required Python packages
RUN pip install kafka-python pymongo

# Start the consumer script
CMD ["python", "consumer.py"]

