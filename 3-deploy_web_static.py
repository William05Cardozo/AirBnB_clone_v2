#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to
your web servers, using the function deploy:
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
from datetime import datetime
env.hosts = ['34.138.174.14', '18.207.116.48']


def do_pack():
    ttime = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(ttime))
        return ("versions/web_static_{}.tgz".format(ttime))
    except:
        return(None)


def do_deploy(archive_path):
    """ deploy """
    if (os.path.isfile(archive_path) is False):
        return(False)

    try:
        new = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new, new_folder))
        run("sudo rm /tmp/{}".format(new))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return(True)
    except:
        return(False)


def deploy():
    try:
        archive_address = do_pack()
        val = do_deploy(archive_address)
        return(val)
    except Exception:
        return(False)
