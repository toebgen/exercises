import unittest

from my_tree import MyBinaryTree


class TestMyBinaryTree(unittest.TestCase):
    
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
        The result of [1, 3, 8, 9] should be:
                8
              /   \
            3      9
           /
          1
        """
        sorted_list = []
        tree = MyBinaryTree.from_sorted_list(sorted_list)
        self.assertIsNone(tree)
        del tree

        sorted_list = [1, 3, 8, 9]
        tree = MyBinaryTree.from_sorted_list(sorted_list)
        self.assertEqual(tree.key, 8)
        self.assertEqual(tree.left.key, 3)
        self.assertEqual(tree.right.key, 9)
        self.assertEqual(tree.left.left.key, 1)
        self.assertIsNone(tree.left.right)
        self.assertIsNone(tree.right.left)
        self.assertIsNone(tree.right.right)


if __name__ == "__main__":
    unittest.main()
