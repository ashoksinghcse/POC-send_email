from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import email
import os
from bs4 import BeautifulSoup

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

class GmailUtil():
    service = None
    __attachment_dir_name  ="attachments"

    def __init__(self):
        """Shows basic usage of the Gmail API.
           Lists the user's Gmail labels.
           """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('gmail', 'v1', credentials=creds)

    """
    @param file_content,filename
    @desc:download attachement
    @return :void
    """
    def __saveattachment(self,file_data,file_name):
        if not os.path.exists(self.__attachment_dir_name):
            os.makedirs(self.__attachment_dir_name)

        if file_name is not None:
            f = open(self.__attachment_dir_name + "/" + file_name, 'wb')
            f.write(file_data)
            f.close()

    """
    @desc :return list of inbox email message
    @reuturn messages list
    """
    def getEmails(self):
        # request a list of all the messages
        result = self.service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        if not result :
            print("No email found")
        else:
            messages = result.get('messages')
            for msg in messages:
                # Get the message from its id
                message = self.service.users().messages().get(userId='me', id=msg['id']).execute()
                ###EXTRACT SUBJECT MESSGAGE AND BODY OF THE EMAIL

                try:
                    payload = message['payload']
                    headers = payload['headers']
                    # Look for Subject and Sender Email in the headers
                    for d in headers:
                        if d['name'] == 'Subject':
                            subject = d['value']
                        if d['name'] == 'From':
                            sender = d['value']

                            # The Body of the message is in Encrypted format. So, we have to decode it.
                    # Get the data and decode it with base 64 decoder.
                    parts = payload.get('parts')[0]

                    data = parts['body']['data']
                    data = data.replace("-", "+").replace("_", "/")
                    decoded_data = base64.b64decode(data)

                    # Now, the data obtained is in lxml. So, we will parse
                    # it with BeautifulSoup library
                    soup = BeautifulSoup(decoded_data, "lxml")
                    body = soup.body()

                    # Printing the subject, sender's email and message
                    print("Subject: ", subject)
                    print("From: ", sender)
                    print("Message: ", body)
                except:
                    print("body of email can not be parsed")

                ###EXTRACT attachments OF THE EMAIL
                if "parts" in message['payload'] :
                    ##comes in this loop if attachment exists in email
                    for part in message['payload']['parts']:
                        if part['filename']:
                            attachment = self.service.users().messages().attachments().get(userId='me',
                                                                                      messageId=message['id'],
                                                                                      id=part['body'][
                                                                                          'attachmentId']).execute()
                            file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
                            file_name = ''.join([ part['filename']])
                            self.__saveattachment(file_data,file_name)

GmailUtil().getEmails()
