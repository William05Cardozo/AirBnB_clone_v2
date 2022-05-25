#!/usr/bin/python3

from fabric.api import *
from datetime import datetime

def do_pack():
    ttime = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(ttime))
        return ("versions/web_static_{}.tgz".format(ttime))
    except:
        return (None)
