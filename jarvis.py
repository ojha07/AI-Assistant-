import time
from pywikihow import search_wikihow
import bs4
import pyautogui as p
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import calendar
# import WishList
from requests import get
import pywhatkit as kit
# import sys
import calculator
# import cv2
# import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voice', voices[0].id)


# engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    e = datetime.datetime.now()
    currentTime = e.strftime("%I:%M %p")
    # print(currentTime)

    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak(f"Good morning sir.{currentTime}")

    elif 12 <= hour < 18:
        speak(f"Good afternoon sir. {currentTime}")

    elif 18 <= hour <= 20:
        speak(f"Good evening sir. {currentTime}")

    else:
        speak(f"Good night sir. {currentTime}")

    # WishList.specialDay()

    speak("I am Jarvis your Personal Assistant. How may I help you?")


def takeCmd():
    """
        It take microphone from the user to give command to the jarvis and return string output.
        """  # noqa: E501
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        # print(e)

        speak("I am sorry. Say that again please....")
        return "None"
    query = query.lower()
    return query


def TaskExecution():
    p.press('esc')
    # speak("Verification Successfully")
    # speak("Welcome back Satyam sir")
    wishMe()
    while True:
        # if 1:
        query = takeCmd()

        # logic to executing task based on query.
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            ipAdd = get("https://api.ipify.org").text
            print(ipAdd)
            try:
                url = requests.get('https://ipinfo.io/json').json()
                city = url['city']
                region = url['region']  # noqa: F841
                country = url['country']
                speak(f"Sir, I am not sure, but we are in {city} of {country}.")
            except Exception:
                speak("Sorry sir, due to network issue I am not able to find the location.")  # noqa: E501
                pass

        elif "take screenshot" in query:
            speak("Sir, please tell me the name for this screenshot file.")
            name = takeCmd().lower()
            speak("Please sir, hold the screen for few seconds, I am taking screenshot")
            time.sleep(3)
            img = p.screenshot()
            img.save(f"{name}.png")
            speak("I am done sir, the screenshot is saved in our main folder.")

        elif "do some calculation" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example 2 plus 2 ")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_str = r.recognize_google(audio)
            print(my_str)

            def get_op(op):
                return {
                    '+': calculator.Add,  # plus
                    '-': calculator.Sub,  # minus
                    'x': calculator.Multi,  # multiplied by
                    '/': calculator.Div,  # divided
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_op(oper)(op1, op2)

            speak(f"Your result is: {eval_binary_expr(*(my_str.split()))}")
            # speak()


        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            speak("Opening notepad fou you")

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("opening command prompt for you")

        elif "open youtube" in query:
            speak("Sir, What should I search on YouTube")
            cmd = takeCmd().lower()
            kit.playonyt(cmd)
            speak("Opening youtube")

        elif "play online music" in query:
            text = "Sir, Which song you want to listen"
            speak(text)
            scm = takeCmd().lower()
            kit.playonyt(scm)

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            ipAd = f"Your IP address is {ip}"
            speak(ipAd)

        elif "open microsoft edge" in query:
            googlePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application"
            speak("Sir, What should i search on edge")
            cm = takeCmd().lower()
            webbrowser.open(cm)
            speak("Opening microsoft browser")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")
            speak("Opening facebook")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")
            speak("Opening instagram")

        elif "play music" in query:
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            musicNumber = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[musicNumber]))
            speak("playing music" + songs[musicNumber])

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.date.today()
            speak(f"Sir, The date is {strDate}")

        elif "the day" in query:
            def findDay():
                day = datetime.date.today().weekday()
                return calendar.day_name[day]

            date = datetime.date.today()
            weekDay = findDay()
            print(f"{weekDay} Sir")
            speak(f"{weekDay} Sir")

        elif "open code" in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS Code")

        elif "open intell jdea" in query:
            intelljpath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.1.1\\bin\\idea64.exe"
            os.startfile(intelljpath)
            speak("Opening Intell JDEA")

        elif "open studio" in query:
            obsPath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obsPath)
            speak("Opening OBS Studio")

        elif "show me photo" in query:
            photoPath = "C:\\Users\\hp\\OneDrive\\Pictures\\pic"
            photo = os.listdir(photoPath)
            pic = random.randint(0, len(photo))
            os.startfile(os.path.join(photoPath, photo[pic]))
            speak("Opening photo")

        elif "temperature" in query or "weather" in query:
            search = "temperature in jabalpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = bs4.BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated please tell me what you want to know")
            how = takeCmd()
            max_result = 1
            how_to = search_wikihow(how, max_result)
            assert len(how_to) == 1
            # how_to[0].print()
            speak(how_to[0].summary)

        elif "volume up" in query:
            p.press("volumeup")

        elif "volume down" in query:
            p.press("volumedown")

        elif "volume mute" in query:
            p.press("volumemute")

        elif "volume unmute" in query:
            p.press("volumeunmute")


        elif "what is my date of birth" in query:
            speak("Sir your date of birth is 26 June")

        elif "when you launch" in query:
            speak("17 March 2021")

        elif "no thanks" in query:
            speak("It my pleasure sir.")

        elif "you can sleep jarvis" in query:
            speak("ok sir, I am going to sleep. You can call me any time.")
            break

        # elif "set timer" in query:

        #     speak("For how long I set the timer?")
        #     setTimer = takeCmd()
        #     intSetTime = int(setTimer*60)
        #     time.sleep(intSetTime)
        #     playsound.playsound("Alarm sound.mp3")



        speak("Sir, do you have any other work for me.....")

if __name__ == '__main__':
    wishMe()
    takeCmd()
    TaskExecution()


# if __name__ == '__main__':

#     recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
#     recognizer.read('trainer/trainer.yml')  # load trained model
#     cascadePath = "haarcascade_frontalface_default.xml"
#     faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

#     font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

#     id = 2  # number of persons you want to Recognize

#     names = ['', 'shristy']  # names, leave first empty bcz counter starts from 0

#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
#     cam.set(3, 640)  # set video FrameWidht
#     cam.set(4, 480)  # set video FrameHeight

#     # Define min window size to be recognized as a face
#     minW = 0.1 * cam.get(3)
#     minH = 0.1 * cam.get(4)

#     # flag = True

#     while True:

#         ret, img = cam.read()  # read the frames using the above created object

#         converted_image = cv2.cvtColor(img,
#                                        cv2.COLOR_BGR2GRAY)  # The function converts an input image from one color space to another

#         faces = faceCascade.detectMultiScale(
#             converted_image,
#             scaleFactor=1.2,
#             minNeighbors=5,
#             minSize=(int(minW), int(minH)),
#         )

#         for (x, y, w, h) in faces:

#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

#             id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])  # to predict on every single image

#             # Check if accuracy is less them 100 ==> "0" is perfect match
#             if accuracy < 100:
#                 id = names[id]
#                 accuracy = "  {0}%".format(round(100 - accuracy))
#                 TaskExecution()

#             else:
#                 id = "unknown"
#                 accuracy = "  {0}%".format(round(100 - accuracy))

#             cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#             cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

#         cv2.imshow('camera', img)

#         k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
#         if k == 27:
#             break

#         # Do a bit of cleanup
#         print("Thanks for using this program, have a good day.")
#         cam.release()
#         cv2.destroyAllWindows()
