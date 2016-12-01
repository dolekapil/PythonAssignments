__author__ = 'dolek'

class Heap:
    __slots__ = 'data','size','lessfn'

    def __init__(self,lessfn):
        """

        :param lessfn:
        :return:
        """
        self.data = []
        self.size =0
        self.lessfn = lessfn

    def insert(self,value):
        self.data.append(value)
        self.size+=1
        self.bubbleUp(self.size-1)

    def __str__(self):
        result = "heap:  "
        for i in range(len(self.data)):
            result =result+str(self.data[i])+" "
        return result
    def bubbleUp(self,loc):
        while loc>0 and self.lessfn(self.data[loc],self.data[self.parent(loc)]):
            self.data[loc],self.data[self.parent(loc)]=self.data[self.parent(loc)],self.data[loc]
            loc = self.parent(loc)

    def parent(self,loc):
        return (loc-1)//2

    def pop(self):
        temp = self.data[0]
        self.size-=1
        if self.size>0:
            self.data[0]=self.data.pop(self.size)
            n =self.bubbleDown(0)
        return temp

    def bubbleDown(self,loc):
        swap = self.min(loc)
        while swap != loc:
            self.data[loc],self.data[swap]=self.data[swap],self.data[loc]
            loc =swap
            swap=self.min(loc)

    def min(self,loc):
        ch1 = loc *2 +1
        ch2 = loc*2+2

        if ch1>= self.size:
            return loc
        if ch2>=loc:
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:return ch1

        if self.lessfn(self.data[ch1],self.data[ch2]):
            if self.lessfn(self.data[loc],self.data[ch1]):
                return loc
            else:return ch1
        else:
             if self.lessfn(self.data[loc],self.data[ch2]):
                 return loc
             else:return ch2
def main():
    h= Heap(lambda x,y:x<y)
    h.insert(10)
    h.insert(2)
    print(h)
    print(h.pop())
    print(h)
if __name__ == '__main__':
    main()