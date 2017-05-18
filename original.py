#!/usr/bin/python
#Filename:original.py
print ('Welcom!')
 
original = raw_input("Enter a word")
empty_string="Enter a word"
if len(empty_string)> 0 and original.isalpha():
         print (original)
else:
         print (False)
