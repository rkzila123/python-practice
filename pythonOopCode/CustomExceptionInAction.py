'''
Created on Nov 27, 2023

@author: Rohit.Kumar012
'''

class CusException(Exception):
    def __init__(self,msg):
        self.msg=msg

def withdrawl(amount):
    if(amount>100000):
        raise CusException('You can not withdraw more than 10000 at a time ')
    

withdrawl(120000)