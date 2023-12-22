'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''
class StaticMethod :
    
    noOfObjectCreated=0
    
    def __init__(self):
        StaticMethod.noOfObjectCreated +=1
    
    @staticmethod    
    def display():
        print( StaticMethod.noOfObjectCreated)
        
s1=  StaticMethod()
s2= StaticMethod() 
s3= StaticMethod()

StaticMethod.display()     
            