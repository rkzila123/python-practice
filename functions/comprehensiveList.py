'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''

lst=[]
for x in range(1,11):
    lst.append(x**3)    
print(lst)   


lst=[]
lst=[x**3 for x in range(1,11)]
print(lst) 

lst=[x for x in range(2,21,2)]
print(lst)

lst=[x for x in range(1,21) if x%2==0]
print(lst)