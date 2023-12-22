'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''

class Student:
    
    def setId(self,s_id):
        self.id=s_id
        
    def getId(self):
        return self.id
    
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return self.name
    
s1= Student()
s1.setId(123)
s1.setName('Rohit')    

print(s1.getId() ,' : ' , s1.getName())