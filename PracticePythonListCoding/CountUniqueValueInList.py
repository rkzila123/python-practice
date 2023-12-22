'''
Created on Dec 5, 2023

@author: Rohit.Kumar012
'''


def getUniqueElementCount1(list1):
    
    uniqueCount=0
    result={}
    for x in list1:
        
        if x not in result.keys():
            result[x]=1
            uniqueCount=uniqueCount+1
            
    print('No of unique element count is ' , uniqueCount)       
        
def getUniqueElementCount2(list1):
    set1=set(list1)
    l=len(set1)
    print('No of unique element count is method2 ' , l)        


l1=[2,3,4,5,6,3,4,6,7,8]
getUniqueElementCount1(l1)
getUniqueElementCount2(l1)
