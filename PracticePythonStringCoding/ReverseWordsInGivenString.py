'''
Created on Dec 7, 2023

@author: Rohit.Kumar012
'''

def reverseWordsInString(string):
    
    stList=string.split()
    revList=stList[::-1]
        
    print(" ".join(revList))    
        

string =" geeks quiz practice code"

reverseWordsInString(string)
