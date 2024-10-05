import json
from confluent_kafka import Consumer, KafkaException

class Subscriber:
    consumer = None

    def __init__(self,host,group,topic):
        self.host = host
        self.group = group
        self.topic = topic
        consumer_config = {
            'bootstrap.servers': self.host ,  # Kafka broker
            'group.id': self.group,  # Consumer group ID
            'auto.offset.reset': 'earliest'  # Start reading at the earliest message
        }
        # Create a Kafka consumer instance
        self.consumer = Consumer(consumer_config)


# Kafka Consumer configuration

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker
    'group.id': 'json_consumer_group',  # Consumer group ID
    'auto.offset.reset': 'earliest'  # Start reading at the earliest message
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)

# Subscribe to the Kafka topic
consumer.subscribe(['json_topic'])

# Consume messages in a loop
try:
    while True:
        # Poll for a new message
        msg = consumer.poll(timeout=1.0)

        if msg is None:
            # No message received
            continue
        if msg.error():
            raise KafkaException(msg.error())

        # Decode the received message
        json_message = msg.value().decode('utf-8')

        # Convert the JSON string back to a Python dictionary
        data = json.loads(json_message)

        # Process the message (save to a file, print, etc.)
        with open('received_email.json', 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Message received and saved: {data}")
        #break

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer cleanly
    consumer.close()
