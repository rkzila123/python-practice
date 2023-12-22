'''
Created on Dec 6, 2023

@author: Rohit.Kumar012
'''


def findLetterWhichStartWithK(testList,startsWith):
    
    for string in testList:
        
        for st in string.split():
            
            if st[0].lower() == startsWith.lower():
                
                print(st)



testList = ['Gfg is good for learning', 'Gfg is for geeks', 'I love G4G']
startsWith = 'l'

findLetterWhichStartWithK(testList,startsWith)