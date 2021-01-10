import os
import sys
import yaml
import wget
from pysteamcmdwrapper import SteamCMD
import sys

yaml_conf_file = open("conf.yml", 'r')
yaml_conf_content = yaml.safe_load(yaml_conf_file)


print(MODLIST)