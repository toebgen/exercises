import unittest

from my_tree import MyBinaryTree


class TestMyBinaryTree(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [1, 2, 3, 4, 8, 9]
        
        #           1
        #       2       3
        #     4  5     6
        self.balanced_tree = MyBinaryTree(1,
            MyBinaryTree(2,
                MyBinaryTree(4), MyBinaryTree(5)),
            MyBinaryTree(3,
                MyBinaryTree(6), None)
        )

        #           1
        #       2
        #     4  5
        self.non_balanced_tree = MyBinaryTree(1,
            MyBinaryTree(2,
                MyBinaryTree(4), MyBinaryTree(5))
        )


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


    def test_list_of_depths(self):
        tree = MyBinaryTree.from_sorted_list(self.sorted_list)
        expected_list_of_depths = {
            0: [3],
            1: [1, 8],
            2: [2, 4, 9]
        }
        list_of_depths = tree.list_of_depths()
        self.assertDictEqual(expected_list_of_depths, list_of_depths)


    def test_height_of_balanced(self):
        self.assertEqual(self.balanced_tree.height_of_balanced(), 3)
        self.assertEqual(self.balanced_tree.left.height_of_balanced(), 2)
        self.assertEqual(self.balanced_tree.left.left.height_of_balanced(), 1)
        self.assertEqual(self.balanced_tree.left.right.height_of_balanced(), 1)
        self.assertEqual(self.balanced_tree.right.height_of_balanced(), 2)
        self.assertEqual(self.balanced_tree.right.left.height_of_balanced(), 1)

        with self.assertRaises(AttributeError):
            self.non_balanced_tree.height_of_balanced()


    def test_is_balanced(self):
        self.assertTrue(self.balanced_tree.is_balanced())
        self.assertTrue(self.balanced_tree.left.is_balanced())
        self.assertTrue(self.balanced_tree.right.is_balanced())

        self.assertFalse(self.non_balanced_tree.is_balanced())
        self.assertTrue(self.non_balanced_tree.left.is_balanced())



if __name__ == "__main__":
    unittest.main()
