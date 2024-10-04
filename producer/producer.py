from kafka import KafkaProducer
import requests
import json
import time

# load the box ids to get the api paths of each box
with open('/app/box_ids.json', 'r') as file:
    box_ids = json.load(file)


# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers='kafka:9092',  # Use kafka' instead of 'localhost'
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def fetch_and_produce_data():
    while True:
        for box_id in box_ids: # iterate through the boxes
            # API path to fetch data for a specific box from OpenSenseMap
            url = f'https://api.opensensemap.org/boxes/{box_id}'

            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                # Add box ID to the data if not already there
                data['box_id'] = box_id

                # Send data to the appropriate Kafka topic
                producer.send(f'sensor_data_{box_id}', data)
                print(f"Data sent to topic sensor_data_{box_id}: {data}")
            else:
                print(f"Failed to fetch data for box {box_id}: {response.status_code}")

        # Fetch data every 60 seconds
        time.sleep(60)


if __name__ == "__main__":
    fetch_and_produce_data()
