import os
import sys
import yaml
import psutil
from psutil import virtual_memory
from math import *

def req_check():

    yaml_conf_file = open(sys.argv[2], 'r')
    yaml_conf_content = yaml.safe_load(yaml_conf_file)

    print('/////////////////// SYSTEM RECQUIREMENT CHECK ///////////////////')

    sys_check = 0

    # CHECKING MEMORY

    total_memory = virtual_memory()
    total_memory = floor((total_memory.total)/1000000000)
    req_memory = yaml_conf_content['requirements']['RAM']

    if total_memory < req_memory:
        print(total_memory, "Go memory detected, The server need at least", req_memory, "Go to run!")
    else:
        print(total_memory, "Go memory detected, The server can run properly,", req_memory, "Go needed to run.")

    # CHECKING CORE NUMBER

    total_cores = os.cpu_count()
    req_cores = yaml_conf_content['requirements']['CORE']

    if total_cores < req_cores:
        print(total_cores, "CPU cores detected, The server need at least", req_cores, "cores to run!")
    else:
        print(total_cores, "CPU cores detected, The server can run properly,", req_cores, "cores needed to run.")

    #CHECKING FREE SPACE

    total_space = psutil.disk_usage('/')
    total_space = floor((total_space[2])/(2**30))
    req_space = yaml_conf_content['requirements']['HDD']

    if total_space < req_space:
        print(total_space, "Go Free space detected, at least", req_space,"Go needed!")
    else:
        print(total_space, "Go Free space detected, the server can install properly", req_space,"Go needed.")

    print('/////////////////////////////////////////////////////////////////')