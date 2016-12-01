__author__ = 'dolek'

class TreeNode:
    __slots__ = 'value','left','right'

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

