# import requests
# import json
from win10toast import ToastNotifier
import time


def update():
    text = "Hello I'm Akshit Mithaiwala"

    while True:
        toast = ToastNotifier()
        toast.show_toast("That's My Name", text, duration=20)
        # this message appears upto 20 secs
        time.sleep(60)
        # notification again occurs after every 1 hr


update()
