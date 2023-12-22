'''
Created on Dec 1, 2023

@author: Rohit.Kumar012
'''


def getMaxValu(newList):
    maxVal=0
    minVal=0
    for x in newList:
        if(x>maxVal):
            maxVal=x
    for x in newList:
        if(x<minVal):
            minVal=x
    
    print(maxVal)
    print(minVal)
    

       

l1=[2,4,-5,10,6,8,9,-3]
getMaxValu(l1)
