#!/usr/bin/python
#Filename:finally.py

import time

try:
	f=open('poem.txt')
	while True:
		line = f.readline()
		if len(line)==0:
			break
		time.sleep(5)
		print (line,end='')
finally:
	f.close()
	print('Cleaning up...closed the file')
