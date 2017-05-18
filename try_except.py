#!/usr/bin/python
#Filename:try_except.py

import sys

try:
	s=input('Enter something -->')
except EOF:
	print('\nWhy did you do an interruption on me?')
	sys.exit()
except:
	print('\nSome error/exception occurred.')
print('Done')

