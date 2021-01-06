import requests
import yaml
from bs4 import BeautifulSoup

yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.load(yaml_conf_file)

print (yaml_conf_content['game']['game_name'])

mods = yaml_conf_content['game']['game_mod']

for mod in mods:
 print(mod)

installdir = yaml_conf_content['steamCMD']['name']
print(installdir)