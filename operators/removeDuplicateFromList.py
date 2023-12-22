l1=eval(input('Enter a list '))
print(l1)
#s1=set(l1)
#print(s1)
l2=[]
for val in l1:
    if val not in l2:
        l2.append(val)

print(l2)