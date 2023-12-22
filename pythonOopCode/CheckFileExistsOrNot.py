'''
Created on Nov 28, 2023

@author: Rohit.Kumar012
'''
import os,sys

if os.path.exists("MyFile123.txt"):
    file=open("MyFile123.txt", 'r')
    s=file.read()
    print(s)
    file.close()
else:
    print("file doesn't exists") 
    sys.exit()   
    

