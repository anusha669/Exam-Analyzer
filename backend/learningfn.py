import pymongo
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db3"]
mycol = mydb["maths"]



#content to audiobook
def audiobook():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    for x in mycol.find({},{ "_id": 0, "content":1 }):
        speak(x)
        
audiobook()
#content display
def displaycontent():
    for x in mycol.find({},{ "_id": 0, "content":1 }):
        print(x)

displaycontent()