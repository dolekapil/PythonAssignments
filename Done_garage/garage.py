__author__ = 'dolek'

import sys
from jobs import Job
class Garage:
    __slots__ = 'cathyData','howardData','sizeC','sizeH'
    def __init__(self):
        self.cathyData = []
        self.howardData = []
        self.sizeC = 0
        self.sizeH = 0

    def insertHeap(self,job):
        self.cathyData.append(job)
        self.howardData.append(job)
        self.sizeC += 1
        self.sizeH += 1
        self.bubbleUpCathyHeap(self.sizeC-1)
        self.bubbleUpHowardHeap(self.sizeH-1)

    def bubbleUpCathyHeap(self,position):
        while position > 0 and self.cathyData[position].cost > self.cathyData[self.parent(position)].cost:
            self.cathyData[position],self.cathyData[self.parent(position)] = \
                self.cathyData[self.parent(position)],self.cathyData[position]
            position = self.parent(position)


    def bubbleUpHowardHeap(self,position):
        while position > 0 and self.howardData[position].time < self.howardData[self.parent(position)].time:
            self.howardData[position],self.howardData[self.parent(position)] = \
                self.howardData[self.parent(position)],self.howardData[position]
            position = self.parent(position)


    def parent(self,location):
        return (location-1)//2

    def popHowardHeap(self):
        temp = self.howardData[0]
        while temp.done is True and self.sizeH > 0:
            self.__popHowardHeap()
            temp = self.howardData[0]
        if self.sizeH > 0:
            self.__popHowardHeap()
            temp.done = True
        else:
            print("No more jobs to do.")
            sys.exit(0)
        return temp

    def __popHowardHeap(self):
        self.sizeH -= 1
        if self.sizeH > 0:
            self.howardData[0] = self.howardData.pop(self.sizeH)
            self.bubbleDownHowardHeap(0)

    def popCathyHeap(self):
        temp = self.cathyData[0]
        while temp.done is True and self.sizeC > 0:
            self.__popCathyHeap()
            temp = self.cathyData[0]
        if self.sizeC > 0:
            self.__popCathyHeap()
            temp.done = True
        else:
            print("No more jobs to do.")
            sys.exit(0)
        return temp

    def __popCathyHeap(self):
        self.sizeC -= 1
        if self.sizeC > 0:
            self.cathyData[0] = self.cathyData.pop(self.sizeC)
            self.bubbleDownCathyHeap(0)

    def bubbleDownCathyHeap(self,position):
        swap = self.maxCost(position)
        while swap != position:
            self.cathyData[position], self.cathyData[swap] = self.cathyData[swap], self.cathyData[position]
            position = swap
            swap=self.maxCost(position)

    def bubbleDownHowardHeap(self,position):
        swap = self.minTime(position)
        while swap != position:
            self.howardData[position], self.howardData[swap] = self.howardData[swap], self.howardData[position]
            position = swap
            swap = self.minTime(position)

    def maxCost(self,position):
        leftChild = position*2+1
        rightChild = position*2+2
        if leftChild >= self.sizeC:
            return position
        if rightChild >= self.sizeC:
            if self.cathyData[position].cost < self.cathyData[leftChild].cost:
                return leftChild
            else:
                return position

        if self.cathyData[leftChild].cost > self.cathyData[rightChild].cost:
            if self.cathyData[position].cost > self.cathyData[leftChild].cost:
                return position
            else:
                return leftChild
        else:
            if self.cathyData[position].cost > self.cathyData[rightChild].cost:
                return position
            else:
                return rightChild

    def minTime(self,position):
        leftChild = position*2+1
        rightChild = position*2+2
        if leftChild >= self.sizeH:
            return position
        if rightChild >= self.sizeH:
            if self.howardData[position].time > self.howardData[leftChild].time:
                return leftChild
            else:
                return position

        if self.howardData[leftChild].time < self.howardData[rightChild].time:
            if self.howardData[position].time < self.howardData[leftChild].time:
                return position
            else:
                return leftChild
        else:
            if self.howardData[position].time < self.howardData[rightChild].time:
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
            if len(data) == 3 and data[1].isnumeric() and data[2].isnumeric():
                n = Job(data[0], int(data[1]), int(data[2]))
                garageObj.insertHeap(n)
                print(n)
            elif len(data) == 2 and data[0] == 'Cathy' and data[1] == 'ready':
                    job = garageObj.popCathyHeap()
                    print("Cathy starting job", job.name)
            elif len(data) ==2 and data[0] == 'Howard' and data[1] == 'ready':
                job = garageObj.popHowardHeap()
                print("Howard starting job", job.name)
            else:
                print("Invalid input.")
                sys.exit(0)

    except FileNotFoundError:
        print("please enter valid file name.")
        sys.exit(0)
if __name__ == '__main__':
    main()