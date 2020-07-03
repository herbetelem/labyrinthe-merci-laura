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


def checkMoove(action, positionY, positionX, lab):
    
    if action == "z":
        positionY = positionY - 1
    elif action == "q":
        positionX = positionX - 1
    elif action == "s":
        positionY = positionY + 1
    elif action == "d":
        positionX = positionX + 1
    
    if lab[positionY][positionX] == 1:
        return True
    else:
        return False