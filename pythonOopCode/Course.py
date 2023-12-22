'''
Created on Nov 15, 2023

@author: Rohit.Kumar012
'''

class Course :
    def __init__(self,name,ratings):
        self.name=name
        self.ratings=ratings
        
    # Instance method     
    def getaverage(self):
        numofelement=len(self.ratings)
        average=sum(self.ratings, 0)/numofelement
        print('Average rating of course ' , self.name ,' is ' , average)
        
            
c1=Course('Java',[1,2,3,4,5])


print(c1.name)
print(c1.ratings) 
c1.getAverage()       
