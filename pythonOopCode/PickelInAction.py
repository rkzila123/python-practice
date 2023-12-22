'''
Created on Nov 28, 2023

@author: Rohit.Kumar012
'''
import pickle 
#,student
from student import Student

f=open("StudentDetail.dat", 'wb')
s=Student(123,'Rohit',70)
pickle.dump(s, f)
f.close()

