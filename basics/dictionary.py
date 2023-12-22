'''
Created on Oct 9, 2023

@author: Rohit.Kumar012
'''
dict1={1:"Rohit" , 2:"Ankit", 3:"Amit"}
print(dict1)
print(type(dict1))

k=dict1.keys()
print(type(k))

for i in k:
    print(i)
    
v=dict1.values()

for i in v:
    print(i)
    
print(dict1[2])

del dict1[2]  

''' delete element from dictionary with key ,
here del is function present in python 
not in dictionary '''

print(dict1)

