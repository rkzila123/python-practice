'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''


def decorFun(fun):
    def inner(n):
        result = fun(n) +' How are you '
        return result
    return inner


@decorFun
def fun(name):
    return 'Hello ' + name

print(fun('Rohit'))