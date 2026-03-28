import Text_to_Speech
import Speech_To_text
import datetime
import webbrowser

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
     Text_to_Speech.text_to_speech("My name is  AI Boss")
     return "My name is  AI Boss"

    elif "hello" in user_data or "hye" in user_data:
     Text_to_Speech.text_to_speech("Hey , Ma'am How can i  help you")
     return "Hey , Ma'am How can i  help you"
    
    elif "greetings" in user_data:
     Text_to_Speech.text_to_speech("Good Morning ma'am")
     return "Good Morning ma'am"
    
    elif "what is the time now" in user_data:
     current_time = datetime.datetime.now()
     Time = f"Hour: {current_time.hour} Minute: {current_time.minute:02d}"
     Text_to_Speech.text_to_speech(Time)
     return Time
    elif "shut down" in user_data or "Bye" in user_data:
     Text_to_Speech.text_to_speech("Okay ma'am")
     return  "Okay ma'am"

    elif "play music" in user_data:
     webbrowser.open("https://spotify.com/")
     Text_to_Speech.text_to_speech("Spotify.com is ready for your music ma'am")
     return "Spotify.com is ready for your music ma'am"
    
    elif "open youtube" in user_data:
     webbrowser.open("https://youtube.com/")
     Text_to_Speech.text_to_speech("Youtube.com is ready for your work ma'am")
     return "Youtube.com is ready for your work ma'am"

    elif "open google" in user_data:
     webbrowser.open("https://google.com/")
     Text_to_Speech.text_to_speech("Google.com is ready for your search ma'am")
     return "Google.com is ready for your search ma'am"

    elif "open linkedin" in user_data:
     webbrowser.open("https://LinkedIn.com/")
     Text_to_Speech.text_to_speech("LinkedIn.com is ready for you ma'am")
     return "LinkedIn.com is ready for you ma'am"

    else:
     Text_to_Speech.text_to_speech("I can't understand .")
     return "I can't understand ."