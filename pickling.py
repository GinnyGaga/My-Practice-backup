#!/usr/bin/python
#/Filename:picking.py

import pickle as p

shoplistfile = 'shoplist.data'

shoplist =['apple','mango','carrot']

f=open(shoplistfile,'wb+')
p.dump(shoplist,f)
f.close()

del shoplist

f=open(shoplistfile,'rb+')
storedlist=p.load(f)
print (storedlist)
