import speech_recognition as sr
r=sr.Recognizer()
text=""

while text!="no":
    print("Please TAlk and Say No to STOP")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=4)
        print("Getting...")
        text=r.recognize_google(audio_data)
        print(text,"--",len(text))

        if text=="hello":
            print("How are you?")
        elif text=="how are you":
            print("I am fine")
        elif text=="hungry":
            print("Let's eat something")
        elif text=="no":
            print("Bye")