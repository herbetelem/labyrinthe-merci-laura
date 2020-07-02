
from pynput import keyboard
import printMap as pMap
import moove as moove
import win as win
import variables
import os
clear = lambda: os.system('cls')


def press(action):
    if action == "z" or action == "q" or action == "s" or action == "d":
        if moove.checkMoove(action, variables.positionY, variables.positionX):
            mouvement = moove.moove(action, variables.positionY, variables.positionX)
            variables.positionY = mouvement[0]
            variables.positionX = mouvement[1]
            clear()
            pMap.printTitre()
            pMap.printLab(variables.positionY, variables.positionX)
            if variables.positionY == 0 and variables.positionX == 24:
                win.win()
        else:
            print("Vous ne pouvez pas traverser les murs")
    else:
        print("ZQSD uniquement merci")

def on_press(key):
    try:
        press(key.char)
    except AttributeError:
        print("ZQSD uniquement merci")


def Main():
    clear()
    pMap.printTitre()
    pMap.printLab(variables.positionY, variables.positionX)

if __name__ == "__main__":
    Main()


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()