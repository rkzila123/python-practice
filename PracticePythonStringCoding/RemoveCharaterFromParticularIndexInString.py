'''
Created on Dec 8, 2023

@author: Rohit.Kumar012
'''

def removeithCharacterFromString(string,indexToRemove):
    
    newStr=''
    
    try:
        length=len(string)
        
        if(indexToRemove>length):
            raise Exception()
        
        else:
            for i in range(length):
                if i!=indexToRemove:
                    newStr=newStr+string[i]
                    
    except:
        print('Invalid index as it is more than length of String')
            
    else:
        print(newStr) 
        
    
string ='Geeks123For123Geeks'
indexToRemove=30
removeithCharacterFromString(string,indexToRemove)