
"""""
Mamba AI ,my personalised pc ai module 
author: Sayan

"""""

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak(" good morning !")

    elif hour>=12 and hour<18:
        speak(" good afternoon !")

    else:
        speak("good evening !")
    speak("Hi Boss! This is Mamba , how can I help you ")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your password') #I have made the model ,enter your own email you want to use
    server.sendmail('your eamil',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:


        query=takeCommand().lower()
#Logics for all the next ai actions

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'play music' in query:
            music_dir='F:\\Downloads\\La Musique'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Boss, the time is {strTime}")

        elif 'open pycharm' in query:
            codePath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.5\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to Tony' in query:
            try:
                speak("What should I send Boss?")
                content=takeCommand()
                to="captainstark.03@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:

                print(e)
                speak(" Sorry Boss! I am not able to send this email")

            if 'quit' in query:
                exit()