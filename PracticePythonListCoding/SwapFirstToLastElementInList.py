'''
Created on Dec 1, 2023

@author: Rohit.Kumar012
'''

def swapelement(lists):
    
    length=len(lists)
    temp=lists[length-1]
    lists[length-1]=lists[0]
    lists[0]=temp
    print(lists)

def swapele(newlist):
    l=len(newlist)
    newlist[0] , newlist[l-1]= newlist[l-1],newlist[0]
    print(newlist)
    

l1=[2,4,6,8,9]
swapelement(l1)

l2=[10,20,30,80,90]
swapele(l2)
print(len(l2))


