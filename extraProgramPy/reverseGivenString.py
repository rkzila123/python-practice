'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''
# 1st  way

input_String1= input('Enter a string ::')
print(input_String1[::-1])

# 2nd  way

input_String2= input('Enter a string ::')
lstIndex=len(input_String2)-1
result=''

while lstIndex >= 0: 
    result=result+input_String2[lstIndex]
    lstIndex=lstIndex-1
    
print(result)

# 3rd  way
''' Here reversed method return iterable object and 
we used join method to convert to String '''

input_String3= input('Enter a string ::')
print(''.join(reversed(input_String3)))