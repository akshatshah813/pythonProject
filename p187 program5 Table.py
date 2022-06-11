import speech_recognition as sr
r=sr.Recognizer()
text=""

while text!="no":
    print("Please talk and say No to STOP")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=3)
        print("Getting it....")
        text=r.recognize_google(audio_data)

        if text.isnumeric():
            a=int(text)
            for i in range(1,11):
                print(a,"X",i,"=",a*i)
            else:
                print("Sorry wrong input")
