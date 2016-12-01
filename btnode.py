"""
CSCI-603: Trees (week 10)
Author: Sean Strout @ RIT CS

This is an implementation of a binary tree node.
"""

class BTNode:
    """
    A binary tree node contains:
     :slot val: A user defined value
     :slot left: A left child (BTNode or None)
     :slot right: A right child (BTNode or None)
    """

    __slots__ = "val", "left", "right"

    value = 0
    left1 = "kapil"
    def __init__(self, val, left=None, right=None):
        """
        Initialize a node.
        :param val: The value to store in the node
        :param left: The left child (BTNode or None)
        :param right: The right child (BTNode or None)
        :return: None
        """
        self.val = val
        self.left = left
        self.right = right

    def __eq__( self, other ):
        """
        :param other: Any other object
        :return: True iff
            1. type( other ) = BTNode
            2. the val slots in this node and the other node are equal
            3. this node's left and right nodes are equal to
               the other node's left and right nodes, respectively
        """
        return type( other ) == BTNode and \
                   self.val == other.val and \
                   self.left == other.left and \
                   self.right == other.right

    def preorder( self ):
        self.__preorder()
        print()

    def __preorder( self ):
        print( '(', end = " " )
        print( self.val, end = " " )
        if self.left is not None: self.left.__preorder(); print( end = " " )
        if self.right is not None: self.right.__preorder(); print( end = " " )
        print( ')', end = "" )

    def inorder( self ):
        self.__inorder()
        print()

    def __inorder( self ):
        print( '(', end = " " )
        if self.left is not None: self.left.__inorder(); print( end = " " )
        print( self.val, end = " " )
        if self.right is not None: self.right.__inorder(); print( end = " " )
        print( ')', end = "" )

    def postorder( self ):
        self.__postorder()
        print()

    def __postorder( self ):
        print( '(', end = " " )
        if self.left is not None: self.left.__postorder(); print( end = " " )
        if self.right is not None: self.right.__postorder(); print( end = " " )
        print( self.val, end = " " )
        print( ')', end = "" )

def testBTNode():
    """
    A test function for BTNode.
    :return: None
    """
    tree1 = BTNode( 30, BTNode( 10, BTNode( 40 ) ), BTNode( 20 ) )
    tree2 = BTNode( 30, BTNode( 10, "forty" ), BTNode( 20 ) )

    print( tree1 == tree2 )

    tree1.preorder()
    tree1.inorder()
    tree1.postorder()

if __name__ == '__main__':
    testBTNode()


def main():
    n =BTNode(9)

    print(n.value)
if __name__ == '__main__':
    main()