'''
Created on Nov 9, 2023

@author: Rohit.Kumar012
'''

from functools import reduce

lst=[10,20,30,40]

print(reduce(lambda x,y : (x+y), lst))
