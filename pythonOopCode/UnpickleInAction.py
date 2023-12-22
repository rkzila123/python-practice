'''
Created on Nov 29, 2023

@author: Rohit.Kumar012
'''
import pickle,student

print('pickle starting ')
f=open('StudentDetails.dat' ,'wb')
s=student.Student(123,'Rahul',70)
pickle.dump(s,f)
print('pickle Done ')
print('unpickle starting ')
f=open('StudentDetails.dat' ,'rb')
obj=pickle.load(f)
print('unpickle Done ')
obj.display()
f.close()