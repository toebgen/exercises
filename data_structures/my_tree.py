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
    def from_sorted_list(cls, sorted_list):
        """
        Given a sorted (increasing order) list with unique integer elements, create a binary search tree with minimal height.
        """
        length = len(sorted_list)
        if (length <= 0):
            return None
        
        get_mid_idx = lambda first, last: int(first + (last-first)/2)
        mid_idx = get_mid_idx(0, length)
        if (length%2 != 0 and length > 1):
            # Ensure the balancing of the tree to be filled from the left,
            # hence use the right value in case of an even sized array (where
            # there is no 'real' middle index).
            mid_idx += 1

        root = MyBinaryTree(sorted_list[mid_idx])
        root.left = MyBinaryTree.from_sorted_list(sorted_list[:mid_idx])
        if (mid_idx+1 < length):
            root.right = MyBinaryTree.from_sorted_list(sorted_list[mid_idx+1:])
        else:
            root.right = None

        return root
