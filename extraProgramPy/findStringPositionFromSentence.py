'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''
s='Hi my name is rohit and this name means lot to me'

subStr='name'

pos=-1

length= len(s)

isFound=False

while True:
    pos =  s.find(subStr, pos+1, length)
    if pos==-1:
        break
    print("Sub String found at position " , pos)
    isFound=True
    


if isFound==False:
    print('Sub String not found')    
    
    
'''

Sub String found at position  6
Sub String found at position  29

'''    