'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''

def reverseAllElementFromList(sList):
    
    changeList=[]
    
    for st in sList:
        
        changeList.append(st[::-1])
        
    print(changeList)    
        



sList=['My','name','is','Rohit']
reverseAllElementFromList(sList)
