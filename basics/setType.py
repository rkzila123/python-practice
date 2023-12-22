'''
Created on Oct 5, 2023

@author: Rohit.Kumar012
'''

s={10,20,30,'xyz',40.0}
print('print set element :: ',s)
print('print data type of set :: ',type(s))

s.update([90,88])
print('print set element after updating/adding element :: ',s)

s.remove(30)
print('print set element after removing element :: ',s)

f=frozenset(s)
""" f.update([50]) & f.remove(20)
update and remove functions are not allowed for frozen set """

print('print frozen set element :: ',f)
