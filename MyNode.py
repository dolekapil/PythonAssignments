__author__ = 'dolek'

class LinkedNode:

    __slots__ = 'value','link'

    def __init__(self,value,link=None):
        self.value=value
        self.link=link

    def __str__(self):
        return str(self.value)

    def __repr__( self ):
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return "LinkedNode(" + repr( self.value ) + "," + \
               repr( self.link ) + ")"

def main():
    s = LinkedNode(10)
    q=LinkedNode(12,s)
    print(q.__repr__())
if __name__ == '__main__':
    main()