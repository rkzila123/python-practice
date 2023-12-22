'''
Created on Nov 16, 2023

@author: Rohit.Kumar012
'''

class Patient:
    
    def __init__(self,name,age):
        self.name=name
        self.age = age
        self.clinicals=[]
     
    def addClinicalData(self,clinical): 
        self.clinicals.append(clinical) 


class ClinicalData:
    
    def __init__(self,attributeName,attributeReport):
        self.attributeName= attributeName
        self.attributeReport=attributeReport
        
        
p1=Patient("Rohit",31)
c1=  ClinicalData("BP" ,"80/120")  
p1.addClinicalData(c1)
c2= ClinicalData("Sugar" ,"120")   
p1.addClinicalData(c2) 


print('Patient Name : ' ,p1.name , ' , Patient Age : ' ,p1.age)
print()
for c in p1.clinicals:
    print(c.attributeName ,' : ' ,c.attributeReport)
    
    


        
        
                