import unittest

"""
Problem #8 [Easy]
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""


class Node:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
     
    def is_leaf(self):
        return (self.left == None and self.right == None)



"""
The better (O(n) time) solution:
"""
def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False


"""
The O(n^2) time solution
"""

def is_unival_subtree(node, value):
    if node is None:
        return True
    if node.val == value:
        # Traverse deeper down the tree
        return is_unival_subtree(node.left, value) and is_unival_subtree(node.right, value)

def num_unival_subtrees(node):
    if node is None:
        return 0
    
    left = num_unival_subtrees(node.left)
    right = num_unival_subtrees(node.right)

    if is_unival_subtree(node, node.val):
        return 1 + left + right
    else:
        return left + right


class TestProblem08(unittest.TestCase):
    def test(self):
        root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        self.assertEqual(num_unival_subtrees(root), 5)

        root = Node('a', Node('c'), Node('b', Node('b'), Node('b', None, Node('b'))))
        self.assertEqual(num_unival_subtrees(root), 5)


if __name__ == '__main__':
    unittest.main()
