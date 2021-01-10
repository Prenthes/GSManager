import os
import subprocess
import yaml
import shutil
import wget
from pysteamcmdwrapper import SteamCMD



def stop():
    try:
        os.system("taskkill /F /IM arma3server.exe")
    except:
        print("Le serveur n'est pas lancé")