import speech_recognition as sr


def speech_to_txt():
    r = sr.Recognizer()

    with sr.Microphone() as source:
     print("Speak something...")
     audio = r.listen(source)

    try:
        voice_data = ""
        voice_data = r.recognize_google(audio)
        print("You Said: ",voice_data)
        return voice_data 
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError:
        print("API error / No internet") 

