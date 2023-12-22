'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''

def square(fun):
    def inner():
        result = fun()
        return result*result
    return inner

def half(fun):
    def inner():
        result = fun()
        return result/2
    return inner

@half
@square
def num():
    return 10

print(num())
