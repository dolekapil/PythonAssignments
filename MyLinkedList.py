__author__ = 'dolek'

from MyNode import LinkedNode
class LinkedList:
    __slots__ = 'front'

    def __init__(self):
        self.front = None

    def append(self,value):
        if self.front is None:
            self.front = LinkedNode(value)
        else:
            n=self.front
            while n.link is not None:
                n=n.link
            n.link = LinkedNode(value)

    def __str__(self):
        result = "LinkedList : ( "
        n = self.front
        while n is not None:
            result = result+str(n)+" "
            n= n.link
        result = result+")"
        return result

    def prepend(self,value):
        n =self.front
        self.front=LinkedNode(value,n)


    def getValue(self,cursor):
        counter = 1
        n= self.front
        while cursor > counter:
            if n is None:
                raise ValueError()
            else:
                n = n.link
                counter = counter+1
        return str(n.value)

    def addInMid(self,value,cursor):
        n= self.front
        for counter in range(cursor-1):
            if n is None:
                raise ValueError()
            else:
                n = n.link
        temp = n
        n.link = LinkedNode(value,temp.link)
    

def main():
    l = LinkedList()

    l.append(10)
    print(l)
    l.prepend(9)
    print(l)
    print(l.getValue(2))
    l.addInMid(8,1)
    print(l)


if __name__ == '__main__':
    main()