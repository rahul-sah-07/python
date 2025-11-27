# TEXT-TO-SPEECH TOOL

import pyttsx3
text = input("Enter the name of the song you wmnat to play:- ")

speaker = pyttsx3.init()
speaker.say({text})
speaker.runAndWait()

#2nd code

import pyttsx3

engine = pyttsx3.init()

text = "hi i am rahul kuma"
engine.say(text)

engine.runAndWait()
