#!/usr/bin/python3
# Fabfile to delete outdated archives
import os
from fabric.api import *

env.hosts = ['3.84.237.80','100.25.203.47']

def do_clean(number=0):
    """ Deletes outdates archives, keeps the most and second
    most recent archives """
    num = 1 if int(num) == 0 else int(num)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(num)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(num)]
        [run("rm -rf ./{}".format(a)) for a in archives]
