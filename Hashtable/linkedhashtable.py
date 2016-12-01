__author__ = 'dolek'

from chainnode import ChainNode
from set import SetType
class LinkedHashTable(SetType):

    __slots__ = 'front', 'back', 'size', 'table', 'LOAD_LIMIT', 'filled'


    def __init__(self, initial_num_buckets=100, load_limit=0.75):
        """
        Create a new empty hash table.
        :param initial_num_buckets: starting number_of_buckets
        :param load_limit: See class documentation above.
        :return:
        """
        self.size = initial_num_buckets
        self.front = None
        self.back = None
        self.table = [None for counter in range(initial_num_buckets)]
        self.LOAD_LIMIT = load_limit
        self

    def hashing(self,string):
        total = 0
        str_list = list(string)
        for index in range(len(list)):
            total += ord(list[index]) * (index ** 2)
        total = total % self.size
        return total

    def add(self, obj):
        """
        Insert a new object into the hash table and remember when it was added
        relative to other calls to this method. However, if the object is
        added multiple times, the hash table is left unchanged, including the
        fact that this object's location in the insertion order does not change.
        Double the size of the table if its load_factor exceeds the load_limit.
        :param obj: the object to add
        :return: None
        """
        n = ChainNode(obj)
        self.size += 1
        if self.front == None:
            self .front = n
            self.back = n

        if self.size >=

