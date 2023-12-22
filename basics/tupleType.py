'''
Created on Oct 5, 2023

@author: Rohit.Kumar012

Tuple is immutable 
'''

tpl=(10,20,30,20,40,50,'Rohit' ,60.0)
print('print element inside tuple :: ',tpl)

""" If there is only one element in tuple then end with comma 
else python will not consider this 
as tuple """
tpl1=(10,)
print('print tuple having single element :: ',tpl1)
print('print data type of tpl1 :: ',type(tpl1))
tpl2=(10)
print('print data type of tpl2 :: ',type(tpl2))

""" Bracket is optional in tuple """
tpl3=10,
print('print element of tpl3 :: ',tpl3)

print('print data of tuple 2 times :: ',tpl*2)
print('print number of occurrence of element 20 from tuple :: ',tpl.count(20))
print('print index of given element from tuple :: ',tpl.index('Rohit'))

""" list to tuple conversion """
lst=[10,20,"kumar"]
print('print data type of list :: ',type(lst))
tpl4=tuple(lst)
print('print data type of tuple after conversion from list :: ',type(tpl4))