__author__ = 'dolek'

class Job:
    __slots__='name','time','cost','done'

    def __init__(self,name,time,cost):
        self.name = name
        self.time = time
        self.cost = cost
        self.done = False

    def __str__(self):
        return "New job arriving! Job name: " + self.name + ", "+str(float(self.time)) + " hours and $"+str(float(self.cost))