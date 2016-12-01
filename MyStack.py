__author__ = 'dolek'

from MyNode import LinkedNode
class Stack:
    __slots__='top'

    def __init__(self):
        self.top = None
    def __str__(self):
        n=self.top
        result = "( "
        while n is not None:
            result = result+str(n)+" "
            n=n.link
        result=result+")"
        return result

    def push(self,value):
        self.top = LinkedNode(value,self.top)

    def pop(self):
        self.top = self.top.link

    def peek(self):
        return self.top.value
    def isEmpty(self):
        return self.top == None

def main():
    s = Stack()
    s.push(10)
    s.push(12)
    print(s)
    print(s.peek())
    s.pop()
    print(s)
    s.pop()
    s.push(32)
    print(s.isEmpty())
    print(s)
if __name__ == '__main__':
    main()