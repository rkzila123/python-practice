'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''

def splitStrListBasedOnPrefix(strList,prefix):
    
    newList=[]
    
    for x in strList:
        
        if x.startswith(prefix):
            newList.append([x])
            
        else:
            newList[-1].append(x)  
            
    print(newList)          




strList=['geeksforgeeks', 'best', 'geeks', 'and', 'geeks', 'love', 'CS']
prefix='geeks'

splitStrListBasedOnPrefix(strList,prefix)
