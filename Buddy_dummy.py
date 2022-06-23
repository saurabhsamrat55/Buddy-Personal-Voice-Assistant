# from read_email import *
# from send_email import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import socket

engine = pyttsx3.init()


def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def time():
	time1=datetime.datetime.now().strftime("%I:%M:%S")
	speak("The current time is")
	speak(time1)

def date():
	year =datetime.datetime.now().year
	month = datetime.datetime.now().month
	day = datetime.datetime.now().day
	speak("and the date is")
	speak(day)
	speak(month)
	speak(year)

def wish():
    speak("Welcome Back Sir!")
    time=  datetime.datetime.now().strftime("%I:%M:%S")
    year =datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date = (day+month+year)
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour <4 and hour >12:
        speak("Gooood Morning!")
    elif hour >=12 and hour <16:
        speak("Gooood Afternoon!")
    elif hour >=16 and hour <24:
        speak("Gooood Evening!")
    speak("Buddy at your service. Please tell me how can i help you today?")



def email(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()


def takecommand():
	def testconnection():
		try:
			socket.create_connection(('google.com',80))
			return True
		except OSError:
			return False
	if testconnection()== False:
		print("Sir, You are Offline, Please Connect Internet Connection For Voice Inraction...")
		speak("Sir, You are Offline, Please Connect Internet Connection For Voice Inraction...")
	else:
		r=sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			r.pause_threshold = 1
			
			audio = r.listen(source)

		try:
			print("Recognizing...")
			query = r.recognize_google(audio,language="en-in")

		except:
			print("Say that again please...")
			return "None"
		return query

if __name__ == "__main__":
	wish()
	while True:
		query = takecommand().lower()

		if 'time' in query:
			time()

		elif 'date' in query:
			date()

		elif 'wikipedia' in query:
			speak("Searching...")
			query=query.replace('wikipedia','')
			result=wikipedia.summary(query,sentences=3)
			speak('According to Wikipedia')
			print(result)
			speak(result)

		elif 'email messages' in query:
			view_message()

		elif 'send email' in query:
			send_email()
			speak("send email done")

		elif 'quit' in query:
			print("Good Bye!")
			speak("Good Bye!")
			exit()

		else:
			speak("I Don't Understand, Please Try Again...")


