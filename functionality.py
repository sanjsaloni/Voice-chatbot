import pywhatkit
import datetime
import input_output as io
import os
def youtube(text):
    video = text.replace('play','')
    io.talk('Playing'+video)
    pywhatkit.playonyt(video)

def time(t):
    t = datetime.datetime.now().strftime('%I:%M %p')
    print(t)
    io.talk('Current time is',t)

def open(t):
        pywhatkit.search(t)

def wishme(name):
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        io.talk('Good morning',name)
    elif hour>12 and hour<17:
        io.talk("Good afternoon",name)    
    else:
        io.talk('Good evening',name) 

def get_path(file):
     path = os.path.abspath(file)
     print(path)
    #  os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    
# get_path('test1.py')

