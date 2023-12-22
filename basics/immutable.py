'''
Created on Oct 9, 2023

@author: Rohit.Kumar012
'''
a=10
b=10

print(id(a))
print(id(b))
print(a is b)

a=True
b=False

print(id(a))
print(id(b))
print(a is b)

a="Rohit"
b="Rohit"

print(id(a))
print(id(b))
print(a is b)

''' Not like JAVA only string data type is immutable 
in python all data types are immutable 
once we change value then python runtime will assign new memory allocation '''