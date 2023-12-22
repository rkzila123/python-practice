'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''
input_str= input('Enter a string')

temp=input_str.split()
#print(temp)

result=[]
lastIndex=len(temp)-1

while lastIndex>=0 :
    result.append(temp[lastIndex])
    lastIndex=lastIndex-1
    
#print(result) 
print(' '.join(result))   

'''
Enter a string - hii is am rohit
o/p - rohit am is hii


'''