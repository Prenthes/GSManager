import os
import sys
import yaml
import shutil



def uninstall():

    yaml_conf_file = open(sys.argv[2], 'r')
    yaml_conf_content = yaml.safe_load(yaml_conf_file)
    
    STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']
    SERVER_DIR = yaml_conf_content['game']['game_dir']
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