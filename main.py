from utils.listen import listen_mic
from utils.personalData import data_assist
from commands.index import commands_bot
#from commands.tocarMusica import tocar
from utils.speak import speak_text
import keyboard

dev = data_assist.get('creator')
name = data_assist.get('name')
nation = data_assist.get('nationality')

def virtual_assistant():
    while True:
        if keyboard.is_pressed('esc'):
            break
        if keyboard.is_pressed('space'):
            text = listen_mic()
            print(text)
              
virtual_assistant()













# def virtual_assistant():
#     if not data.get("name").lower() in prompt.lower():  # type: ignore
#         print(f'{data.get("name")} não foi citada na frase')
#         return
#     comm = prompt.replace(data.get("name"), "")  # type: ignore
#     commands_bot(comm)
