import os
import sys
import subprocess
import yaml
from pysteamcmdwrapper import SteamCMD
from requests import get

def start(SERVER_DIR, MODS, GAME_EXE, PORT):

    # CHECKING IP ADRESS
    ip = get('https://api.ipify.org').text
    print('Your server is accessible from: {}'.format(ip))

    # LAUNCHING GAME
    root = str(os.getcwd())
    CONF = str("-config=conf.cfg")
    MODLIST = ["-mod="]
    for mod in MODS:
       mod = "@" + mod + ";"
       MODLIST.append(mod)
    MODLIST = ''.join(MODLIST)
    APP_LAUNCH = str(os.path.join(root,SERVER_DIR,str(GAME_EXE)))
    subprocess.run([APP_LAUNCH,CONF, MODLIST])


