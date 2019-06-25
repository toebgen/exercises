import math
from collections import defaultdict

from my_queue import MyQueue


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


    def list_of_depths(self):
        """
        Create a linked list of all the nodes at each depth.
        For example, a tree with depth D has D linked lists.
        """
        queue = MyQueue()
        the_dict = defaultdict(list)
        level = 0
        
        queue.push((self, level))
        while (queue.is_empty() == False):
            node, level = queue.pop()
            the_dict[level].append(node.key)
            if (node.left != None):
                queue.push((node.left, level+1))
            if (node.right != None):
                queue.push((node.right, level+1))
        
        return the_dict


    def height_of_balanced(self):
        """
        Returns height of tree. Raises Attribute Error if unbalanced tree given.
        TODO: Certainly not the best way of solving it right now...
        """
        if (self.left is None and self.right is None):
            return 1  # Leaf, recursion base case
        
        height_left, height_right = 0, 0
        if (self.left is not None):
            height_left = self.left.height_of_balanced()
        if (self.right is not None):
            height_right = self.right.height_of_balanced()

        if (abs(height_left - height_right) > 1):
            raise AttributeError
        height = max(height_left, height_right) + 1

        return height


    def is_balanced(self):
        """
        Tree is balanced if the heights of 2 sub-trees of any node never differ
        by more than 1.
        """
        try:
            self.height_of_balanced()
        except AttributeError:
            return False
        return True
