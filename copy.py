#!/usr/bin/env python36

#version 1.0
import os
import time

#vars
source='/home/docker/aws'
target='/home/docker/backup/'+time.strftime('%d%m%y_%H%M')
copy_command='cp -r '+source+' '+target

if not os.path.exists(target):
    os.makedirs(target)

if os.system(copy_command)==0:
    print('Copied to '+target)
else:
    print('Error!')


