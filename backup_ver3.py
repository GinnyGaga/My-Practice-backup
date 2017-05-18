#!/usr/bin/python
#Filename:backup_ver3.py

import os
import time

source=['/home/dog/wolf']

target_dir='/home/dog/backup/'

today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=input('Enter a comment -->')
if len(comment)==0:
	target=today+os.sep+now+'.zip'
else:
	target=today+os.sep+now+'_'+\
                comment.replace(' ','_')+'.zip'
if not os.path.exists(today):
	os.mkdir(today)
	print ('Successful created directory',today)
zip_command="zip -qr '%s' %s" % (target,' '.join(source))
if os.system(zip_command)==0:
	print ('Successful backup to',target)
else:
	print('Backup FAILED')

