from gtts import gTTS 
import pyttsx3  

def tts(text):
    # initialize Text-to-speech engine  
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty("rate", 178)
    engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here
    # convert this text to speech  
    engine.say(text)  
    # play the speech  
    engine.runAndWait()  