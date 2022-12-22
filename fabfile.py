#!/usr/bin/python3
# This is a fabric file that will be used for deployment

from fabric.api import *
env.use_ssh_config = True

def web_servers():
    env.hosts = ['57647-web-01' '57647-web-02']

def deploy():
    run('57647-web-01' '57647-web-02')


