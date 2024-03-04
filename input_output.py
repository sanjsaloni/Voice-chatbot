
import json
import pyttsx3 as pt
import speech_recognition as sr
# import test1 as t
import functionality as fun


engine = pt.init()
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',150)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source,timeout=12)
            print("Passed 1")
            command = listener.recognize_google(voice)
            return command
    except:
        print("didn't work")


def add(file_path,key):
    with open(file_path,'r') as f:
        data = json.load(f)
    
    if None == key or 'null'==key:
        talk("Could not hear you")
        # del key
    if "wish" in key:
        talk("Can i know your name?")
        # name = input("Enter the name: ")
        name = take_command()
        print(name)
        fun.wishme(name)
    # if key in data.keys(): #For unknown input stream!
        # talk(data[key])
    else:
        talk("Please answer the question.")
        value = take_command()
        data[key] = value
        with open(file_path,'w') as f:
            json.dump(data,f)
    print(data)


if __name__ in '__main__':
    filePath = "dict.json"
    print('Started')
    # key = input("Enter the string")
    key = take_command()
    print(key)
    add(filePath,key)
    # print(t.add_int(2,3))
