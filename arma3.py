import os
from pysteamcmdwrapper import SteamCMD

#programmer script pour checker si pysteamcmd est installé
    #oui print pysteamcmd est installé pass
    #non installer via pip install pysteamcmd

# Création du repertoire steamCMD 
try:
    os.mkdir('steamCMD')
    print('Création du dossier steamCMD')    
except:
    print('Le dossier steamCMD existe déjà')

# Création du répertoire arma3

try:
    os.mkdir('arma_server')
    print('Création du dossier arma_server')    
except:
    print('Le dossier arma_server existe déjà')

# Installation de SteamCMD

steamcmd_path = os.path.join('steamCMD')
gameserver_path = os.path.join('arma_server')
s = SteamCMD("steamcmd")
try:
    s.install()
except:
    print("SteamCMD est déjà installé")

#Installation du serveur arma

try:
    s.login()
    s.app_update(233780,os.path.join(os.getcwd(),gameserver_path),validate=True)
except:
    print('Arma3Server déjà installé')