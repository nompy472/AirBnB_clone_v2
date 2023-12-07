#!/usr/bin/python3
# Deletes out-of-date archives.
import os
from fabric.api import *

env.hosts = ["54.158.222.196", "34.207.120.67"]


def do_clean(number=0):
    """Deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number = 0 || 1, keeps only the most recent archive. If
    number = 2, keeps the most and second-most recent archives,
    etc."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
