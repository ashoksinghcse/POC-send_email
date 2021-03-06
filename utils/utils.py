from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import email
from bs4 import BeautifulSoup
from  utils.logger import Logger


class Utils():
    logger = None
    service = None

    def __init__(self):
        self.logger =  Logger(self.__class__.__name__).get()
        self.logger.info("Class init started")
        print("intialized")
        self.start()
        self.logger.info("GMAIL API authenticated")
        if self.service is not None :
            self.logger.info("GMAIL API connection serviee crated")




    def start(self):
        """Shows basic usage of the Gmail API.
                   Lists the user's Gmail labels.
                   """
        SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
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

    def getmessages(self):
        return self.service.users().messages().list(userId='me').execute()
