import time
import pyautogui
import os
import tkinter as tk

# use to dynamic path
FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'screenshots')


def screenshot():
    filename = int(round(time.time() * 1000))
    filename = os.path.join(TEMPLATE_DIR, "{}.png".format(filename))
    time.sleep(1)
    # img = pyautogui.screenshot(f"{filename}.png")
    img = pyautogui.screenshot(filename)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Take Screenshot',
    command=screenshot
)
button.pack(side=tk.LEFT)

close = tk.Button(
    frame,
    text='Cancel',
    command=quit
)
close.pack(side=tk.RIGHT)

root.mainloop()
