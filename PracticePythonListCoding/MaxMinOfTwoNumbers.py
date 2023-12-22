'''
Created on Dec 1, 2023

@author: Rohit.Kumar012
'''

def getmax(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
    
def getmin(num1,num2):
    if num1<num2:
        return num1
    else:
        return num2
    
    
a,b=10,15
print('Max number is ' ,getmax(a, b))    
print('Min number is ' ,getmin(a, b))
