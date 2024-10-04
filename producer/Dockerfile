FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy all necessary files into the container
COPY producer.py .
COPY box_ids.json .

# Install required Python packages
RUN pip install kafka-python requests

# Start the producer script
CMD ["python", "producer.py"]

