'''
Created on Nov 28, 2023

@author: Rohit.Kumar012
'''
class Student:
    def __init__(self,ids,name,marks):
        self.ids=ids
        self.name=name
        self.marks=marks
        
    def display(self):
        print(self.ids , self.name, self.marks) 
        
s=Student(23,'Rohit',70)
s.display()          