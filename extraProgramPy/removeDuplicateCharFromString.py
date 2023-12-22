'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''

input_str= input('Enter a string')
result=[]

for char in input_str:
    if char not in result:
        result.append(char)
        
print(''.join(result))        
        