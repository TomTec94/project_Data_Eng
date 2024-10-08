# Project Title

## Project Overview
This project is a containerized application that processes sensor data using Kafka and stores it in MongoDB for further analysis.

![image](https://github.com/user-attachments/assets/9696d694-65d0-4a69-86ee-6d7b06b0340e)


## Prerequisites
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.x with packages: `kafka-python`, `pymongo`

## Setup Instructions

### Clone the Repository
```
git clone https://github.com/TomTec94/project_Data_Eng.git
cd project_Data_Eng
````
## Build and Start the Docker Containers

### Build the containers:
```bash
docker-compose build
```

### Start the containers:
```bash
docker-compose up
```

## Check Logs

### Producer Logs:
```bash
docker-compose logs producer
```

### Consumer Logs:
```bash
docker-compose logs consumer
```

### Kafka Logs:
```bash
docker-compose logs kafka
```

### MongoDB Logs:
```bash
docker-compose logs mongodb
```

## Running the Pipeline

To start the full data pipeline, simply run:
```bash
docker-compose up
```

## Troubleshooting Tips

- **Producer.py / Consumer.py are not runnuing**: It can take some time at first start till kafka and mongoDB is started complete.
  If you check with `docker ps`  and there are not the consumer and producer are listed then try to start all containers again with `docker-compose up`
- **NoBrokersAvailable**: Ensure Kafka is running and the correct port is exposed.
- **MongoDB Connection Issues**: Check the connection string and verify MongoDB container is up.

## Configuration Details

- **Environment Variables**: Configure any required environment variables in `.env` or within `docker-compose.yml`.
- **Kafka Topics & Box IDs**: Adjust in the code or configuration files as needed.

## Next Steps for Use

- **Querying MongoDB**: Use MongoDB shell or any client to query the `sensor_database` for stored data.
- **Potential Extensions**:
  - Visualization of the data using tools like Grafana.
  - Data analysis and reporting using Python or BI tools.
