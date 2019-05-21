import unittest

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def is_leaf(self):
        return (self.left == None and self.right == None)


def serialize(node):
    serialized_str = ' ' + str(node.val) + ' '
    if node.is_leaf():
        return serialized_str
    serialized_str += ' < '
    if node.left != None:
        serialized_str += serialize(node.left)
    serialized_str += ' , '
    if node.right != None:
        serialized_str += serialize(node.right)
    serialized_str += ' > '
    return serialized_str


def deserialize(serialized_str):
    tokens = [token for token in serialized_str.split(' ') if token]
    if len(tokens)<1:
        return None
    pass


class TestProblem03(unittest.TestCase):
    def test(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        node = Node('1', Node('2', Node('4'), Node('5')), Node('3', Node('7')))
        print("serialize:", serialize(node))
        # self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')


if __name__ == '__main__':
    unittest.main()
