import os
import sys
import subprocess
import yaml
import shutil
import wget
from pysteamcmdwrapper import SteamCMD
from inc.sys_check import req_check

def install(LOGIN, PWD, SERVER_DIR,WORKSHOP_DIR,MOD_DIR,GAME_ID,STEAMCMD_DIR, MAPS, MODS):
    
    #SYSTEM CHECK
    req_check()

    #CREATE GAME DIRECTORY
    try:
        os.mkdir(SERVER_DIR)
        print('Creating game folder')    
    except:
        print('Game folder exist')

    #DOWNLOAD AND INSTALL GAME
    try:
        s = SteamCMD(STEAMCMD_DIR)
        s.login(LOGIN, PWD)
        s.app_update(GAME_ID,os.path.join(os.getcwd(),SERVER_DIR),validate=True)
    except:
        print('Game server installation error')

    # MAP INSTALLER

    MPMISSIONS = os.path.join(os.getcwd(),SERVER_DIR,'mpmissions')

    try:
        for map in MAPS:
            print("Downloading Maps :")
            print(map)
            wget.download(map, MPMISSIONS)
    except:
        print("Maps installation error")

    # MOD INSTALLER

    try:
        for mod, mod_id in MODS.items():
            s.workshop_update(107410,mod_id,os.path.join(os.getcwd(),MOD_DIR),validate=True)
            os.symlink(os.path.join(WORKSHOP_DIR, str(mod_id)),os.path.join(MOD_DIR,"@"+mod))
    except:
        print("Mod Installation Error")
    
    try:
        conf_cfg = open("conf.cfg", "w+")
        yaml_conf = yaml_conf_content['conf']

        conf_cfg.write('// Generated with GSManager Python script \n')

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