import os
import sys
import subprocess
import yaml
import shutil
import wget
from pysteamcmdwrapper import SteamCMD

from bs4 import BeautifulSoup
import requests
import sys

yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)

MODS = yaml_conf_content['game']['game_mods']
STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']
SERVER_DIR = yaml_conf_content['game']['game_dir']
WORKSHOP_DIR = os.path.join(os.getcwd(),SERVER_DIR,"armamods","steamapps","workshop","content","107410")
MOD_DIR = os.path.join(os.getcwd(),SERVER_DIR)


conf_cfg = open("conf.cfg", "w+")
yaml_conf = yaml_conf_content['conf']

conf_cfg.write('// Generated with Arma 3 Antistasi Python script \n')

for name, conf in yaml_conf.items():
    nameline = str(name)
    confline = str(conf)
    conf_cfg.writelines([nameline, " = ", confline, "; \n"])

conf_cfg.write('class Missions \n')
conf_cfg.write('{ \n')
conf_cfg.write('class Mission_1 \n')
conf_cfg.write('{ \n')
conf_cfg.writelines(['template =', str(yaml_conf_content['map']['selected']),";\n"])
conf_cfg.write('difficulty = "custom"; \n')
conf_cfg.write('}; \n')
conf_cfg.write('}; \n')

conf_cfg.close()
