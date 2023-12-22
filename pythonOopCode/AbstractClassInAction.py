'''
Created on Nov 27, 2023

@author: Rohit.Kumar012
'''
from abc import abstractmethod,ABC

class BMW(ABC):
    
    def __init__(self,modelNumber,launchYear,price):
        self.modelNumber=modelNumber
        self.launchYear=launchYear
        self.price=price
        
    def starting(self):
        print("Starting car")    
     
    def stopping(self):
        print("Stopping car")
    
    @abstractmethod    
    def drive(self):  
        pass  
        
            


class ThreeSeries(BMW): 
    
    def __init__(self,crousControlEnable,modelNumber,launchYear,price):
        BMW.__init__(self, modelNumber, launchYear, price)
        self.crousControlEnable= crousControlEnable 
        
    def display(self):
        print("crousControlEnable :: ", self.crousControlEnable) 
        
    def starting(self):
        print("Starting button")
        
    def drive(self):
        print("Model 3 is driven")              
        
        
class FiveSeries(BMW): 
    
    def __init__(self,parkingEnable,modelNumber,launchYear,price):
        super().__init__(self, modelNumber, launchYear, price)
        self.parkingEnable= parkingEnable
        
    def drive(self):
        print("Model 5 is driven")    
        
t3= ThreeSeries(True,'BMWA1',2017,'50L')

print(t3.modelNumber)
print(t3.launchYear)
print(t3.price)
print(t3.crousControlEnable)

t3.starting()
t3.stopping()
t3.display()
t3.drive()