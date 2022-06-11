import speech_recognition as sr
r=sr.Recognizer()
text=""

while text!="no":
    try:
        print("Please Talk and say NO to Stop.")
        with sr.Microphone() as source:
            audio_data=r.record(source,duration=3)
            print("Getting....")
            text=r.recognize_google(audio_data)
            if text=="no":
                print("Bye")
            else:
                if text.isnumeric():
                    a=int(text)
                    if a%2==0:
                        print(a,"is even")
                    else:
                        print(a,"is odd")
                else:
                    print("Sorry wrong input")
    except:
            print("Error in input")