import unittest

from my_tree import MyBinaryTree


class TestMyBinaryTree(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [1, 2, 3, 4, 8, 9]


    def test_instantiation(self):
        tree = MyBinaryTree()
        self.assertIsNotNone(tree)
        self.assertIsNone(tree.key)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)
        del tree

        key = 1
        tree = MyBinaryTree(key)
        self.assertIsNotNone(tree)
        self.assertEqual(tree.key, key)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)


    def test_create_from_sorted_list(self):
        """
        The result of [1, 2, 3, 4, 8, 9] should be:
                3
              /   \
            1      8
             \    / \
              2  4   9
        """
        sorted_list = []
        tree = MyBinaryTree.from_sorted_list(sorted_list)
        self.assertIsNone(tree)
        del tree

        tree = MyBinaryTree.from_sorted_list(self.sorted_list)
        self.assertEqual(tree.key, 3)
        self.assertEqual(tree.left.key, 1)
        self.assertEqual(tree.right.key, 8)
        self.assertIsNone(tree.left.left)
        self.assertEqual(tree.left.right.key, 2)
        self.assertEqual(tree.right.left.key, 4)
        self.assertEqual(tree.right.right.key, 9)



if __name__ == "__main__":
    unittest.main()
