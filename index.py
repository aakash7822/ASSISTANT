import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except:
            return ""

sites = [
    ["Google", "https://www.google.com"],
    ["YouTube", "https://www.youtube.com"],
    ["Facebook", "https://www.facebook.com"],
    ["WhatsApp", "https://www.whatsapp.com"],
    ["Instagram", "https://www.instagram.com"],
    ["ChatGPT", "https://chat.openai.com"]
]

if __name__ == "__main__":
    speak("Hello, I am your assistant.")
    while True:
        print("Listening...")
        query = takeCommand().lower()

        # Open websites
        for site in sites:
            if f"open {site[0].lower()}" in query:
                speak(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

        # Tell time
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strfTime}")

        # Open VS Code
        if "open code" in query:
            speak("Opening Visual Studio Code")
            os.system(r'"C:\Users\mukes\AppData\Local\Programs\Microsoft VS Code\Code.exe"')


             # Open google chrome
        if "open chrome" in query:
            speak("Opening google chrome")
            os.system(r'"C:\Users\mukes\Desktop\Aayush (Person 1) - Chrome.lnk"')

            # open music using path
        if "open music" in query:
            musicpath = r"C:\Users\mukes\Downloads\midnight-whispers-lo-fi-background-music-for-video-stories-short-2-413329.mp3"
            os.startfile(musicpath)    


        
    
       

     




            