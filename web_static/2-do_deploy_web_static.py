#!/usr/bin/python3
"""
"""

import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.host = ['34.138.174.14', '18.207.116.48']


def do_deploy(archive_path):
    if (os.path.isfile(archive.path) is False):
        return(False)
    try:
        new = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new.split(".")[0])
        put(archive_path, "/tmp")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new, new_folder))
        run("sudo rm /tmp/{}".format(new))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ls -s {} /data/web_static/current".format(new_folder))
        return(True)
    except Exception:
        return(False)
