#!/usr/bin/python3
# makes tgz archive
import tarfile
from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['54.197.73.242', '54.208.60.185']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/rsa'


def do_pack():
    # packs file
    try:
        name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        local("tar -cvzf versions/{}.tgz {}".format(
            name, "web_static/"))
        size = os.path.getsize("./versions/{}.tgz".format(name))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
            name, size))
        return "versions/{}.tgz".format(name)
    except:
        return None


def do_deploy(archive_path):
    fd = archive_path.split('/')[1]
    try:
        put(archive_path, '/tmp/{}'.format(fd))
        run('mkdir -p /data/web_static/releases/{}'.format(fd))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(fd, fd))
        run('rm /tmp/{}'.format(fd))
        run('mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/'.format(fd, fd))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(fd))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/\
        /data/web_static/current'.format(fd))
        print("New version deployed!")
        return True
    except:
        print("New version not deployed...")
        return False
