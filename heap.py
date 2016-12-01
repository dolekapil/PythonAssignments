__author__ = 'zjb'

class Heap(object):
    '''
    Heap that orders by a given comparison function.
    Comparison defaults to less-than for a min heap.
    '''
    __slots__ = ( 'data', 'size', 'above_fn' )

    def __init__(self,above_fn=lambda x,y:x<y):
        '''
        Constructor takes a comparison function.
        :param above_fn: Function that takes in two heap objects and returns true
        if the first arg goes higher in the heap than the second
        '''
        self.data = []
        self.size = 0
        self.above_fn = above_fn

    def __parent(self,loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return (loc-1)//2

    def __left(self,loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return loc * 2 + 1

    def __right(self,loc):
        '''
        Helper function to compute the parent location of an index
        :param loc: Index in the heap
        :return: Index of parent
        '''
        return loc * 2 + 2

    def __bubbleUp(self,loc):
        '''
        Starts from the given location and moves the item at that spot
        as far up the heap as necessary
        :param loc: Place to start bubbling from
        '''
        while loc > 0 and \
                self.above_fn(self.data[loc],self.data[self.__parent(loc)]):
            (self.data[loc], self.data[self.__parent(loc)]) = \
                      (self.data[self.__parent(loc)], self.data[loc])
            loc = self.__parent(loc)

    def __bubbleDown(self,loc):
        '''
        Starts from the given location and moves the item at that spot
        as far down the heap as necessary
        :param loc: Place to start bubbling from
        '''
        swapLoc = self.__top(loc)
        while swapLoc != loc:
            (self.data[loc], self.data[swapLoc]) = \
                      (self.data[swapLoc], self.data[loc])
            loc = swapLoc
            swapLoc = self.__top(loc)

    def __top(self,loc):
        '''
        Finds the value among loc and loc's two children that should be at
        the top. Correctly handles end-of-heap issues.
        :param loc: Index
        :return: index of top value
        '''
        left_pos = self.__left(loc)
        if left_pos >= self.size:
            # No children: no choice!
            return loc

        this_val = self.data[loc]
        left_val = self.data[left_pos]
        right_pos = self.__right(loc)
        if right_pos >= self.size:
            # Choose between this one and left child
            if self.above_fn( left_val, this_val ):
                return left_pos
            else:
                return loc

        right_val = self.data[right_pos]

        if self.above_fn( left_val, this_val ):
            if self.above_fn( left_val, right_val ):
                return left_pos
            else:
                return right_pos
        else:
            if self.above_fn( this_val, right_val ):
                return loc
            else:
                return right_pos

    def insert(self,item):
        '''
        Inserts an item into the heap.
        :param item: Item to be inserted
        '''
        self.data.append(item)
        # Note that the above line actually extends the data list.
        self.size += 1
        self.__bubbleUp(self.size-1)

    def pop(self):
        '''
        Removes and returns top of the heap
        :return: Item on top of the heap
        '''
        result = self.data[0]
        self.size -= 1
        if self.size > 0:
            self.data[0] = self.data.pop(self.size)
            # Note that the above line actually shrinks the data list.
            self.__bubbleDown(0)
        return result

    def __bool__(self):
        '''
        Defining thid method allows a heap to be used as a boolean value!
        See the while loops in the test code.
        :return: size of heap
        '''
        return self.size > 0

    def __str__(self):
        return "(" + str(self.size) + ")" + str(self.data)

def namecmp(n1, n2):
    '''
    Simple comparison function as an example.
    Assumes each name is (first, last) sequence
    :param n1: Name
    :param n2: Other name
    :return: True if n1 comes before n2
    '''
    return n1[1] < n2[1]

def main():
    # here's a min heap (comparison is less than)
    minh = Heap()
    print( "Heap starts as " + str(minh))
    for num in (5,3,7,2):
        print( "Adding", num )
        minh.insert(num)
        print( minh )
    print("POPPING", minh.pop())
    print(minh)
    for num in (1,8):
        print( "Adding", num )
        minh.insert(num)
        print(minh)
    print("Emptying heap:")
    while minh:
        print(minh.pop())
        print(minh)

    # here's a max heap
    maxh = Heap(lambda x,y: x > y)
    for num in (4,6,10,2,-1,3):
        maxh.insert(num)
    print("Emptying max heap:")
    while maxh:
        print(maxh.pop())

    # a heap of names, for some reason?
    nameheap = Heap(namecmp)
    nameheap.insert(('Sean','Strout'))
    nameheap.insert(('Zack','Butler'))
    nameheap.insert(('James','Heliotis'))
    nameheap.insert(('Alan','Turing'))
    print("Emptying name-tuple heap:")
    print(nameheap.pop())
    print(nameheap.pop())
    print(nameheap.pop())
    nameheap.insert(('Ada','Lovelace'))
    nameheap.insert(('Grace','Hopper'))
    while nameheap:
        print(nameheap.pop())

if __name__ == '__main__':
    main()