import os
import sys
import subprocess
import yaml
from pysteamcmdwrapper import SteamCMD
from requests import get

def start(yaml_conf_content):

    # LAUNCHING GAME
    SERVER_DIR = yaml_conf_content['game']['game_dir']
    root = str(os.getcwd())
    PORT = str(yaml_conf_content['game']['game_firewall'])
    CONF = str("-config=conf.cfg")
    MODS = yaml_conf_content['game']['game_mods']
    MODLIST = ["-mod="]
    for mod in MODS:
       mod = "@" + mod + ";"
       MODLIST.append(mod)
    MODLIST = ''.join(MODLIST)
    APP = "arma3server.exe"
    APP_LAUNCH = str(os.path.join(root,SERVER_DIR,str(APP)))
    START_CMD = (" -port=", PORT,' "-config=',CONF,'"',' "',"-mod=",MODLIST,'"')
    JOIN_START_CMD = ''.join(START_CMD)
    subprocess.run([APP_LAUNCH,CONF, MODLIST])

    # CHECKING IP ADRESS
#   ip = get('https://api.ipify.org').text
#   print('Your server is accessible from: {}'.format(ip))
