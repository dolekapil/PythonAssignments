__author__ = 'dolek'

class ChainNode:
    __slots__ = 'obj', 'prev', 'link', 'chain'

    def __init__(self, obj, prev=None, link=None, chain=None):
        self.obj = obj
        self.prev = prev
        self.link = link
        self.chain = chain