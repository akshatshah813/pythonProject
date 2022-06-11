import pyttsx3
engine = pyttsx3.init()
str1=input("Enter name ")
engine.say(str1)
engine.say("Thank you, Geeksforgeeks")
engine.runAndWait()