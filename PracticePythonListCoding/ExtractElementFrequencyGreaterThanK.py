'''
Created on Dec 5, 2023

@author: Rohit.Kumar012
'''

def getElements(list1,freqs):
    
    newList=[]
    result={}
    for x in list1:
        
        if x in result.keys():
            result[x]=result.get(x)+1
        
        else:
            result[x]=1
            
    for k,v in result.items():
        
        if v>freqs:
            newList.append(k)  
            
    print(newList)                




l1=[2,3,4,5,6,3,4,6,7,8,2,3,5,7,5]
freqs=2

getElements(l1,freqs)
