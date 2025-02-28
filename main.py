import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import os

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio) 
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + " Hours and " + min + " Minutes") 

def Hello():
    speak("Hello! How may I help you")

def searchYouTube(query):
    webbrowser.open("https://www.youtube.com/results?search_query=" + query)

def openApplication(appName):
    if appName == "notepad":
        os.system("notepad.exe")
    elif appName == "calculator":
        os.system("calc.exe")

def Take_query():
    Hello()
    while(True):
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("www.youtube.com")
            continue
        
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
            
        elif "which day it is" in query:
            tellDay()
            continue
        
        elif "tell me the time" in query:
            tellTime()
            continue

        elif "open notepad" in query:
            speak("Opening Notepad")
            openApplication("notepad")
            continue

        elif "open calculator" in query:
            speak("Opening Calculator")
            openApplication("calculator")
            continue

        elif "bye" in query:
            speak("Bye. Have a nice day!")
            exit()
        
        elif "tell me your name" in query:
            speak("I am Jarvis, your desktop assistant")

        elif "search youtube" in query:
            query = query.replace("search youtube", "")
            searchYouTube(query)
            continue

if __name__ == '__main__':
    Take_query()
