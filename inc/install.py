import os
import subprocess
import yaml
import shutil
import wget
from pysteamcmdwrapper import SteamCMD


yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)

LOGIN = yaml_conf_content['steamCMD']['login']

PWD = yaml_conf_content['steamCMD']['password']
SERVER_DIR = yaml_conf_content['game']['game_dir']

WORKSHOP_DIR = os.path.join(os.getcwd(),SERVER_DIR,"armamods","steamapps","workshop","content","107410")
MOD_DIR = os.path.join(os.getcwd(),SERVER_DIR)

GAME_ID = yaml_conf_content['game']['game_id']

def install():
     #DOWNLOAD AND INSTALL GAME
    try:
        s.login(LOGIN, PWD)
        s.app_update(GAME_ID,os.path.join(os.getcwd(),SERVER_DIR),validate=True)
    except:
        print('Game server is already installed')


    # MAP INSTALLER

    MAPS = yaml_conf_content['game']['game_maps']
    MPMISSIONS = os.path.join(os.getcwd(),SERVER_DIR,'mpmissions')

    try:
        for map in MAPS:
            print("Downloading Maps :")
            print(map)
            wget.download(map, MPMISSIONS)
    except:
        print("Maps already installed")
