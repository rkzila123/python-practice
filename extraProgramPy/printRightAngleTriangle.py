'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''

''' 3rd pattern '''
    
n4=int(input('Enter a number here : '))

for i in range(1,n4+1):
    print(' '*(n4-i) , end="")
    print('*'*(i))

''' 1st way '''

n=int(input('Enter a number here : '))

for i in range(1,n+1):
    for j in range(1,i+1):
        print('* ',end="")
    print()   
    
 
''' 2nd way '''
    
n2=int(input('Enter a number here : '))

for i in range(1,n2+1):
    print('* '*i)


''' 2nd pattern '''
    
n3=int(input('Enter a number here : '))

for i in range(1,n3+1):
    print(' '*(n3-i) , end="")
    print('* '*(i))
