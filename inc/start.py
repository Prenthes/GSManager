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
    root = os.getcwd()
    abs_path = os.path.join(root,SERVER_DIR,"arma3server.exe")
    subprocess.Popen([abs_path])