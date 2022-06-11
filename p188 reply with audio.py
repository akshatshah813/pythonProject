import speech_recognition as sr
from playsound import playsound
r=sr.Recognizer()
text=""

while text!="no":
    print("Please talk and say NO to STOP.")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=5)
        playsound('audio//getting it.mp3')
        text=r.recognize_google(audio_data)

        if text=="no":
            playsound('audio//bye.mp3')
            break
        elif text=="hello":
            playsound('audio//how are you.mp3')
            playsound('audio//how is your day.mp3')
        elif text=="i am having a bad day":
            playsound('audio//I am sorry to hear that.mp3')
        elif text=="bye":
            playsound('audio//bye.mp3')
