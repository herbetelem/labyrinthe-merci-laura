
from pynput import keyboard
import printMap as pMap
import moove as moove
import os
clear = lambda: os.system('cls')


def press(action):
    global positionX
    global positionY
    if action == "z" or action == "q" or action == "s" or action == "d":
        if moove.checkMoove(action, positionY, positionX):
            mouvement = moove.moove(action, positionY, positionX)
            positionY = mouvement[0]
            positionX = mouvement[1]
            clear()
            pMap.printLab(positionY, positionX)
            print(f"Y {positionY}, X {positionX}")
        else:
            print("Vous ne pouvez pas traverser les murs")
    else:
        print("ZQSD uniquement merci")

def on_press(key):
    try:
        press(key.char)
    except AttributeError:
        print("ZQSD uniquement merci")



positionY = 1
positionX = 1
pMap.printLab(positionY, positionX)
statutParti = "ok"
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()