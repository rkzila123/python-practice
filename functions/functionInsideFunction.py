'''
Created on Nov 7, 2023

@author: Rohit.Kumar012
'''

def greeting(name):
    def messsage():
        return 'Hello'
    result=messsage()+' ' +name
    return result

print(greeting('Rohit'))