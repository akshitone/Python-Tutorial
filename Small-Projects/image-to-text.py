import pytesseract
import pyttsx3
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def convert():
    img = Image.open('gr10_lev5_lrg.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

    # TEXT TO SPEECH
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


convert()
