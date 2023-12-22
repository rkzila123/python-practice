'''
Created on Dec 4, 2023

@author: Rohit.Kumar012
'''

def checkOccrance(newList , num):
    counter=0
    for x in newList:
        if x==num:
            counter=counter+1
        
    print(num ,' ocured  ' , counter ,' times')


l=[2,4,5,3,6,7,5,8,2]
checkOccrance(l, 9)


def checkOccurenceOfAllElement(newList):
    result = {}
    for x in newList:
        if x in result.keys():
            result[x]=result.get(x)+1
        else:
            result[x]=1
            
    
    for k,v in result.items():
        print(k , 'occures' ,v ,'times')
    
checkOccurenceOfAllElement(l)            
        