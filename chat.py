import datetime
import pyttsx3
import random
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    
    elif hour>=12 and hour<17:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    
    elif hour>=17 and hour<=20:
        print("Good Evening Sir")
        speak("Good Evening Sir")
    
    else:
        print("Good Night Sir")
        speak("Good Night Sir")
    
    print("I am your Chat bot can we talk?")
    speak("I am your Chat bot can we talk?")

def takeAnswer():
    userAnswer = input("Type anything.....")
    try:
        print("Typing.....")
        query = userAnswer
    except:
        print("I am sorry I don't understand what you have write.")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeAnswer().lower()

        if "no" in query:
            print("Ok sir we talk later")
            speak("Ok sir we talk later")
            break

        elif "hi" in query:
            print("Hello Sir")
            speak("Hello Sir")
        
        elif "how are you" in query:
            print("I am fine sir thank you for asking me and how are you?")
            speak("I am fine sir thank you for asking me and how are you?")
        
        elif "i am fine" in query:
            print("I wish for your good health.")
            speak("I wish for your good health.")
        
        elif "what is your name" in query:
            print("My name is David")
            speak("My name is David")
        
        elif "when your birthday is come" in query:
            print("21st March")
            speak("21st March")
        
        elif "when my birthday is come" in query:
            print("26th June")
            speak("26th June")
        
        elif "hello" in query:
            lst = ["Hello sir", "Namaste sir, I am doing well sir."]
            try:
                rand = random.randint(0,len(lst)-1)
                print(lst[rand])
                speak(lst[rand])
            except:
                pass
        
        elif "play music" in query:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            musicNumber = random.randint(0,len(songs))  
            os.startfile(os.path.join(music_dir, songs[musicNumber]))
            print("playing music "+ songs[musicNumber])
            speak("playing music "+ songs[musicNumber])
        
        elif "play online music" in query:
            webbrowser.open("music.youtube.com")
            print("playing some music on YouTube music")
            speak("playing some music on YouTube music")
        
        elif "quit" in query:
            print("Thank you sir for talking with me")
            speak("Thank you sir for talking with me")
            break