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

#LOADING CONF AND VARIABLE DECLARATION

function = sys.argv[1]
conf = sys.argv[2]
yaml_conf_content = read_conf(conf)

STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']
SERVER_DIR = yaml_conf_content['game']['game_dir']
LOGIN = yaml_conf_content['steamCMD']['login']
PWD = yaml_conf_content['steamCMD']['password']
WORKSHOP_DIR = os.path.join(os.getcwd(),SERVER_DIR,"armamods","steamapps","workshop","content","107410")
MOD_DIR = os.path.join(os.getcwd(),SERVER_DIR)
MODS = yaml_conf_content['game']['game_mods']
GAME_ID = yaml_conf_content['game']['game_id']
GAME_EXE = yaml_conf_content['game']['game_exe']
MAPS = yaml_conf_content['game']['game_maps']
MODS = yaml_conf_content['game']['game_mods']
PORT = yaml_conf_content['game']['game_port']

#INIT

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

# MAIN SCRIPT

if function == "install":
    install(LOGIN, PWD, SERVER_DIR,WORKSHOP_DIR,MOD_DIR,GAME_ID,STEAMCMD_DIR, MAPS, MODS)
elif function == "uninstall":
    uninstall(STEAMCMD_DIR, SERVER_DIR)
elif function == "start":
    start(SERVER_DIR, MODS, GAME_EXE, PORT)
elif function == "stop":
    stop(GAME_EXE)
else:
    print('Function unavalable, check documentation for further notice')