import pyttsx3 

def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate' , 170)
    engine.say(text)
    engine.runAndWait()

