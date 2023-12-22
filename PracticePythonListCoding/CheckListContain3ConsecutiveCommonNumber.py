'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''


def get3ConsecutiveElement(list1):
    
    length=len(list1)
    
    r=range(length-2)
    s=set()
    
    for i in r:
        
        if list1[i]==list1[i+1] and list1[i+1]==list1[i+2]:
            
            s.add(list1[i])
            #print(s)
            #print(list1[i])
            
        
    for x in s:
        print(x)        


l1=[1, 1, 1, 64, 23, 64, 22, 22, 22,22]
get3ConsecutiveElement(l1)
