from datetime import date
import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    # text = input("Enter text to speech: ")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f'the current time is {Time}')
    # print(Time)


time()
