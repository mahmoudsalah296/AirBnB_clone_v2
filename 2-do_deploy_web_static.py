#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local, put, run, env


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    env.hosts = ["54.90.17.187", "54.227.129.101"]
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if (
        run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)
        ).failed
        is True
    ):
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if (
        run(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)
        ).failed
        is True
    ):
        return False
    if (
        run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed
        is True
    ):
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if (
        run(
            "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)
        ).failed
        is True
    ):
        return False
    return True
