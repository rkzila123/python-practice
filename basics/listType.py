'''
Created on Oct 5, 2023

@author: Rohit.Kumar012
'''

lst=[10,20,"Rohit" ,-10,30.5]

print('print list :: ',lst)            
print('print element from 2nd index :: ',lst[2])         
print('slice list from element 3 to 5 :: ',lst[3:5])       
print('repeat list elements 2 times :: ',lst*2)
print('length of list :: ',len(lst))

lst.append(40)
print('print list after append element :: ',lst)

lst.remove("Rohit")
print('print list after remove element :: ',lst)



del(lst[1])
print('print list after deleting particular index element  :: ',lst)

""" Some useful function on list """

print('get biggest element from list :: ',max(lst))
print('get smallest element from list :: ',min(lst))

lst.insert(3, 99)
print('print list after insertion of element at specific index :: ',lst)

lst.sort()
print('print list in ascending order :: ',lst)

lst.sort(reverse=True)
print('print list in descending order :: ',lst)

lst.clear()
print('print list after clearing all element from it :: ',lst)
