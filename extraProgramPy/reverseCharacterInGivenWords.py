'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''
input_str= input('Enter a string')

temp=input_str.split()

result=[]
lastIndex=len(temp)-1
i=0

while i<=lastIndex :
    str_temp=temp[i]
    result.append(str_temp[::-1])
    i=i+1
    
#print(result) 
print(' '.join(result)) 


'''

Enter a string - you are beautyful
o/p - uoy era lufytuaeb

''' 