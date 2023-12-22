'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''

def custom(x,y):
    while x<y :
        yield x**2
        x=x+1
        
result = custom(10, 20)     

for x in result:print(x)  
   
