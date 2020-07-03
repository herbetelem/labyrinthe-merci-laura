
import variables

def printLab(y, x, lab, avatar):
    compteur1 = 0
    print()
    for index in lab:
        compteur2 = 0
        ligne = ""
        while compteur2 < len(lab[0]):
            if compteur1 == y and compteur2 == x:
                ligne = str(ligne) + avatar
            else:
                ligne = str(ligne) + str(lab[compteur1][compteur2])
            compteur2 = compteur2 + 1
        compteur1 = compteur1 + 1
        print(ligne)
    print()
    print()

def printTitre():
    print(" ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____  ____  ____ ")
    print("||L ||||e ||||       ||||L ||||a ||||b ||||y ||||r ||||i ||||n ||||t ||||h ||||e ||")
    print("||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||||__||||__||")
    print("|/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|")

def randomMap(choiceMap):
    if choiceMap == 1:
        variables.lab = variables.lab1
        variables.checkLab = variables.checkLab1
        variables.winY = 0
        variables.winX = 24
    else:
        variables.lab = variables.lab2
        variables.checkLab = variables.checkLab2
        variables.winY = 13
        variables.winX = 129



