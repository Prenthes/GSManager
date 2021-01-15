import yaml
import os

def read_conf(file):
    yaml_conf_file = open(file, 'r')
    return yaml.safe_load(yaml_conf_file)