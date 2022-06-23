from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
from buddy import *
from voice_mode import *
from read_email import *
from send_email import *
import tkinter as tk
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
saved_username = ["you"]
ans=["Buddy"]
window_size="550x450"

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


def wish():
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour < 12:
        speak('Good morning.')
    elif 12 <= hour < 18:
        speak('Good afternoon.')
    else:
        speak('Good evening.')




class ChatInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        speak("Welcome Back")
        wish()
        speak("Buddy at Your Service. How May i Help You Today?")


        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
    # Menu bar

    # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
       # file.add_command(label="Save Chat Log", command=self.save_chat)
        file.add_command(label="Clear Chat", command=self.clear_chat)
      #  file.add_separator()
        file.add_command(label="Exit",command=self.chatexit)

    # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

        # username

        # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default",command=self.font_change_default)
        font.add_command(label="Times",command=self.font_change_times)
        font.add_command(label="System",command=self.font_change_system)
        font.add_command(label="Helvetica",command=self.font_change_helvetica)
        font.add_command(label="Fixedsys",command=self.font_change_fixedsys)

        # color theme
        color_theme = Menu(options, tearoff=0)
        options.add_cascade(label="Color Theme", menu=color_theme)
        color_theme.add_command(label="Default",command=self.color_theme_default) 
       # color_theme.add_command(label="Night",command=self.) 
        color_theme.add_command(label="Grey",command=self.color_theme_grey) 
        color_theme.add_command(label="Blue",command=self.color_theme_dark_blue) 
       
        color_theme.add_command(label="Torque",command=self.color_theme_turquoise)
        color_theme.add_command(label="Hacker",command=self.color_theme_hacker)
       # color_theme.add_command(label='Mkbhd',command=self.MKBHD)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        #help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About", command=self.msg)
        help_option.add_command(label="Features", command=self.feature)
        help_option.add_command(label="Developers", command=self.about)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1,)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)


        def buttonClick():
            mixer.init()
            mixer.music.load("C:\\Users\\Rajan Kumar Sah\\Desktop\\Project_File\\music\\tone.mp3")
            mixer.music.play()
            query = takecommand().lower()
            pr1 = "You : " + query + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr1)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            #t1 = threading.Thread(target=self.playResponce, args=(query,))
            #t1.start()
            #time.sleep(0)

            if 'wikipedia' in query:
                speak("Searching...")
                query=query.replace('wikipedia','')
                result=wikipedia.summary(query,sentences=3)
                speak('According to Wikipedia')
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()

            elif 'time' in query:
                result = datetime.datetime.now().strftime("%I:%M:%S")
                speak("The current time is")
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
            elif 'email messages' in query:
                #view_message()
                pass

            elif 'send email' in query:
                pass

            elif 'voice mode' in query  or 'voice command' in query:
                main()

            elif 'on youtube' in query:
                query =query.replace('on youtube','') 
                if 'search' in query:
                    query = query.replace('search','') 
                    speak("Searching...")
                    wb.open('https://www.youtube.com/results?search_query='+query)
                if True:
                    result = "Search completed"
                    pr="Buddy : " + result + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(1)
                    t2 = threading.Thread(target=self.playResponce, args=(result,))
                    t2.start()
                    time.sleep(3) 

            elif 'search' in query:
                query = query.replace('search','')
                speak("Searching...")
                wb.open('https://www.google.com/search?q='+query)
                if True:
                    result = "Search Completed"
                    pr="Buddy : " + result + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    t2 = threading.Thread(target=self.playResponce, args=(result,))
                    t2.start()
                    time.sleep(3) 

            elif 'cpu' in query:
                usage = str(psutil.cpu_percent())
                battery = psutil.sensors_battery()
                battery = str(battery.percent)
                pr="Buddy : CPU usage is at " + usage + " and Battery is "+battery+"%\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                result = "CPU usage is at " + usage + "and Battery is "+ battery +" %"
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()

            elif 'joke' in query:
                result = jokes.get_joke()
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(0)

            elif 'write a note' in query or 'make a note' in query:
                try:
                    speak("What should i write?")
                    checknet()
                    if checknet()== False:
                        speak("You are Offline, Please Connect Internet Connection For Voice Inraction...")
                    else:
                        mixer.init()
                        mixer.music.load('music/tone.mp3')
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
                    pr = "Buddy : Note = " + query1 + "\n"
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                except Exception as e:
                    speak("Something went wrong, Please Try Again...")

            elif 'show notes' in query or 'show note' in query:
                speak("Showing Notes...")
                file = open('notes.txt','r')
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, "Notes\n-------------------------\n")
                self.text_box.insert(END, file.read())
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))


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
                pr="Buddy : " + result + "\n"
                if 'bye' in query:
                    self.text_box.configure(state=NORMAL)
                    self.text_box.insert(END, pr)
                    self.text_box.configure(state=DISABLED)
                    self.text_box.see(END)
                    self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                    self.entry_field.delete(0,END)
                    time.sleep(0)
                    t2 = threading.Thread(target=self.playResponce, args=(result,))
                    t2.start()
                    time.sleep(3)
                exit()

            else:
                ob=chat(query)
                pr="Buddy : " + ob + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(ob,))
                t2.start()



        # send button
        self.send_button1 = Button(self.send_button_frame, text="Send", width=5, relief=GROOVE, bg='white',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button1.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)


        self.send_button = Button(self.send_button_frame, text = "Voice",width=5, relief=GROOVE, bg='white',
                                  bd=1, command=buttonClick,activebackground="#FFFFFF",
                                  activeforeground="#000000")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)



        self.last_sent_label(date="No messages sent.")
        #t2 = threading.Thread(target=self.send_message_insert(, name='t1')
        #t2.start()

    def playResponce(self,responce):
        x=pyttsx3.init()
        #print(responce)
        li = []
        if len(responce) > 100:
            if responce.find('--') == -1:
                b = responce.split('--')
                #print(b)
                 
        x.setProperty('rate',120)
        x.setProperty('volume',100)
        x.say(responce)
        x.runAndWait()
        #print("Played Successfully......")

    def last_sent_label(self, date):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("About Buddy" , 'Buddy is a Personal Voice Assistant Application based on Python Programming language\n\n It is an Intelligent Personal Assistant System Developed Under Final Year Major Project')
    def feature(self):
    	tkinter.messagebox.showinfo("Buddy Features" , 'Here are the some features of Buddy\n\n1. Conversation \n2. Open Programs  \n3. Google Search    \n4. Wikipedia Search    \n5. Play Music      \n6. Play Vedios       \n7. Locate Place      \n8. Read News       \n9. Weather Report    \n10. Medicine Detail    \n11. send email       \n12. read email     \n13. offline NLTK search     \n14. take picture    \n15. set reminder...etc   ')
    def about(self):
        tkinter.messagebox.showinfo("Buddy Developers","1.  Rajan Kumar Sah (16105117035)\n     rajankrlnjpit@gmail.com\n\n2.  Saurabh Samrat (17105117901)\n     saurabhsamrat2012@gmail.com\n\n3.  Vikas Kumar (16105117028)\n     depakpk100@gmail.com\n\n4.  Rubi Kumari (16105117024)\n     krubi1121@gmail.com\n\n5.   Anisha Kumari (16105117029)\n     anishalnjpit@gmail.com")
    def send_message_insert(self, message):
        user_input = self.entry_field.get()
        pr1 = "You : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        #t1 = threading.Thread(target=self.playResponce, args=(user_input,))
        #t1.start()
        #time.sleep(1)
        if 'voice mode' in user_input  or 'voice command' in user_input:
            main()

        elif 'wikipedia' in user_input:
            if checknet() == True:  
                speak("Searching...")
                query=user_input.replace('wikipedia','')
                result=wikipedia.summary(query,sentences=3)
                speak('According to Wikipedia')
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
            else:
                result = "You are offline please connect internet connection"
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(0)
        elif 'cpu' in user_input:
            usage = str(psutil.cpu_percent())
            battery = psutil.sensors_battery()
            battery = str(battery.percent)
            pr="Buddy : CPU usage is at " + usage + " and Battery is "+battery+"%\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            result = "CPU usage is at " + usage + "and Battery is "+ battery +" %"
            t2 = threading.Thread(target=self.playResponce, args=(result,))
            t2.start()

        elif 'joke' in user_input:
            result = jokes.get_joke()
            pr="Buddy : " + result + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)
            t2 = threading.Thread(target=self.playResponce, args=(result,))
            t2.start()
            time.sleep(0)
            
        elif 'time' in user_input:
            result = datetime.datetime.now().strftime("%I:%M:%S")
            speak("The current time is")
            pr="Buddy : " + result + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)
            t2 = threading.Thread(target=self.playResponce, args=(result,))
            t2.start()

        elif 'make a note' in user_input or 'write a note' in user_input:
            try:
                speak("What should i write?")
                checknet()
                if checknet()== False:
                    speak("You are Offline, Please Connect Internet Connection For Voice Inraction...")
                else:
                    mixer.init()
                    mixer.music.load("C:\\Users\\Rajan Kumar Sah\\Desktop\\Project_File\\music\\tone.mp3")
                    mixer.music.play()
                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        r.pause_threshold = 1
                        audio = r.listen(source)
                print("Recognizing...")
                query = r.recognize_google(audio,language="en-in")
                file = open('notes.txt','w')
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(":- ")
                file.write(query)
                file.write("\n")
                speak("Succesfully Done..")
                pr = "Buddy : Note = " + query + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            except Exception as e:
                speak("Something went wrong, Please Try Again...")

        elif 'show notes' in user_input or 'show note' in user_input:
            speak("Showing Notes...")
            file = open('notes.txt','r')
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, "Notes\n-------------------------\n")
            self.text_box.insert(END, file.read())
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))

        elif 'email messages' in user_input:
            if True:
                result = "How many messages do you want to see ?"
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(0)
            #view_message()
            pass

        elif 'send email' in user_input:
            pass

        elif 'on youtube' in user_input:
            user_input =user_input.replace('on youtube','') 
            if 'search' in user_input:
                user_input =user_input.replace('search','') 
            speak("Searching...")
            wb.open('https://www.youtube.com/results?search_query='+user_input)
            if True:
                result = "Search completed"
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(1)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(3) 

        elif 'search' in user_input:
            user_input = user_input.replace('search','')
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+user_input)
            if True:
                result = "Search Completed"
                pr="Buddy : " + result + "\n"
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(3) 

        elif 'notepad' in user_input:
            speak("Opening Notepad...")
            notepad = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(notepad)

        elif 'vlc' in user_input:
            speak("Opening VLC Player...")
            vlc = 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'
            os.startfile(vlc)

        elif 'media player' in user_input:
            speak("Opening Media Player...")
            wm = 'C:\\Program Files\\Windows Media Player\\wmplayer.exe'
            os.startfile(wm)

        elif 'sublime' in user_input:
            speak("Opening Sublime Editor...")
            sublime = 'C:\\Program Files\\Sublime Text 3\\subl.exe'
            os.startfile(sublime)

        elif 'mozila' in user_input:
            speak("Opening Mozila Firefox")
            mozila = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
            os.startfile(mozila)

        elif 'explorer' in user_input:
            speak("Opening Internet Explorer")
            explorer = 'C:\\Program Files\\Internet Explorer\\iexplore.exe'
            os.startfile(explorer)

        elif 'adobe reader' in user_input:
            speak("Opening Adobe Reader")
            adobe = 'C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe'
            os.startfile(adobe)

        elif 'code block' in user_input:
            speak("Opening Code Block Editor")
            codeblock = 'C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            os.startfile(codeblock)

        elif 'edit plus' in user_input:
            speak("Opening Edit Plus Editor")
            editplus = 'C:\\Program Files (x86)\\EditPlus\\editplus.exe'
            os.startfile(editplus)
                
        elif 'chrome' in user_input:
            speak("Opening Chrome Browser")
            chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome)

        elif 'browser' in user_input:
            speak("Opening Chrome Browser")
            chrome = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(chrome)

        elif 'typing' in user_input:
            speak("Opening Typing Master")
            typing = 'C:\\Program Files (x86)\\TypingMaster\\TypingMaster.exe'
            os.startfile(typing)

        elif 'word' in user_input:
            speak("Opening MS Word")
            word = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
            os.startfile(word)

        elif 'excel' in user_input:
            speak("Opening MS Excel")
            excel = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(excel)

        elif 'power point' in user_input:
            speak("Opening MS Power Point")
            Powerpoint = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE'
            os.startfile(Powerpoint)

        elif 'team viewer' in user_input:
            speak("Opening Team Viewer")
            teamviewer = 'C:\\Program Files (x86)\\TeamViewer\\TeamViewer.EXE'
            os.startfile(teamviewer)

        elif 'edge' in user_input:
            speak("Opening Edge Browser")
            edge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(edge)


        elif 'bye' in user_input:
            result = "Bye Bye"
            pr="Buddy : " + result + "\n"
            if 'bye' in user_input:
                self.text_box.configure(state=NORMAL)
                self.text_box.insert(END, pr)
                self.text_box.configure(state=DISABLED)
                self.text_box.see(END)
                self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
                self.entry_field.delete(0,END)
                time.sleep(0)
                t2 = threading.Thread(target=self.playResponce, args=(result,))
                t2.start()
                time.sleep(3)
            exit()

        else:
            ob=chat(user_input)
            pr="Buddy : " + ob + "\n"
            self.text_box.configure(state=NORMAL)
            self.text_box.insert(END, pr)
            self.text_box.configure(state=DISABLED)
            self.text_box.see(END)
            self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
            self.entry_field.delete(0,END)
            time.sleep(0)
            t2 = threading.Thread(target=self.playResponce, args=(ob,))
            t2.start()


    def font_change_default(self):
        self.text_box.config(font="Verdana 10")
        self.entry_field.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_times(self):
        self.text_box.config(font="Times")
        self.entry_field.config(font="Times")
        self.font = "Times"

    def font_change_system(self):
        self.text_box.config(font="System")
        self.entry_field.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.text_box.config(font="helvetica 10")
        self.entry_field.config(font="helvetica 10")
        self.font = "helvetica 10"

    def font_change_fixedsys(self):
        self.text_box.config(font="fixedsys")
        self.entry_field.config(font="fixedsys")
        self.font = "fixedsys"

    def color_theme_default(self):
        self.master.config(bg="#EEEEEE")
        self.text_frame.config(bg="#EEEEEE")
        self.entry_frame.config(bg="#EEEEEE")
        self.text_box.config(bg="#FFFFFF", fg="#000000")
        self.entry_field.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
        self.send_button_frame.config(bg="#EEEEEE")
        self.send_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.send_button1.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        #self.emoji_button.config(bg="#FFFFFF", fg="#000000", activebackground="#FFFFFF", activeforeground="#000000")
        self.sent_label.config(bg="#EEEEEE", fg="#000000")

        self.tl_bg = "#FFFFFF"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"

    # Dark
    def color_theme_dark(self):
        self.master.config(bg="#2a2b2d")
        self.text_frame.config(bg="#2a2b2d")
        self.text_box.config(bg="#212121", fg="#FFFFFF")
        self.entry_frame.config(bg="#2a2b2d")
        self.entry_field.config(bg="#212121", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#2a2b2d")
        self.send_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#212121", fg="#FFFFFF", activebackground="#212121", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#2a2b2d", fg="#FFFFFF")

        self.tl_bg = "#212121"
        self.tl_bg2 = "#2a2b2d"
        self.tl_fg = "#FFFFFF"

    # Grey
    def color_theme_grey(self):
        self.master.config(bg="#444444")
        self.text_frame.config(bg="#444444")
        self.text_box.config(bg="#4f4f4f", fg="#ffffff")
        self.entry_frame.config(bg="#444444")
        self.entry_field.config(bg="#4f4f4f", fg="#ffffff", insertbackground="#ffffff")
        self.send_button_frame.config(bg="#444444")
        self.send_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.send_button1.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        #self.emoji_button.config(bg="#4f4f4f", fg="#ffffff", activebackground="#4f4f4f", activeforeground="#ffffff")
        self.sent_label.config(bg="#444444", fg="#ffffff")

        self.tl_bg = "#4f4f4f"
        self.tl_bg2 = "#444444"
        self.tl_fg = "#ffffff"


    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"    

    # Blue
    def color_theme_dark_blue(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    # Torque
    def color_theme_turquoise(self):
        self.master.config(bg="#003333")
        self.text_frame.config(bg="#003333")
        self.text_box.config(bg="#669999", fg="#FFFFFF")
        self.entry_frame.config(bg="#003333")
        self.entry_field.config(bg="#669999", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#003333")
        self.send_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#669999", fg="#FFFFFF", activebackground="#669999", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#003333", fg="#FFFFFF")

        self.tl_bg = "#669999"
        self.tl_bg2 = "#003333"
        self.tl_fg = "#FFFFFF"

    # Hacker
    def color_theme_hacker(self):
        self.master.config(bg="#0F0F0F")
        self.text_frame.config(bg="#0F0F0F")
        self.entry_frame.config(bg="#0F0F0F")
        self.text_box.config(bg="#0F0F0F", fg="#33FF33")
        self.entry_field.config(bg="#0F0F0F", fg="#33FF33", insertbackground="#33FF33")
        self.send_button_frame.config(bg="#0F0F0F")
        self.send_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.send_button1.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#0F0F0F", fg="#33FF33")

        self.tl_bg = "#0F0F0F"
        self.tl_bg2 = "#0F0F0F"
        self.tl_fg = "#33FF33"


    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()    


root=Tk()


img=ImageTk.PhotoImage(Image.open ("C:\\Users\\Rajan Kumar Sah\\Desktop\\Project_File\\img\\buddy.png"))
lab=Label(image=img)
lab.pack()


a = ChatInterface(root)
root.geometry(window_size)
root.title("Buddy, Personal Assistant")
root.iconbitmap("C:\\Users\\Rajan Kumar Sah\\Desktop\\Project_File\\img\\buddy.ico")
root.mainloop()
