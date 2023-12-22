'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''

class BMW:
    
    def __init__(self,modelNumber,launchYear,price):
        self.modelNumber=modelNumber
        self.launchYear=launchYear
        self.price=price
        
    def starting(self):
        print("Starting car")    
     
    def stopping(self):
        print("Stopping car")
        
            


class ThreeSeries(BMW): 
    
    def __init__(self,crousControlEnable,modelNumber,launchYear,price):
        BMW.__init__(self, modelNumber, launchYear, price)
        self.crousControlEnable= crousControlEnable 
        
    def display(self):
        print("crousControlEnable :: ", self.crousControlEnable) 
        
    def starting(self):
        print("Starting button")          
        
        
class FiveSeries(BMW): 
    
    def __init__(self,parkingEnable,modelNumber,launchYear,price):
        BMW.__init__(self, modelNumber, launchYear, price)
        self.parkingEnable= parkingEnable
        
t3= ThreeSeries(True,'BMWA1',2017,'50L')

print(t3.modelNumber)
print(t3.launchYear)
print(t3.price)
print(t3.crousControlEnable)

t3.starting()
t3.stopping()
t3.display()

                    