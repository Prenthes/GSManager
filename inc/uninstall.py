import os
import sys
import yaml
import shutil

def uninstall(STEAMCMD_DIR, SERVER_DIR):

    try:
        shutil.rmtree(STEAMCMD_DIR)
        print("SteamCMD Directory is deleted")
    except OSError as e:
        print("Error: %s : %s" % (STEAMCMD_DIR, e.strerror))

    try:
        shutil.rmtree(SERVER_DIR)
        print("Game Directory is deleted")
    except OSError as e:
        print("Error: %s : %s" % (SERVER_DIR, e.strerror))