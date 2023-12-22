'''
Created on Nov 15, 2023

@author: Rohit.Kumar012
'''
a=[2,4,6,8,10,12]
b=[3,6,9,12,15,18]

result=[]

comprehenceResult=[]

for i in a:
    if i in b:
        result.append(i)
        
print(result)     

comprehenceResult=[i for i in a if i in b]

print(comprehenceResult)