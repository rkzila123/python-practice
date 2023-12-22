'''
Created on Nov 28, 2023

@author: Rohit.Kumar012
'''
file=open("MyFile.txt", 'w')
print('Input string (Type $ when you are done) ')
s=''
while s !='$':
    s=input()
    file.write(s+'\n')
    
file.close()