'''
Created on Oct 10, 2023

@author: Rohit.Kumar012
'''

students={"rohit":["java","jquery","jasper"],"sourab":["plsql","java","angular"] , 
          "abhinav":["angular" ,"python" ,"kafka"]}

keys=students.keys()

for eachKey in keys:
    print('courses taken by ',eachKey ,'are')
    lst=students[eachKey]
    # for eachCources in students[eachKey]:
    for eachCources in lst:
        print(eachCources)