import os
from Google import Create_Service
from dotenv import load_dotenv
import logging
import re,html
from bs4 import BeautifulSoup
import base64
from time import sleep
load_dotenv('.env')
from utils import convert_date_from_string
from  publisher import Publisher
class mailUtil:
	def __init__(self):
		self.CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE")
		self.API_NAME = os.getenv("API_NAME")
		self.API_VERSION =  os.getenv("API_VERSION")
		self.SCOPES = ['https://mail.google.com/']
		self.service = Create_Service(self.CLIENT_SECRET_FILE,self.API_NAME, self.API_VERSION,self.SCOPES)

class Logger(object):
    def __init__(self, name):
        name = name.replace('.log','')
        logger = logging.getLogger('log_namespace.%s' % name)  # log_namespace can be replaced with your namespace
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            #date_tag = datetime.now().strftime("%Y-%b-%d")
            #file_name = os.path.join(os.getcwd() + "/logs/application_"+ str(date_tag) + ".log")
            logpath = os.getcwd() + "/logs/app.log"
            if not os.path.exists(logpath):
                os.mkdir("logs")
            file_name = os.path.join(os.getcwd() + "/logs/app.log")# usually I keep the LOGGING_DIR defined in some global settings file
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler) # finally add handler to logger
        self._logger = logger

    def get(self):
        return self._logger

class TextConverter:
    def __clean_text(self,text):
        try:
            text = html.unescape(text)
            # Remove leading/trailing whitespace
            text = text.strip()
            # Replace multiple newlines and spaces with a single space
            text = re.sub(r'\s+', ' ', text)
            return text
        except Exception as e:
            print(str(e))



    def convert_into_text(self,content):
        try:
            soup = BeautifulSoup(content, 'lxml')
            # Extract and print the text
            return self.__clean_text(soup.get_text(separator=' '))
        except Exception as e:
            print(str(e))



class MailRead(mailUtil,TextConverter):
    def __init__(self):
        super().__init__()
        self.logger = Logger(self.__class__.__name__).get()
        self.default_mail_count = os.getenv("DEFAULT_MAIL_COUNT")
        self.SAVE_EMAIL_HTML = os.getenv("SAVE_EMAIL_HTML")

        if self.service is not None:
            self.logger.info("Gmail Account is logged in")

    def __mark_email_as_read(self, message):
        "mark email as read"
        self.service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()

    def __get_header_of_email(self,message):
        headers_info = {}
        if "payload" in message:
            if "headers" in message.get("payload"):
                headers = message['payload']['headers']
                if isinstance(headers,list):
                    for hdr in headers:
                        if hdr.get("name") == 'From':
                            headers_info["from_email"] = hdr.get("value")
                        elif hdr.get("name") == 'To':
                            headers_info["to_email"] = hdr.get("value")
                        elif hdr.get("name") == 'Subject':
                            headers_info["subject"] = hdr.get("value")
                        elif hdr.get("name") == 'Date':
                            headers_info["sent_date"] = hdr.get("value")
        return headers_info

    def __get_body_of_email(self,message):
        try:
            text = None

            # print(message)

            if "payload" in message:

                payload = message.get("payload")

                if "parts" in payload:

                    parts = payload.get("parts")
                    # print(parts)

                    for p in parts:
                        if "parts" in p:
                            for in_parts in p.get("parts"):
                                body = in_parts.get("body")
                                data = body.get("data")
                                byte_code = base64.urlsafe_b64decode(data)
                                text = byte_code.decode("utf-8")
                        else:
                            body = p.get("body")
                            data = body.get("data")

                            byte_code = base64.urlsafe_b64decode(data)
                            text = byte_code.decode("utf-8")
                        byte_code = base64.urlsafe_b64decode(data)
                        text = byte_code.decode("utf-8")
                        # print(text)
                        if self.SAVE_EMAIL_HTML:
                            folder = os.getenv("EMAIL_FOLDER")
                            file_name = f"{folder}/{message.get('id')}.html"
                            f = open(file_name, "w")
                            f.write(text)
                elif "body" in payload:

                    body = payload.get("body")
                    if "data" in body:
                        data = body.get("data")
                        byte_code = base64.urlsafe_b64decode(data)
                        text = byte_code.decode("utf-8")
                        if self.SAVE_EMAIL_HTML:
                            folder = os.getenv("EMAIL_FOLDER")
                            file_name = f"{folder}/{message.get('id')}.html"
                            f = open(file_name, "w")

                return self.convert_into_text(text)
        except Exception as e:
            print(str(e))



    def fetch_email(self):
        try:
            email_list = []
            results = self.service.users().messages().list(userId='me', q='in:jobs is:unread').execute()
            messages = results.get('messages', []);
            #print(messages)
            #iterate throught the emails
            for msg in messages:


                email_details = {}
                m = self.service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                #make the mail unread
                self.service.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}).execute()
                headers = self.__get_header_of_email(m)
                body = self.__get_body_of_email(m)
                plaintext =str(self.convert_into_text(body))
                headers["mail_text"] = plaintext

                #print(headers)
                #exit()
                #exit()

                #exit()
                #self.__mark_email_as_read(msg)

                #email_details["body"] = str(self.convert_into_text(body))
                email_list.append(headers)
                #print(email_list)
                topic = "json_topic"
                publihser = Publisher(topic)
                print("headers",headers)
                print(publihser.send_message(headers))
                #exit()

                #Publisher()

                #exit()
                #pass
            return  email_list
        except Exception as e:
            print(str(e))
            raise  e
            self.logger.exception(str(e))





