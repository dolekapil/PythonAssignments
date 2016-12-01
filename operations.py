__author__ = 'dolek'

class Operation:
    __slots__='name','time','cost','cIndex','hIndex'

    def __init__(self,name,time,cost):
        self.name = name
        self.time = time
        self.cost = cost
        self.cIndex=0
        self.hIndex=0

    def __str__(self):
        return "New job arriving! Job name: " + self.name + ", "+str(float(self.time)) + " hours and $"+str(float(self.cost))