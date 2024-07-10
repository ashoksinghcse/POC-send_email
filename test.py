from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = 'You won $100,000'
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'ashoksinghcs@gmail.com'
mimeMessage['subject'] = 'You won'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

results = service.users().messages().list(userId='me',q='in:jobs is:unread').execute()

messages = results.get('messages',[]);

for message in messages:
	msg = service.users().messages().get(userId='me', id=message['id'],  format='full').execute()

	email_data = msg['payload']['headers']


	for values in email_data:
		name = values['name']
		if name == 'From':
			from_name = values['value']

			for part in msg['payload']['parts']:
				try:
					data = part.get("parts")[0].get("body").get("data")
					byte_code = base64.urlsafe_b64decode(data)
					text = byte_code.decode("utf-8")
					print("This is the message: " + str(text))

					exit()
					# data = part['body']["data"]
					# print(data)


				except Exception as e:
					print("skdjfksjdfkj")
					raise e
					print(str(e))
					exit()

#message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
# print(list)

