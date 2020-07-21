import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# initaling the engine and proving it the voice of zira
engine = pyttsx3.init("sapi5")
#  voices = engine.getProperty('voices')
# engine.getProperty('voice',voices[1].id)

# writing our speak function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good Morning...sir")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon  sir")
    else:
        speak("Good Evening...sir")
    speak("I am Avni  How may i help you")

# wirting function for takling user input


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail', 'password')
    server.sendmail('mail', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        # takecommand()
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open my site' in query:
            webbrowser.open("idhrudhr.tk")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsappweb.com")

        elif "open github" in query:
            webbrowser.open("github.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "C:\\Users\\USER\\Desktop\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif "search for" in query:
            search_term = query.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} on google')

        elif "search on youtube" in query:
            speak("what do you want to search sir")
            query1 = takecommand().lower()
            url = f"https://www.youtube.com/results?search_query={query1}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {query1} on youtube')

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "email"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'quit' in query:
            speak("Bye Bye sir have a nice day")
            break
