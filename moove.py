#fonction qui vas modifier la position de mon avatar et le dessin de l'avatar
def moove(action, positionY, positionX, avatar):
    if action == "z":
        positionY = positionY - 1
        avatar = "▲"
    elif action == "q":
        positionX = positionX - 1
        avatar = "◄"
    elif action == "s":
        positionY = positionY + 1
        avatar = "▼"
    elif action == "d":
        positionX = positionX + 1
        avatar = "►"
    return positionY, positionX, avatar

#fonction qui vas verifier si le moove est possible
def checkMoove(action, positionY, positionX, lab):
    
    if action == "z":
        positionY = positionY - 1
    elif action == "q":
        positionX = positionX - 1
    elif action == "s":
        positionY = positionY + 1
    elif action == "d":
        positionX = positionX + 1
    #check dans mon tableau binaire si le deplacement est possible
    if lab[positionY][positionX] == 1:
        return True
    else:
        return False