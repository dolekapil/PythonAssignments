"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS
Author: James Heliotis @ RIT CS

This is an implementation of a binary search tree.
It includes the solution to a quiz question: 'num_less'.
Note the static methods.
"""

from btnode import BTNode

class BST:
    """
    A binary search tree consists of:
    :slot root: The root node of the tree (BTNode)
    :slot size: The size of the tree (int)
    """
    __slots__ = "root", "size"


    def __init__(self):
        """
        Initialize an empty tree.
        :return: None
        """
        self.root = None
        self.size = 0

    @staticmethod
    def __size(node):
        if node is None:
            return 0
        else:
            return BST.__size( node.left ) + 1 + BST.__size( node.right )

    def __insert(self, val, node):
        """
        The recursive helper function for inserting a new value into the tree.
        :param val: The value to insert
        :param node: The current node in the tree (BTNode)
        :return: None
        """
        if val < node.val:
            if node.left is not None:
                self.__insert( val, node.left )
            else:
                node.left = BTNode( val )
                self.size += 1
        elif val > node.val:
            if node.right is not None:
                self.__insert( val, node.right )
            else:
                node.right = BTNode( val )
                self.size += 1
        # else do nothing; OUR binary search tree is a set.

    # TIME COMPLEXITY?
    #
    def insert(self, val):
        """
        Insert a new value into the tree
        :param val: The value to insert
        :return: None
        """   
        if self.root == None:
            self.root = BTNode( val )
            self.size = 1
        else:
            self.__insert( val, self.root )

    def __contains(self, val, node):
        """
        The recursive helper function for checking if a value is in the tree.
        :param val: The value to search for
        :param node: The current node (BTNode)
        :return: True if val is present, False otherwise
        """
        if node is None:
            return False
        elif val == node.val:
            return True
        elif val < node.val:
            return self.__contains( val, node.left )
        else:
            return self.__contains( val, node.right )

    # TIME COMPLEXITY: O(N), but we hope log N
    #
    def contains(self, val):
        """
        Returns whether a value is in the tree or not.
        :param val: The value to search for
        :return: True if val is present, False otherwise
        """
        return self.__contains( val, self.root )

    def __height(self, node):
        """
        The recursive helper function for computing the height of a node
        :param node: The current node (BTNode)
        :return: The height of node (int)
        """
        if node is None:
            return -1
        else:
            return 1 + max( self.__height( node.left ), \
                            self.__height( node.right ) )

    # TIME COMPLEXITY: O(N), N no matter what.
    #
    def height(self):
        """
        Return the height of a tree.  Recall:
            - The height of an empty tree is -1
            - The height of a tree with one node is 0
            - Otherwise the height is one plus the larger of the heights of
            the left or right children.
        :return: The height (int)
        """
        return self.__height( self.root )

    def __inorder(self, node):
        """
        The recursive inorder traversal function that builds a string
        representation of the tree.
        :param node: The current node (BTNode)
        :return: A string of the tree, e.g. "1 2 5 9 "
        """
        if node is None:
            return ""
        else:
            return self.__inorder( node.left ) + \
                   str( node.val ) + " " + \
                   self.__inorder( node.right )

    # TIME COMPLEXITY: O(N)
    #
    def __str__(self):
        """
        Return a string representation of the tree.  By default this will
        be a string with the values in order.
        :return:
        """
        return self.__inorder( self.root )

    def num_less(self,x):
        return BST.__num_less(self.root,x)

    @staticmethod
    def __num_less(node,x):
        if node is None:
            return 0
        elif node.val < x:
            return BST.__size(node.left) + 1 + BST.__num_less(node.right,x)
        else:
            return BST.__num_less(node.left,x)

def testBST():
    """
    Test function for the binary search tree.
    :return: None
    """
    # empty tree
    t0 = BST()
    print('t0:', t0)
    print('t0 size (0):', t0.size)
    print('t0 contains 10 (False)?', t0.contains(10))
    print('t0 height (-1)?', t0.height())

    # single node tree
    t1 = BST()
    t1.insert(10)
    print('t1:', t1)
    print('t1 size (1):', t1.size)
    print('t1 contains 10 (True)?', t1.contains(10))
    print('t1 contains 0 (False)?', t1.contains(0))
    print('t1 height (0)?', t1.height())

    # tree with a parent (20), left child (10) and right child (30)
    t2 = BST()
    for val in (20, 10, 30): t2.insert(val)
    print('t2:', t2)
    print('t2 size (3):', t2.size)
    print('t2 contains 30 (True)?', t2.contains(30))
    print('t2 contains 0 (False)?', t2.contains(0))
    print('t2 height (1)?', t2.height())

    # a larger tree
    t3 = BST()
    for val in (17, 5, 35, 2, 16, 29, 38, 19, 33): t3.insert(val)
    print('t3:', t3)
    print('t3 size (9):', t3.size)
    print('t3 contains 16 (True)?', t3.contains(16))
    print('t3 contains 0 (False)?', t3.contains(0))
    print('t3 height (3)?', t3.height())

    for x in 2,4,15,16,17,18,20,30,34,37,39:
        print( "#Nodes <", x, "=", t3.num_less( x ) )

if __name__ == '__main__':
    testBST()
