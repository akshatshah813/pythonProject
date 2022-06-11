import speech_recognition as sr
from playsound import playsound
import webbrowser
import pyttsx3
import time
engine = pyttsx3.init()
current=time.localtime(time.time())
r=sr.Recognizer()
text=""

while text!="stop":
    print("Please Speak and say STOP to Stop")
    with sr.Microphone() as source:
        audio_data=r.record(source,duration=5)
        playsound('dummy voice//yes.mp3')
        text=r.recognize_google(audio_data)
        print(text)
        if (text=="hey" or text=="hello"):
            engine.say("how can i assist you today?")
        elif text=="stop":
            engine.say("bye")
            print("bye")
            break
        elif text=="how are you":
            engine.say("i am fine, how are you")
        elif (text=="i am fine" or text=="fine" or text=="i am happy" or text=="great"):
            engine.say("good to hear that")
        elif (text=="i am sad" or text=="sad" or text=="i am not feeling good"):
            engine.say("i am sorry to hear that.")
            engine.say("do you want to hear a joke to cheer you up?")
            if (text=="yes" or text=="sure" or text=="yeah sure"):
                playsound('dummy voice//joke1.mp3')
            else:
                engine.say("okay")
        elif (text=="i am hungry" or text=="I'm hungry" or text=="hungry" or text=="i need food"):
            engine.say("lets eat something")
        elif (text=="i am angry" or text=="angry"):
            engine.say("i am sorry that something went wrong")
            engine.say("do you want to meditate to cool down")
            if (text == "yes" or text == "sure" or text=="yeah sure"):
                playsound('dummy voice//meditation.mp3')
            else:
                engine.say("okay")
        elif (text=="what is love"):
            playsound('dummy voice//love.mp3')
        elif (text=="thank you" or text=="thanks" or text=="thanks dummy" or text=="thank you dummy"):
            engine.say("you are welcome")
        elif (text=='who is your creator' or text=="Dummy who made you"):
            engine.say("my creator is akshat shah")
        elif (text=="who do you belong to" or text=="dummy who do you belong to"):
            engine.say("i belong to akshat shah")
        elif (text=="do you have any other name" or text=="do you have a nick name" or text=="do you have any nick name"):
            engine.say("no i do not have any other name")
        elif (text=="what are you" or text=="dummy what are you"):
            playsound('dummy voice//dummy intro.mp3')
        elif (text=="google" or text=="search on google"):
            engine.say("what would you like to search")
            if text=="":
                engine.say("Sorry i did not get that")
            else:
                url = "https://www.google.com/search?q=" +text
                webbrowser.open(url)
        elif (text=="time" or text=="current time" or text=="What is time" or text=="what is current time"):
            x = current.tm_hour
            y = current.tm_min
            if x == 13:
                z = x - 1
                time = (z, "o'clock", y, "minutes")
            elif x >= 14:
                z = x - 12
                time = (z, "o'clock", y, "minutes")
            engine.say(time)
        #elif (text=="today's day" or text=="what is today" or text=="which day is today"):


        engine.runAndWait()