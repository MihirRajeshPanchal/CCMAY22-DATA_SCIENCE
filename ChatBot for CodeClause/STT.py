import speech_recognition as sr
import pyaudio 
from speech_recognition import *

def stt():
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=2) as source:
            # audio_text=r.adjust_for_ambient_noise(source,5)
            # audio=r.listen(source=source,phrase_time_limit=5)
            audio = r.listen(source)
            # using google speech recognition
            text = r.recognize_google(audio)
            print(text)
            return text
