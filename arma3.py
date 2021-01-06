import os
import subprocess
import yaml
import shutil
from pysteamcmdwrapper import SteamCMD

###########################################
# VARS
###########################################

yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)

STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']

SERVER_DIR = yaml_conf_content['game']['game_dir']
WORKSHOP_DIR = os.path.join(os.getcwd(),"armamods","steamapps","workshop","content","107410")
MOD_DIR = os.path.join(os.getcwd(),SERVER_DIR)

GAME_ID = yaml_conf_content['game']['game_id']

LOGIN = yaml_conf_content['steamCMD']['login']
PWD = yaml_conf_content['steamCMD']['password']

###########################################
# FONCTIONS
###########################################
def install():
     #DOWNLOAD AND INSTALL GAME
    try:
        s.login(LOGIN, PWD)
        s.app_update(GAME_ID,os.path.join(os.getcwd(),SERVER_DIR),validate=True)
    except:
        print('Game server is already installed')

def start():
    # LAUNCHING GAME
    root = os.getcwd()
    abs_path = os.path.join(root,SERVER_DIR,"arma3server.exe")
    subprocess.Popen([abs_path])

def uninstall():
    try:
        shutil.rmtree(STEAMCMD_DIR)
        print("SteamCMD Directory is deleted")
    except OSError as e:
        print("Error: %s : %s" % (STEAMCMD_DIR, e.strerror))

    try:
        shutil.rmtree(SERVER_DIR)
        print("SteamCMD Directory is deleted")
    except OSError as e:
        print("Error: %s : %s" % (SERVER_DIR, e.strerror))

###########################################
# SCRIPT
###########################################

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

uninstall()