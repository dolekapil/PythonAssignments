__author__ = 'zjb'

import node

class LinkedList:
    __slots__ = ('__front', '__size')

    def __init__(self):
        self.__front = None
        self.__size = 0

    def add_front(self,val):
        newnode = node.Node(val,self.__front)
        self.__front = newnode
        self.__size += 1

    def append(self,val):
        if self.__front == None:
            self.__front = node.Node(val)
        else:
            ptr = self.__front
            while ptr.link != None:
                ptr = ptr.link
            newnode = node.Node(val)
            ptr.link = newnode
        self.__size += 1

    def start(self):
        '''
        give me a pointer into the list, initially at front
        :return:
        '''
        return self.__front

    def is_off(self,cursor):
        return cursor == None

    def next(self,cursor):
        if cursor == None:
            raise ValueError()
        return cursor.link

    def get_val(self,cursor):
        return cursor.value

    def insert(self,cursor,val):
        '''
        insert after the cursor
        '''
        if cursor == None:
            raise ValueError
        newnode = node.Node(val,cursor.link)
        cursor.link = newnode
        self.__size += 1

    def update(self,cursor,val):
        if cursor == None:
            raise ValueError()
        cursor.value = val

    def remove_after(self,cursor):
        if cursor == None:
            raise ValueError()
        if cursor.link != None:
            cursor.link = cursor.link.link
        self.__size -= 1

    def remove(self,cursor):
        '''
        this is good practice, not good practice(s)
        '''
        if cursor == None:
            raise ValueError()
        if cursor == self.__front:
            self.__front = self.__front.link
        else:
            ptr = self.__front
            while ptr.link != cursor:
                ptr = ptr.link
            ptr.link = cursor.link
        self.__size -= 1
        #cursor = cursor.link --- doesn't effect caller's cursor
        # return something - removed value, probably?

    def size(self):
        return self.__size

def print_list(thelist):
    '''
    prints the list using cursor.  Note we have no idea
    what data type the cursor is!
    :return:
    '''
    cursor = thelist.start()
    while not thelist.is_off(cursor):
        print(thelist.get_val(cursor))
        cursor = thelist.next(cursor)

def main():
    ll = LinkedList()
    l2=LinkedList()
    l2= l1
    ll.append('first')
    print('size: ' + str(ll.size()))
    ll.append('second')
    ll.add_front('third')
    print_list(ll)
    print('size: ' + str(ll.size()))

    cursor = ll.start()
    #cursor = ll.next(cursor)
    ll.remove(cursor)
    print_list(ll)
    print('size: ' + str(ll.size()))




if __name__ == '__main__':
    main()