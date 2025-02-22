from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils import *

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
	#print(email_data)
	#exit()
	for values in email_data:
		name = values['name']
		if name == 'Date':
			date = convert_date_from_string(values['value'])
			print(date)


	exit()
	service.users().messages().modify(userId='me', id=message['id'], body={
		'removeLabelIds': ['UNREAD']
	}).execute()




	for values in email_data:
		name = values['name']
		if name == 'From':
			from_name = values['value']

			msgpaylod = msg['payload']
			if "parts" in msgpaylod:
				for part in msg['payload']['parts']:
					try:
						if "parts" in part:
							if len(part.get("parts")) > 0 :
								body = part.get("parts")[0].get("body")
								if "data" in body:
									data = part.get("parts")[0].get("body").get("data")
									byte_code = base64.urlsafe_b64decode(data)
									text = byte_code.decode("utf-8")
									print("This is the message: " + str(text))
									folder = "mail/html/20241002/"
									textfolder = "mail/text/20241002/"
									fname = message['id'] + ".html"
									txt = message['id'] + ".txt"
									filename = f"{folder}{fname}"
									txtfname = f"{textfolder}{txt}"
									f = open(fname, "w")
									f.write(str(text))
									txtf = open(txtfname, "w")
									txtcontent = convert_text_from_html(text)
									txtf.write(txtcontent)
						else:
							if "body" in part:
								body = part.get("body")
								if "data" in body:
									data = body.get("data")
									byte_code = base64.urlsafe_b64decode(data)
									text = byte_code.decode("utf-8")
									print("This is the message: " + str(text))
									folder = "mail/html/20241002/"
									textfolder = "mail/text/20241002/"
									fname = message['id'] + ".html"
									txt = message['id'] + ".txt"
									filename = f"{folder}{fname}"
									txtfname = f"{textfolder}{txt}"
									f = open(fname, "w")
									f.write(str(text))
									txtf = open(txtfname, "w")
									txtcontent = convert_text_from_html(text)
									txtf.write(txtcontent)


							#print("here different body email")
							#exit()



					# exit()
					# data = part['body']["data"]
					# print(data)

					except Exception as e:
						print("skdjfksjdfkj")
						raise e
						print(str(e))
						exit()
			else :
				#check if body exits or not
				if "body" in msgpaylod:
					body = msgpaylod.get("body")
					#decode byte code and convert into text
					byte_code = base64.urlsafe_b64decode(body.get("data"))
					html = byte_code.decode("utf-8")
					folder = "mail/html/20241002/"
					textfolder = "mail/text/20241002/"
					fname = message['id'] + ".html"
					txt = message['id'] + ".txt"
					filename = f"{folder}{fname}"
					txtfname = f"{textfolder}{txt}"
					f = open(fname, "w")
					f.write(str(html))
					txtf = open(txtfname, "w")
					txtcontent = convert_text_from_html(html)
					txtf.write(txtcontent)

					#print(text)
					#print(body)

				#exit()
				#pass


#message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
# print(list)
