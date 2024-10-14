import json
from confluent_kafka import Consumer, KafkaException
import time
from datetime import datetime


class Subscriber:
    consumer = None

    def __init__(self,host,group,topic):
        self.host = host
        self.group = group
        self.topic = topic
        consumer_config = {
            'bootstrap.servers': self.host ,  # Kafka broker
            'group.id': self.group,  # Consumer group ID
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,  # Disable auto commit to manually manage offsets
            # 'session.timeout.ms': 30000,
            # Start reading at the earliest message
        }
        # Create a Kafka consumer instance
        self.consumer = Consumer(consumer_config)


# Kafka Consumer configuration

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker
    'group.id': 'json_consumer_group',  # Consumer group ID
    'auto.offset.reset': 'latest',
    'enable.auto.commit':False,
    'session.timeout.ms': 30000,
    'max.poll.interval.ms':600000,
    # 'enable.auto.commit':False,
    # 'session.timeout.ms':30000
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
        formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('subscriber.txt', 'w') as f:
            f.write(str(formatted_datetime))

        if msg is None:
            # No message received
            continue
        if msg.error():
            raise KafkaException(msg.error())

        # Decode the received message
        json_message = msg.value().decode('utf-8')

        # Convert the JSON string back to a Python dictionary

        data = json.loads(json_message)
        print(data)

        # Process the message (save to a file, print, etc.)
        with open('received_email.json', 'w') as f:
            json.dump(data, f, indent=4)

        from dao.email_model import Email
        #inserted_data = data[0]


        emailobj = Email()



        emailobj.save_data(data['from_email'],data["to_email"],data["mail_text"],data["sent_date"], data["subject"])
        print(f"Message received and saved: {data}")
        consumer.commit(msg)

        #break

except KeyboardInterrupt:
    pass
finally:
    # Close down consumer cleanly
    consumer.close()
