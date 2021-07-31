#This Program is made with the help of wolframalpha.
__author__      = "Adelin"
__copyright__   = "Copyright Adelinn112"



import wolframalpha
client = wolframalpha.Client("8A2LWL-6GK3TVAWHG")

import wikipedia

import PySimpleGUI as sg
sg.theme('DarkGrey3')
sg.set_options(font=('Courier New', 20))
layout =[[sg.Text('Enter a question'), sg.InputText()],[sg.Button('Enter'), sg.Button('Exit')]]
window = sg.Window('AI Assistant', layout)

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello,The Answer is:")
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Answer: "+wolfram_res,"Wikipedia Answer: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

window.close()
