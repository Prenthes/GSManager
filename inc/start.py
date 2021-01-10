import os
import subprocess
import yaml
import shutil
import wget
from pysteamcmdwrapper import SteamCMD

yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)
SERVER_DIR = yaml_conf_content['game']['game_dir']

def start():
    # LAUNCHING GAME
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
