import json
from confluent_kafka import Producer

class Publisher:

    def  __init__(self,topic,host = 'localhost:9092'):
        # Kafka Producer configuration
        self.topic = topic
        self.email_key = 'email_key'
        producer_config = {
            'bootstrap.servers': host # Kafka broker
        }
        self.producer = Producer(producer_config)

    def send_message(self,data):
        """

        :param data:
        :return:
        """
        try:
            # Convert the JSON data to a string format
            json_data = json.dumps(data)

            # Produce (send) the message to the Kafka topic
            self.producer.produce(self.topic, key=self.email_key, value=json_data)

            # Wait for any outstanding messages to be sent to the broker
            self.producer.flush()

            return ("Message sent successfully!")
        except Exception as e:
            print(str(e))








# Create a Kafka producer instance


# JSON data to send
data = {
    "from": "sender@example.com",
    "subject": "Kafka JSON Test",
    "date": "2024-09-03 10:55:43"
}
topic = "json_topic"
publihser = Publisher(topic)
print(publihser.send_message(data))

