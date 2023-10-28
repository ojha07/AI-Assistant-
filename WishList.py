import datetime
import random
import player
import playsound
from jarvis import speak


def specialDay():
    if datetime.date(2022, 6, 26) == datetime.date.today():
        wishList = ["Happy birthday sir", playsound.playsound("BirthdaySong.mp3")]
        speak(random.Random(wishList))
        
    elif datetime.date(2022, 8, 19) == datetime.date.today():
        player.notification.notify(
            title="Ankita's Birthday",
            message="Wish them",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        # speak("Today is Ankita's birthday.")

    elif datetime.date(2022, 3, 18) == datetime.date.today():
        player.notification.notify(
            title="Today is Holy",
            message="Happy Holy",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Holli sir.")

    elif datetime.date(2022, 8, 15) == datetime.date.today():
        player.notification.notify(
            title="Independence Day",
            message="Happy Independence Day",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Independence Day sir")

    elif datetime.date(2021, 10, 15) == datetime.date.today():
        player.notification.notify(
            title="Dussehra",
            message="Happy Dussehra sir",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Dussehra sir")

    elif datetime.date(2021, 11, 4) == datetime.date.today():
        player.notification.notify(
            title="Diwali",
            message="Happy Diwali",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Diwali sir")

    elif datetime.date(2021, 11, 10) == datetime.date.today():
        player.notification.notify(
            title="Chhat Puja",
            message="Happy Chhat puja",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Chhat puja sir.")

    elif datetime.date(2022, 1, 26) == datetime.date.today():
        player.notification.notify(
            title="Republic Day",
            message="Happy Republic Day",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Republic day sir")

    elif datetime.date(2022, 4, 26) == datetime.date.today():
        player.notification.notify(
            title="Jarvis's Birthday",
            message="Today is Birthday of your Jarvis's AI.",
            app_icon="E:\Jarvis AI\icon.ico",
            timeout=5
        )
        speak("Happy Birthday to me")

    # elif datetime.date(2021, 6, 12) == datetime.date.today():
    #     playsound.playsound("BirthdaySong.mp3")
