'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''

def findCombinationHavingSumX(newList , sums):
    
    checkList=[]
    
    for i in range(len(newList)-1):
        
        for x in newList:
            
            if(newList[i]!= x and (newList[i]+x)==sums and 
               (x not in checkList or newList[i] not in checkList )):
                
                checkList.append(x)
                checkList.append(newList[i])
                
                print(newList[i] , x)
        




l1=[1,2,3,4,6,7,8,9,5]
sums=10
findCombinationHavingSumX(l1,sums)