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
STEAMCMD_DIR = yaml_conf_content['steamCMD']['steamCMD_dir']

def install():
     #DOWNLOAD AND INSTALL GAME
    try:
        s = SteamCMD(STEAMCMD_DIR)
        s.login(LOGIN, PWD)
        s.app_update(GAME_ID,os.path.join(os.getcwd(),SERVER_DIR),validate=True)
    except:
        print('Game server installation error')


    # MAP INSTALLER

    MAPS = yaml_conf_content['game']['game_maps']
    MPMISSIONS = os.path.join(os.getcwd(),SERVER_DIR,'mpmissions')

    try:
        for map in MAPS:
            print("Downloading Maps :")
            print(map)
            wget.download(map, MPMISSIONS)
    except:
        print("Maps installation error")

    # MOD INSTALLER

    MODS = yaml_conf_content['game']['game_mods']
    
    try:
        for mod, mod_id in MODS.items():
            s.workshop_update(107410,mod_id,os.path.join(os.getcwd(),MOD_DIR),validate=True)
            os.symlink(os.path.join(WORKSHOP_DIR, str(mod_id)),os.path.join(MOD_DIR,"@"+mod))
    except:
        print("Mod Installation Error")
    
    try:
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

    except:
        print("conf.cfg error")