#!/usr/bin/env python3

#version 2.0-make .zip archieve of repo
import os
import time

#vars
source='/root/repos'
target_dir='/root/work/backup/repos/'
target=target_dir+time.strftime('%d%m%y_%H%M')+'.zip'
zip_command="zip -qr "+target+" "+source

#check if the target folder exists
#if not os.path.exists(target_dir):
#    os.makedirs(target)

os.system('clear')
print("Wait. Copy in progress...")

if os.system(zip_command)==0:
    print('Copied to '+target)
else:
    print('Error!')
