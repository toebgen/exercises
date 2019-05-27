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
