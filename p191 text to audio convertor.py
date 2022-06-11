import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
engine = pyttsx3.init()
text=""

while text!="no":
    print("please talk and NO to stop")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=5)
        text=r.recognize_google(audio_data)

        engine.connect(text)

        engine.say("text")