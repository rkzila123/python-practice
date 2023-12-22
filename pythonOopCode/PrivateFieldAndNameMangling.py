'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''
class Student:
    def __init__(self):
        self.__id=123
        self.__name='Rohit'
        self.age=31
        
    def display(self):
        print(self.__id) 
        print(self.__name) 
        print(self.age)    
        

s1=Student()
s1.display()

print()

print(s1._Student__id)  
print(s1._Student__name) 
print(s1.age)          