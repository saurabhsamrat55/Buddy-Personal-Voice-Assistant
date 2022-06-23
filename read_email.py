from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)


def gmail():
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me',labelIds = ['INBOX']).execute()
    messages = results.gezt('messages', [])
    speak("How many messages do you want to see?")
    query = takecommand()

    if "15" in query:
        messages_count = 15
    elif "14" in query:
        messages_count = 14
    elif "13" in query:
        messages_count = 13
    elif "12" in query:
        messages_count = 12
    elif "11" in query:
        messages_count = 11
    elif "10" in query:
        messages_count = 10
    elif '9' in query:
        messages_count = 9
    elif '8' in query:
        messages_count = 8
    elif '7' in query:
        messages_count = 7
    elif '6' in query:
        messages_count = 6
    elif '5' in query:
        messages_count = 5
    elif '4' in query:
        messages_count = 4
    elif '3' in query:
        messages_count = 3
    elif '2' in query:
        messages_count = 2
    elif '1' in query:
        messages_count = 1
    else:
        speak("Not Understand You, So Default is 2")
        messages_count = 2

    if not messages:
        print("No messages Found")
    else:
        print("Messages:")
        for message in messages[:messages_count]:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
            speak(msg['snippet'])
            print("\n")
            time.sleep(2)

if __name__ == '__main__':
    main()
    gmail()