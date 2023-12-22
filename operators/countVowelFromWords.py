word=input('Enter a word here : ')
vowels={'a','e','i','o','u'}

result={}

for c in word:
    if c in vowels:
        result[c]=result.get(c, 0)+1
        
for k , v in result.items():
    print(k ,'count is ' ,v)        
        