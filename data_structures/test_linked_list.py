import unittest

from linked_list import Node

class TestHashMap(unittest.TestCase):
    # def setUp(self):
    #     pass
    
    def testGetNthNode(self):
        l = Node.create_singly_linked_list(9)
        nth = Node.get_nth_node(3, l)
        # print_singly_linked_list(l)
        self.assertEqual(nth.data, 3)
    
    def testAsListAndAsArray(self):
        arr = [1, 2, 3, 4, 5]
        l = Node.as_list(arr)
        arr2 = Node.as_array(l)
        self.assertEqual(arr, arr2)
    
    def testDeleteMiddleNode(self):
        arr = [1, 2, 3, 4, 5]
        l = Node.as_list(arr)
        fourth_node = Node.get_nth_node(3, l)
        expected = [1, 2, 3, 5]
        Node.delete_middle_node(fourth_node)
        self.assertEqual(expected, Node.as_array(l))
    
    def testAddLists(self):
        l1 = Node.as_list([7, 1, 6])
        l2 = Node.as_list([5, 9 ,2])
        expected = [2, 1, 9]
        self.assertEqual(expected, Node.as_array(Node.add_lists(l1, l2)))

if __name__ == '__main__':
    unittest.main()
