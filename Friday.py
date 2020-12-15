import pyttsx3
import webbrowser
import smtplib,ssl 
import random
import speech_recognition as sr
from time import ctime
import wikipedia
import datetime
import wolframalpha
import os
import sys
from playsound import playsound
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes


engine = pyttsx3.init()

client = wolframalpha.Client(' 2RX228-KWEXT6PLTT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print("Friday:" + audio)
    engine.say(audio)
    engine.runAndWait()

def greetme():
    print('Friday : Hello' + ' Arnav')
    print('Friday : Say your command')

greetme()

def greetme2():
    speak("Anything else??")

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:/Screenshots")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )   

def jokes():
    speak(pyjokes.get_joke())


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        playsound('Assistant.mp3')

        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        speak("ok...")
        print('You : ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry boss! I didn\'t get that! Try typing!')
        query = str(input("Type Here : "))

    return query

def sendEmail():
    speak("Please enter the following credentials")
    sender_email = "thefridayassistant@gmail.com"
    rec_email = input(str("Email:"))
    password = 'uwantit??'
    message = ('I am friday here is your email: ' + ' Hello ,' + rec_email )


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()   
    server.login(sender_email, password)
    speak('I logged in !')
    server.sendmail(sender_email, rec_email, message)
    print('email sent sucessfully to ' + rec_email)

        
if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            sys.exit()

        elif 'open google' in query:
            webbrowser.open('www.google.co.in')
            sys.exit()

        elif 'say this' in query:
            speak("what should i say?")
            this = myCommand
            speak(this)

        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')
            sys.exit()

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            try:
                sendEmail()
                say("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')

        elif 'search google' in query:
            print("What should i search ?")
            chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            search = myCommand()
            webbrowser.get(chromepath).open_new_tab('https://www.google.com/search?q=' + search)        

        elif 'email me' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')
        

                
        elif 'email my father' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')

        elif 'email to' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')       

        elif 'nothing' in query or 'abort' in query or 'stop' or 'get the hell out of here' or 'no thanks' in query:
            playsound('bye bye.mp3')
            sys.exit()

        elif "you are mad " in query:
            speak ('sorry boss will not do it again,perhaps never')   

        elif "what is the time" in query:
            speak("the time is:")
            speak(ctime())

        elif 'hello' in query:
            speak('Hello boss')

        elif 'bye' in query:
            speak('Bye Arnav, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            speak('Here is your music! Enjoy!')
            webbrowser.open('https://music.amazon.in/my/playlists/Fav/73669e57-3261-4f56-a694-d9e513124650')
            sys.exit()    
            
        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on boss, I will show you where " + location + " is.")
            url = 'https://www.google.nl/maps/place/' + location + "/&amp;"
            webbrowser.open(url)
            sys.exit()    

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Any thing else?' + 'Arnav')
        
