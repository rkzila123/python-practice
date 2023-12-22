'''
Created on Nov 6, 2023

@author: Rohit.Kumar012
'''

word=input('Enter a word here : ')

result={}

'''
result_List=[]
for c in word:
    if c not in result:
        result_List.append(c)
        result[c]=result.get(c, 0)+1
    else:
        result[c]=result.get(c, 0)+1
            
'''

for c in word:
    if c in result.keys():
        result[c]=result.get(c)+1
    else:
        result[c]=1    
    
        
for k , v in result.items():
    print(k ,'count is ' ,v) 