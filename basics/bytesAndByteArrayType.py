'''
Created on Oct 9, 2023

@author: Rohit.Kumar012
'''
lst=[10,20,30,230]
print("type of lst :: ",type(lst))

b=bytes(lst)
print("type of bytes :: ",type(b))

b1=bytearray(lst)
print("type of bytes :: ",type(b1))

b1[2]=60
for i in b1:
    print(i)

''' Assignment is only possible in bytearray not in bytes
slicing and stepping is not possible in any one '''