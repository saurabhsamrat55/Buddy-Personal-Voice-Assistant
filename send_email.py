import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import filedialog
import base64
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
import mimetypes

# If modifying these scopes, delete the file token.pickle1.
SCOPES = ['https://mail.google.com/']
str = ""

def send_email():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle1 stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle1'):
        with open('token.pickle1', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials1.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle1', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('message ID: {}'.format(message['id']))
        return message
    except Exception as e:
        print('an error occured: {}'.format(e))
        return None 
def create_message(sender, to, subject, body):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)
    raw_msg = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
    return {'raw': raw_msg.decode('utf-8')}



def create_message_with_attachment(sender, to, subject, body, file):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)
    (content_type, encoding) = mimetypes.guess_type(file)

    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'

    (main_type, sub_type) = content_type.split('/', 1)

    if main_type == "text":
        with open(file, 'rb') as f:
            msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

    elif main_type == 'image':
        with open(file, 'rb') as f:
            msg = MIMEImage(f.read(), _subtype = sub_type)

    elif main_type == 'audio':
        with open(file, 'rb') as f:
            msg = MIMEAudio(f.read(), _subtype = sub_type)

    else:
        with open(file, 'rb') as f:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(f.read())

    filename = os.path.basename(file)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)
    raw_msg = base64.urlsafe_b64encode(message.as_string().encode('utf-8'))

    return {'raw': raw_msg.decode('utf-8')}


if __name__ == '__main__':
    service = send_email()
    user_id = 'me'
    sender = 'me'
    to = input("Sender's E-mail Address :- ")
    subject = input("What is the Subject :- ")
    body = input("What is the message :- ")

    file_attach = input("Do You Want to Attach File ? (Y/N)")

    if 'Y' in file_attach:
        file = filedialog.askopenfilename()
        msg = create_message_with_attachment(sender, to, subject, body, file)
        send_message(service, user_id, msg)

    else:
        msg = create_message(sender, to, subject, body)
        send_message(service, user_id, msg)
