from kafka import KafkaConsumer
from pymongo import MongoClient, errors
import json
import time
import re

# Initialize MongoDB Client
client = MongoClient('mongodb', 27017)
db = client['sensor_database']
collection = db['sensor_collection']

# Initialize Kafka Consumer to subscribe to all sensor topics
consumer = KafkaConsumer(bootstrap_servers='kafka:9092',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Subscribe to all topics prefixed with 'sensor_data_'
consumer.subscribe(pattern='^sensor_data_.*')

# Continuously process data from the consumer
while True:
    # Poll for new messages
    records = consumer.poll(timeout_ms=1000)
    for topic_partition, messages in records.items():
        # Extract the box ID from the topic name
        topic = topic_partition.topic
        box_id_match = re.match(r'sensor_data_(.*)', topic)
        if box_id_match:
            box_id = box_id_match.group(1)

            for message in messages:
                data = message.value
                # Remove `_id` field to avoid duplicates
                if '_id' in data:
                    del data['_id']
                # Add box ID to MongoDB document
                data['box_id'] = box_id

                try:
                    collection.insert_one(data)
                    print(f"Inserted data for box {box_id}: {data}")
                except errors.PyMongoError as e:
                    print(f"Error inserting data for box {box_id}: {e}")

    # Small delay to prevent tight loop if no data is available
    time.sleep(1)
