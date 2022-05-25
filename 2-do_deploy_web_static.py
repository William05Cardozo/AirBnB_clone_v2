#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
from os.path import exists
from fabric.api import put, run, env
env.hosts = ['34.138.174.14', '18.207.116.48']


def do_deploy(archive_path):
    """ deploy """
    if exists((archive_path) is False):
        return(False)

    try:
        new = archive_path.split("/")[-1]
        new_folder = new.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}".format(path, new_folder))
        run("tar xzf /tmp/{} -C {}{}".
            format(new, path, new_folder))
        rm("mv {0}{1}/web_static/* {0}{1}/".format(path, new_folder))
        run("rm /tmp/{}".format(new))
        run("rm /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, new_folder))
        return(True)
    except Exception:
        return(Falsie)
