'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''


def getAllCombination(newList):
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    
                    if( i!=j and j!=k and k!=l and l!=j and l!=i and k!=i):
                        
                        print(newList[i],newList[j],newList[k],newList[l])
                        



l=[1,3,6,9]
getAllCombination(l)
