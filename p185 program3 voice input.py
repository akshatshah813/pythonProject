import speech_recognition as sr
r=sr.Recognizer()
text=""

dic1={"hello":"how are you","how are you":"what about you","angry":"No I am not","hungry":"Let's eat something","have a nice day":"same to you","no":"bye"}

while text!="no":
    print("Please talk and say NO to STOP.")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=4)
        print("Getting....")
        text=r.recognize_google(audio_data)
        if text in dic1:
            print(dic1[text])
        else:
            print("Sorry not in dic")
