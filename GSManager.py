import os
import sys
import yaml
from pysteamcmdwrapper import SteamCMD
from inc.install import install
from inc.start import start
from inc.uninstall import uninstall
from inc.stop import stop
from inc.sys_check import req_check

yaml_conf_file = open(sys.argv[2], 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)

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

function = sys.argv[1]
conf = sys.argv[2]

if function == "install":
    install()
elif function == "uninstall":
    uninstall()
elif function == "start":
    start()
elif function == "stop":
    stop()
else:
    print('Function unavalable, check documentation for further notice')