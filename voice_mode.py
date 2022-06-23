from pygame import mixer
from buddy import *
#from read_email import *
#from send_email import *
import psutil
import time
import jokes
import tkinter.messagebox
import pyttsx3
import threading
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import socket
import subprocess


engine = pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    checknet()
    if checknet()== False:
        speak("You are Offline, Please Connect Internet Connection For Voice Inraction...")
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
            speak("Don't Understand, Try Again")
            return "None"
        return query


def checknet():
    try:
       socket.create_connection(('google.com',80))
       return True
    except OSError:
        return False

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"reset":"\u001b[0m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


def main():
    os.system('cls')
    f  = open("C:\\Users\\Rajan Kumar Sah\\Desktop\\Project_File\\intro\\voice_intro.txt","r")
    ascii = "".join(f.readlines())
    print(colorText(ascii))
    speak("Voice Mode Activated...")
    checknet()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            try:
                speak("Searching...")
                query=query.replace('wikipedia','')
                result=wikipedia.summary(query,sentences=3)
                speak('According to Wikipedia')
                pr="Buddy : " + result + "\n"
                speak(result)
            except:
                speak("Not Found Correct Result..")

        elif 'time' in query:
            result = datetime.datetime.now().strftime("%I:%M:%S")
            speak("The current time is")
            pr="Buddy : " + result + "\n"
            speak(result)

        elif 'email messages' in query:
            #view_message()
            pass

        elif 'send email' in query:
            pass
        elif 'on youtube' in query:
            query =query.replace('on youtube','') 
            if 'search' in query:
                query = query.replace('search','') 
                speak("Searching...")
                wb.open('https://www.youtube.com/results?search_query='+query)
                speak("Search completed")

        elif 'search' in query:
            query = query.replace('search','')
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+query)
            speak("Search completed")

        elif 'cpu' in query:
            usage = str(psutil.cpu_percent())
            battery = psutil.sensors_battery()
            battery = str(battery.percent)
            result = "CPU usage is at " + usage + "and Battery is "+ battery +" %"
            speak(result)


        elif 'joke' in query:
            result = jokes.get_joke()
            speak(result)

        elif 'write a note' in query or 'make a note' in query:
            try:
                speak("What should i write?")
                checknet()
                if checknet()== False:
                    speak("You are Offline, Please Connect Internet Connection For Voice Inraction...")
                else:
                    mixer.init()
                    mixer.music.load('tone.mp3')
                    mixer.music.play()
                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        r.pause_threshold = 1
                        audio = r.listen(source)
                print("Recognizing...")
                query1 = r.recognize_google(audio,language="en-in")
                file = open('notes.txt','a')
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":- ")
                file.write(query1)
                file.write("\n")
                speak("Succesfully Done..")
            except Exception as e:
                speak("Something went wrong, Please Try Again...")

        elif 'show notes' in query or 'show note' in query:
            speak("Showing Notes...")
            file = open('notes.txt','r')
            speak(file.read())


        elif 'notepad' in query:
            speak("Opening Notepad...")
            notepad = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(notepad)

        elif 'vlc' in query:
            speak("Opening VLC Player...")
            vlc = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
            os.startfile(vlc)

        elif 'media player' in query:
            speak("Opening Media Player...")
            wm = 'C:\\Program Files\\Windows Media Player\\wmplayer.exe'
            os.startfile(wm)

        elif 'sublime' in query:
            speak("Opening Sublime Editor...")
            sublime = 'C:\\Program Files\\Sublime Text 3\\subl.exe'
            os.startfile(sublime)

        elif 'mozila' in query:
            speak("Opening Mozila Firefox")
            mozila = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            os.startfile(mozila)

        elif 'explorer' in query:
            speak("Opening Internet Explorer")
            explorer = 'C:\\Program Files\\Internet Explorer\\iexplore.exe'
            os.startfile(explorer)

        elif 'adobe reader' in query:
            speak("Opening Adobe Reader")
            adobe = 'C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe'
            os.startfile(adobe)

        elif 'code block' in query:
            speak("Opening Code Block Editor")
            codeblock = 'C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            os.startfile(codeblock)

        elif 'edit plus' in query:
            speak("Opening Edit Plus Editor")
            editplus = 'C:\\Program Files (x86)\\EditPlus\\editplus.exe'
            os.startfile(editplus)
            
        elif 'chrome' in query:
            speak("Opening Chrome Browser")
            chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome)

        elif 'browser' in query:
            speak("Opening Chrome Browser")
            chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome)

        elif 'typing' in query:
            speak("Opening Typing Master")
            typing = 'C:\\Program Files (x86)\\TypingMaster\\TypingMaster.exe'
            os.startfile(typing)

        elif 'word' in query:
            speak("Opening MS Word")
            word = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word)

        elif 'excel' in query:
            speak("Opening MS Excel")
            excel = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(excel)

        elif 'power point' in query:
            speak("Opening MS Power Point")
            Powerpoint = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(Powerpoint)

        elif 'team viewer' in query:
            speak("Opening Team Viewer")
            teamviewer = 'C:\\Program Files (x86)\\TeamViewer\\TeamViewer.EXE'
            os.startfile(teamviewer)

        elif 'edge' in query:
            speak("Opening Edge Browser")
            edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(edge)

        elif 'bye' in query:
            result = "Bye Bye"
            speak(result)
            exit()
        elif "stop" in query or "exit form voice" in query or "deactivate" in query:
            speak("Voice Mode deactivated..")
            break

        else:
            ob=chat(query)
            pr="Buddy : " + ob + "\n"
            speak(ob)

if __name__ == '__main__':
    main()