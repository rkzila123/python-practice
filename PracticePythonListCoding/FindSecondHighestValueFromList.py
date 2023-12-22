'''
Created on Dec 4, 2023

@author: Rohit.Kumar012
'''


def findSeondHigh(newList):
    
    set1= set(newList)
    print(set1)   
    set1.remove(max(set1))   
    print(max(set1))
    
    

l=[2,4,5,4,9,7,8]
findSeondHigh(l)
