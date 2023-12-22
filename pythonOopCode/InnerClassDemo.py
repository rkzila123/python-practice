'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''
class Car:
    def __init__(self,name,mfDate):
        self.name=name
        self.mfDate=mfDate
    class Engine :
        def __init__(self,chassisNumber):
            self.chassisNumber=chassisNumber
            
        def start(self):
            print("Engine has started")        

c1=Car('Ford','2019')

e1=c1.Engine('123456')

e1.start()