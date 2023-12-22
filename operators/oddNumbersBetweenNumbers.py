a,b=[int(x) for x in input('Enter start and end number between which we need to find odd number :').split()]
print(a,b)
while (a<=b):
    if a%2 != 0:
        print(a)
        a+=2
    else :
        a+=1    