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
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
    
    def is_leaf(self):
        return (self.left == None and self.right == None)
    
    def is_root(self):
        return self.parent == None


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
    print(tokens)
    # root = Node(tokens[0])
    # parent_node = root
    node, previous_token = None, None
    for token in tokens:
        if token == '<':
            previous_token = '<'
        elif token == '>':
            previous_token = '>'
            if node.parent:
                node = node.parent
        elif token == ',':
            previous_token = ','
            if node.parent:
                node = node.parent
        else:
            node = Node(val=token, parent=node)
            if previous_token == '<':
                node.parent.left = node
            elif previous_token == ',':
                node.parent.right = node
    return node


class TestProblem03(unittest.TestCase):
    def test(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(serialize(node)).left.left.val, 'left.left')

        node = Node('1', Node('2', Node('4'), Node('5')), Node('3', Node('7')))
        self.assertEqual(serialize(node), ' 1  <  2  <  4  ,  5  >  ,  3  <  7  ,  >  > ')
        
        deserialized_node = deserialize(serialize(node))
        self.assertEqual(deserialized_node.val, '1')
        self.assertEqual(deserialized_node.left.val, '2')
        self.assertEqual(deserialized_node.left.left.val, '4')
        self.assertEqual(deserialized_node.left.right.val, '5')
        self.assertEqual(deserialized_node.right.val, '3')
        self.assertEqual(deserialized_node.right.left.val, '7')
        

if __name__ == '__main__':
    unittest.main()
