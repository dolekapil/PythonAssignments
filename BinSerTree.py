__author__ = 'dolek'

from MyTreeNode import TreeNode
class BST:
    __slots__ = 'root','size'

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,value):
        r= self.root
        if r is None:
            self.root = TreeNode(value)
        else:
            self.__insert(value,r)
        self.size+=1

    def __insert(self,value,node):
        if value < node.value:
            if node.left is not None:
                self.__insert(value,node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self.__insert(value,node.right)
            else:
                node.right = TreeNode(value)

    def __str__(self):

        return "inorder "+self.inOrder(self.root)

    def inOrder(self,node):
        if node is None:
            return " "
        else:
            return self.inOrder(node.left)+str(node.value)+self.inOrder(node.right)
    def height(self):
        if self.root is None:
            return 0
        else:
            return self.__height(self.root)
    def __height(self,node):
        if node is None:
            return 0
        else:
            return 1+max(self.__height(node.left),self.__height(node.right))

    def contains(self,value):
        return self.__contains(self.root,value)
    def __contains(self,node,value):
        if node is None:
            return False
        else:
            if value<node.value:
                return self.__contains(node.left,value)
            elif value>node.value:
                return self.__contains(node.right,value)
            else:
                return True
def main():
    n = BST()
    n.insert(10)
    print(n)
    n.insert(5)
    n.insert(12)
    print(n)
    print(n.height())
    print(n.contains(1))

if __name__ == '__main__':
    main()