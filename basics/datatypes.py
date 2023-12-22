'''
Created on Oct 9, 2023

@author: Rohit.Kumar012
'''


uniqueId=1
firstName="Rohit"
lastName="  Kumar"
isInsumred=True
snn="123-45-6789"
billAmount="10000"
print(type(billAmount))

billAmount=float(billAmount)
print(type(billAmount))
paidAmount="7000"

print(uniqueId , firstName , lastName ,isInsumred , snn[7:len(snn)] ,billAmount)
print(uniqueId , firstName , lastName.lstrip() ,isInsumred , snn[7:] ,float(paidAmount))