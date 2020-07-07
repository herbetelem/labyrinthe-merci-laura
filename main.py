# Import toutes mes librairie / fonction
from pynput import keyboard
import random
import printMap as pMap
import moove as moove
import win as win
import variables
import os
clear = lambda: os.system('cls')

# fonction qui gere les mouvement
def press(action):
    #check si l'action est bien zqsd
    if action == "z" or action == "q" or action == "s" or action == "d":
        # check si le moove est possible
        if moove.checkMoove(action, variables.positionY, variables.positionX, variables.checkLab):

            #appel de la fonction pour chager la position de l'avatar et l'avatar lui même
            mouvement = moove.moove(action, variables.positionY, variables.positionX, variables.avatar)
            #recuperer les tuples
            variables.positionY = mouvement[0]
            variables.positionX = mouvement[1]
            variables.avatar = mouvement[2]
            #comme dans le main
            clear()
            pMap.printTitre()
            pMap.printLab(variables.positionY, variables.positionX, variables.lab, variables.avatar)
            #check si win
            if variables.positionY == 0 or variables.positionX == 0 or variables.positionY == (len(variables.lab) - 1) or variables.positionX == (len(variables.lab[0]) - 1):
                win.win()
        else:
            print("Vous ne pouvez pas traverser les murs")
    else:
        print("ZQSD uniquement merci")

#fonctin qui est appeler a chaque touches
def on_press(key):
    #si la touche est une touche standard
    try:
        #j'apelle la fonctin press avec en param la touche utiliser
        press(key.char)
    #si la touche n'est pas standard
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
        

#fonction main
def Main():
    #clear la map
    clear()
    #choix de la map 1 ou 2
    pMap.randomMap(random.randint(1, 2))
    #print le titre
    pMap.printTitre()
    #print le laby
    pMap.printLab(variables.positionY, variables.positionX, variables.lab, variables.avatar)

#main fonction propre
if __name__ == "__main__":
    Main()

# le bloc de pynput
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
