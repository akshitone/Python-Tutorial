import speech_recognition as sr


def get_audio():
    req = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something..!!')
        audio = req.listen(source)
        print('Done!')

    try:
        text = req.recognize_google(audio)
        print('you said... ', text)

    except Exception as e:
        print(e)


get_audio()
