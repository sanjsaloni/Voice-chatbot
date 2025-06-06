
import json
import pyttsx3 as pt
import speech_recognition as sr
# import test1 as t
import functionality as fun


engine = pt.init()
print(engine)
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
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
    print(data)
    if key in data:
        k = data[key]
        print(k)
        talk(data[key])
    else:
        talk("Please answer the question.")
        value = take_command()
        data[key] = value
        with open(file_path,'w') as f:
            json.dump(data,f)
    # print(data)


if __name__ == '__main__':
    filePath = "dict.json"
    print('Started')
    # key = input("Enter the string")
    key = take_command()
    print(key)
    add(filePath,key)
    # print(t.add_int(2,3))
