'''
Created on Nov 29, 2023

@author: Rohit.Kumar012
'''

f=open('MyFile.txt','r')
print(f.read())

f.seek(0)
print('try to read line wise')
s=f.readline()
print(s)

f.seek(0)
print(f.readlines())



