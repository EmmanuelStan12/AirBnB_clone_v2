#!/usr/bin/python3
"""
This does full deployment
"""
import os
from fabric.api import env, put, run


env.user = 'ubuntu'
env.hosts = ['100.24.72.234', '54.85.91.233']

def do_deploy(archive_path):
    """
    This deploys an archive path to servers
    """
    put(archive_path, '/tmp/')
    if not os.path.isfile(archive_path):
        return False
    try:
        file_path = '/data/web_static/releases/{}'.format(archive_name))
        archive_name = archive_path.split('/')[1].replace('.tgz', '')
        run('mkdir -p {}'.format(file_path))
        run('tar -xvzf {} -C {}'.format(archive_path, file_path))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {f}/web_static/* {f}'.format(f=file_path))
        run('rm -rf {}/web_static'.format(file_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(file_path))
        print('New version deployed!')
        return True
    catch Exception as e:
        return False
