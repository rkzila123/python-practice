'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''

def decorFun(fun):
    def inner():
        result=fun() 
        return result *2
    return inner

@decorFun
def num():
    return 5

print(num())

