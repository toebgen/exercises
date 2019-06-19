import math


class MyBinaryTree():

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


    def to_list(self):
        """
        Write instance to a list in the form of
        [root, root.left, root.right, root.left.left, root.left.right, root.right.left, ...]
        Breadth first search so to say.
        """
        pass


    @classmethod
    def from_sorted_list(cls, sorted_list, start=None, end=None):
        """
        Given a sorted (increasing order) list with unique integer elements, create a binary search tree with minimal height.
        """
        length = len(sorted_list)
        if (length <= 0):
            return None
        
        # Initialize indices on first call
        if (start == None):
            start = 0
        if (end == None):
            end = length - 1
        if (end < start):
            return None
        
        mid_idx = int((start+end) / 2)
        root = MyBinaryTree(sorted_list[mid_idx])
        root.left = MyBinaryTree.from_sorted_list(sorted_list, start, mid_idx-1)
        root.right = MyBinaryTree.from_sorted_list(sorted_list, mid_idx+1, end)
        
        return root
