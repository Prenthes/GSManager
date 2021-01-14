import os
import sys
import yaml
from pysteamcmdwrapper import SteamCMD
from inc.GSMYml import read_conf
from inc.install import install
from inc.start import start
from inc.uninstall import uninstall
from inc.stop import stop
from inc.sys_check import req_check

function = sys.argv[1]
conf = sys.argv[2]
yaml_conf_content = read_conf(conf)

#TEST DES VARIABLES SI CONF EXISTE POURSUITE DU TEST

STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']
SERVER_DIR = yaml_conf_content['game']['game_dir']

# INIT
# CREATING STEAMCMD DIRECTORY
try:
    os.mkdir(STEAMCMD_DIR)
    print('Creating steamCMD directory')    
except:
    print('SteamCMD exist')

s = SteamCMD(STEAMCMD_DIR)

#INSTALLING STEAMCMD
try:
    s.install()
except:
    print("SteamCMD installed")

#CREATE GAME DIRECTORY
try:
    os.mkdir(SERVER_DIR)
    print('Creating game folder')    
except:
    print('Game folder exist')

# MAIN SCRIPT

if function == "install":
    install(yaml_conf_content)
elif function == "uninstall":
    uninstall(STEAMCMD_DIR, SERVER_DIR)
elif function == "start":
    start(yaml_conf_content)
elif function == "stop":
    stop(yaml_conf_content)
else:
    print('Function unavalable, check documentation for further notice')