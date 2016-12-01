__author__ = 'dolek'

import sys
from operations import Operation
class Garage:
    __slots__ = 'cathyData','howardData','size'
    def __init__(self):
        self.cathyData = []
        self.howardData = []
        self.size =0


    def insertHeap(self,job):
        self.cathyData.append(job)
        self.howardData.append(job)
        job.cIndex = self.size
        job.hIndex = self.size
        self.size+=1
        pos1 = self.bubbleUpCathyHeap(self.size-1)
        pos2 = self.bubbleUpHowardHeap(self.size-1)
        job.cIndex = pos1
        job.hIndex = pos2


    def bubbleUpCathyHeap(self,position):
        while position>0 and self.cathyData[position].cost>self.cathyData[self.parent(position)].cost:
            self.cathyData[position],self.cathyData[self.parent(position)] = \
                self.cathyData[self.parent(position)],self.cathyData[position]
            self.cathyData[position].cIndex,self.cathyData[self.parent(position)].cIndex = \
                self.cathyData[self.parent(position)].cIndex,self.cathyData[position].cIndex
            position = self.parent(position)
        return position

    def bubbleUpHowardHeap(self,position):
        while position>0 and self.howardData[position].time<self.howardData[self.parent(position)].time:
            self.howardData[position],self.howardData[self.parent(position)] = \
                self.howardData[self.parent(position)],self.howardData[position]
            self.howardData[position].hIndex,self.howardData[self.parent(position)].hIndex = \
                self.howardData[self.parent(position)].hIndex,self.howardData[position].hIndex
            position = self.parent(position)
        return position

    def parent(self,location):
        return (location-1)//2

    def popHowardHeap(self):
        temp = self.howardData[0]
        self.size-=1
        if self.size>0:
            popH = self.howardData.pop(self.size)
            self.howardData[0]= popH
            popH.hIndex = 0
            popC = self.cathyData.pop(self.size)
            self.cathyData.insert(popH.cIndex,popC)
            popC.cIndex = popH.cIndex
            self.bubbleDownHowardHeap(0)
            self.bubbleDownCathyHeap(popC.cIndex)
        return temp


    def popCathyHeap(self):
        temp = self.cathyData[0]
        self.size-=1
        if self.size>0:
            popC=self.cathyData.pop(self.size)
            self.cathyData[0]=popC
            popC.cIndex=0
            popH=self.howardData.pop(self.size)
            self.howardData.insert(popC.hIndex,popH)
            popH.hIndex = popC.hIndex
            self.bubbleDownHowardHeap(popH.hIndex)
            self.bubbleDownCathyHeap(0)
        return temp

    def bubbleDownCathyHeap(self,position):
        swap = self.maxCost(position)
        while swap != position:
            self.cathyData[position],self.cathyData[swap]=self.cathyData[swap],self.cathyData[position]
            self.cathyData[position].cIndex,self.cathyData[swap].cIndex=self.cathyData[swap].cIndex,self.cathyData[position].cIndex
            position =swap
            swap=self.maxCost(position)

    def bubbleDownHowardHeap(self,position):
        swap = self.minTime(position)
        while swap != position:
            self.howardData[position],self.howardData[swap]=self.howardData[swap],self.howardData[position]
            self.howardData[position].hIndex,self.howardData[swap].hIndex=self.howardData[swap].hIndex,self.howardData[position].hIndex
            position =swap
            swap=self.minTime(position)

    def maxCost(self,position):
        leftChild = position*2+1
        rightChild = position*2+2
        if leftChild>=self.size:
            return position
        if rightChild>=self.size:
            if self.cathyData[position].cost<self.cathyData[leftChild].cost:
                return leftChild
            else:
                return position

        if self.cathyData[leftChild].cost > self.cathyData[rightChild].cost:
            if self.cathyData[position].cost>self.cathyData[leftChild].cost:
                return position
            else:
                return leftChild
        else:
            if self.cathyData[position].cost>self.cathyData[rightChild].cost:
                return position
            else:
                return rightChild

    def minTime(self,position):
        leftChild = position*2+1
        rightChild = position*2+2
        if leftChild>=self.size:
            return position
        if rightChild>=self.size:
            if self.howardData[position].time>self.howardData[leftChild].time:
                return leftChild
            else:
                return position

        if self.howardData[leftChild].time < self.howardData[rightChild].time:
            if self.howardData[position].time<self.howardData[leftChild].time:
                return position
            else:
                return leftChild
        else:
            if self.howardData[position].time<self.howardData[rightChild].time:
                return position
            else:
                return rightChild

def main():
    garageObj = Garage()
    file = input("enter the name of the file which contains garage operation.")
    try:
        filehandle = open(file)
        for line in filehandle:
            line = line.strip()
            data = line.split()
            if len(data) == 3:
                n = Operation(data[0],data[1],data[2])
                garageObj.insertHeap(n)
                print(n)
            else:
                if data[0]=='Cathy':
                    job=garageObj.popCathyHeap()
                    print("Cathy starting job ",job.name)
                elif data[0]=='Howard':
                    job=garageObj.popHowardHeap()
                    print("Howard starting job ",job.name)
    except FileNotFoundError:
        print("please enter valid file name.")
        sys.exit(0)
if __name__ == '__main__':
    main()