__author__ = 'dolek'
from MyNode import LinkedNode
class Queue:
    __slots__='front'

    def __init__(self):
        self.front=None

    def enQueue(self,value):
        n=self.front
        if n is None:
            self.front = LinkedNode(value)
        else:
            while n.link is not None:
                n=n.link
            n.link=LinkedNode(value)

    def deQueue(self):
        self.front = self.front.link

    def __str__(self):
        result = "( "
        n= self.front
        while n is not None:
            result = result + str(n)+" "
            n = n.link
        result = result+")"
        return result

    def isEmpty(self):
        return self.front == None

    def peek(self):
        return str(self.front.value)

def main():
    q = Queue()
    q.enQueue(10)
    q.enQueue(23)
    print(q)
    q.deQueue()
    print(q)
    q.enQueue(43)
    print(q)
    print(q.peek())
if __name__ == '__main__':
    main()