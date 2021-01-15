import os

def stop(GAME_EXE):
    CMD = str("taskkill /F /IM ") + str(GAME_EXE)
    try:
        os.system(CMD)
    except:
       print("Le serveur n'est pas lancé")