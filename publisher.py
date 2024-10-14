import json
from confluent_kafka import Producer

class Publisher:

    def  __init__(self,topic,host = 'localhost:9092'):
        # Kafka Producer configuration
        self.topic = topic
        self.email_key = 'email_key'
        self.producer_config = {
            'bootstrap.servers': host ,# Kafka broker,

        }


    def send_message(self,data):
        """

        :param data:
        :return:
        """
        self.producer = Producer(self.producer_config)
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

#
# # JSON data to send
# data =[{'sent_date': '2024-10-05 23:09:46', 'from_email': 'Naukri Alerts <naukrialerts@naukri.com>', 'to_email': 'Ashok Singh <ashoksinghcs@gmail.com>', 'subject': 'Ashok Singh, Discover Missed Opportunities: Your Weekly Job Recap', 'mail_text': "TS - Python Airflow Developer Weekend Catch-Up: Jobs You Might Have Missed! TS - Python Airflow Developer Srivango 4.2 Bengaluru A AI-ML Python Developer ADA Global Bengaluru Software Developer III Skillmine Technolog... Bengaluru Are these jobs relevant? Yes No Python Developer/ Software Engineer Pyramid It Consulting Hybrid - Chennai,... Python Developer Lead Hexaware Technologies 3.6 Hybrid - Bengaluru Python Developer Coforge 3.4 Hyderabad Software Engineer/Sr Software Engineer - Python - WFO - Blr- JP Nagar Izmo 3.7 Bengaluru(JP Nagar) Python Developer UST 4.0 Chennai, Trivandr... Python Developer Optimum Solutions 3.4 Chennai, Bengaluru B AI/ML Developer Bluebird India R&d ... 2.3 Bengaluru(Mahadev... D Python Developer-ReactJS-Hybrid-Hyderabad, Bangalore Databuzz Hybrid - Bengalur... Python Software Developer Tech Mahindra 3.6 Pune, Bengaluru, ... Senior Product Developer - Python Developer BMC Software 4.1 Bengaluru Lead Python Developer - Bangalore Xoriant 3.8 Hybrid - Bengaluru Jobs outside your preference Sr. Python Developer (FastApi + Sqlalchemy Noida/Gurgaon Vinove Software 1.3 Gurgaon View All Recommendations Applies are a click away on the Naukri app Available on Get App Scan to download Unsubscribe Report a Problem You have received this mail because your e-mail ID is registered with Naukri.com. This is a system-generated e-mail regarding your Naukri account preferences, please don't reply to this message. The jobs sent in this mail have been posted by the clients of Naukri.com. And we have enabled auto-login for your convenience, you are strongly advised not to forward this email to protect your account from unauthorized access. IEIL has taken all reasonable steps to ensure that the information in this mailer is authentic. Users are advised to research bonafides of advertisers independently. Please do not pay any money to anyone who promises to find you a job. IEIL shall not have any responsibility in this regard. We recommend that you visit our Terms & Conditions and the Security Advice for more comprehensive information."},
# {'sent_date': '2024-10-05 23:09:46', 'from_email': 'tttttt', 'to_email': 'Ashok Singh <ashoksinghcs@gmail.com>', 'subject': 'Ashok Singh, Discover Missed Opportunities: Your Weekly Job Recap', 'mail_text': "TS - Python Airflow Developer Weekend Catch-Up: Jobs You Might Have Missed! TS - Python Airflow Developer Srivango 4.2 Bengaluru A AI-ML Python Developer ADA Global Bengaluru Software Developer III Skillmine Technolog... Bengaluru Are these jobs relevant? Yes No Python Developer/ Software Engineer Pyramid It Consulting Hybrid - Chennai,... Python Developer Lead Hexaware Technologies 3.6 Hybrid - Bengaluru Python Developer Coforge 3.4 Hyderabad Software Engineer/Sr Software Engineer - Python - WFO - Blr- JP Nagar Izmo 3.7 Bengaluru(JP Nagar) Python Developer UST 4.0 Chennai, Trivandr... Python Developer Optimum Solutions 3.4 Chennai, Bengaluru B AI/ML Developer Bluebird India R&d ... 2.3 Bengaluru(Mahadev... D Python Developer-ReactJS-Hybrid-Hyderabad, Bangalore Databuzz Hybrid - Bengalur... Python Software Developer Tech Mahindra 3.6 Pune, Bengaluru, ... Senior Product Developer - Python Developer BMC Software 4.1 Bengaluru Lead Python Developer - Bangalore Xoriant 3.8 Hybrid - Bengaluru Jobs outside your preference Sr. Python Developer (FastApi + Sqlalchemy Noida/Gurgaon Vinove Software 1.3 Gurgaon View All Recommendations Applies are a click away on the Naukri app Available on Get App Scan to download Unsubscribe Report a Problem You have received this mail because your e-mail ID is registered with Naukri.com. This is a system-generated e-mail regarding your Naukri account preferences, please don't reply to this message. The jobs sent in this mail have been posted by the clients of Naukri.com. And we have enabled auto-login for your convenience, you are strongly advised not to forward this email to protect your account from unauthorized access. IEIL has taken all reasonable steps to ensure that the information in this mailer is authentic. Users are advised to research bonafides of advertisers independently. Please do not pay any money to anyone who promises to find you a job. IEIL shall not have any responsibility in this regard. We recommend that you visit our Terms & Conditions and the Security Advice for more comprehensive information."}]
# topic = "json_topic"
# publihser = Publisher(topic)
# print(publihser.send_message(data))
#
