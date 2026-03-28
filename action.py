import Text_to_Speech
import Speech_To_text
import datetime
import webbrowser
user_data = Speech_To_text.speech_to_txt()

if "What is Your name" in user_data:
    Text_to_Speech.text_to_speech("My name is  AI Boss")
    

elif "Hello" in user_data or "hye" in user_data:
    Text_to_Speech.text_to_speech("Hey , Ma'am How can i  help you")
    
elif "Greetings " in user_data:
    Text_to_Speech.text_to_speech("Good Morning ma'am")

elif "What is the time now" in user_data:
    current_time = datetime.datetime.now()
    Time = (str)(current_time) = "Hour: ", (str)(current_time.minute) = "Minute"
    Text_to_Speech.text_to_speech(Time)
    
elif "Shut down" in user_data or "Bye" in user_data:
    Text_to_Speech.text_to_speech("Okay ma'am")

elif "play music" in user_data:
    webbrowser.open("https://spotify.com/")
    Text_to_Speech.text_to_speech("Spotify.com is ready for your music ma'am")

elif " open Youtube" in user_data:
    webbrowser.open("https://youtube.com/")
    Text_to_Speech.text_to_speech("Youtube.com is ready for your work ma'am")

elif "open google" in user_data:
    webbrowser.open("https://google.com/")
    Text_to_Speech.text_to_speech("Google.com is ready for your search ma'am")

elif "open LinkedIn" in user_data:
    webbrowser.open("https://LinkedIn.com/")
    Text_to_Speech.text_to_speech("LinkedIn.com is ready for you ma'am")

else:
    Text_to_Speech.text_to_speech("Kuch samajh nhi aya mujhe.")