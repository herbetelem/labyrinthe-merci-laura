
from pynput import keyboard
import random
import printMap as pMap
import moove as moove
import win as win
import variables
import os
clear = lambda: os.system('cls')


def press(action):
    if action == "z" or action == "q" or action == "s" or action == "d":
        if moove.checkMoove(action, variables.positionY, variables.positionX, variables.checkLab):
            mouvement = moove.moove(action, variables.positionY, variables.positionX, variables.avatar)
            variables.positionY = mouvement[0]
            variables.positionX = mouvement[1]
            variables.avatar = mouvement[2]
            clear()
            pMap.printTitre()
            pMap.printLab(variables.positionY, variables.positionX, variables.lab, variables.avatar)
            if variables.positionY == variables.winY and variables.positionX == variables.winX:
                win.win()
        else:
            print("Vous ne pouvez pas traverser les murs")
    else:
        print("ZQSD uniquement merci")

def on_press(key):
    try:
        press(key.char)
    except AttributeError:
        if key == key.up:
            press("z")
        elif key == key.down:
            press("s")
        elif key == key.left:
            press("q")
        elif key == key.right:
            press("d")
        else:
            print("ZQSD uniquement merci")
        


def Main():
    clear()
    pMap.randomMap(random.randint(1, 2))
    pMap.printTitre()
    pMap.printLab(variables.positionY, variables.positionX, variables.lab, variables.avatar)

if __name__ == "__main__":
    Main()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()