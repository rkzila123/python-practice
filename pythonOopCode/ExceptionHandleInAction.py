'''
Created on Nov 27, 2023

@author: Rohit.Kumar012
'''
try:
    f=open('MyFile', 'w')
    a,b=[int(x) for x in input('Enter two number').split()]
    c=a/b
    f.write('Writing %d in to file'  %c)
    #print(c)
    
except ZeroDivisionError:
    print("Divison with zero is not allowed")
    print('kindly enter non zero number')  
    
else:
    print('You have entered a non zero number')  
    
finally:
    f.close()
    print('File Closed')      
    
print('Code after Exception block')
      
    

