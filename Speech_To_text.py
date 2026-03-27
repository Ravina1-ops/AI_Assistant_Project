import sounddevice as sd
import speech_recognition as sr
import numpy as np

r = sr.Recognizer()

# Record 5 seconds of audio from mic
duration = 5  # seconds
print("Recording...")
audio_data = sd.rec(int(duration * 16000), samplerate=16000, channels=1, dtype='int16')
sd.wait()
print("Recording complete.")

# Convert to AudioData for SpeechRecognition
audio_bytes = audio_data.tobytes()
audio = sr.AudioData(audio_bytes, 16000, 2)

# Recognize speech
try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I could not understand.")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
