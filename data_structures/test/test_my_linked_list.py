import unittest

from my_linked_list import MyLinkedList, MyLinkedListTools


class TestMyLinkedList(unittest.TestCase):

    def test_str(self):
        linked_list = MyLinkedList.create_from_list([1, 2, 3])
        expected_string = '[1, 2, 3]'
        self.assertEqual(str(linked_list), expected_string)


    def test_eq(self):
        linked_list_1 = MyLinkedList.create_from_list([1, 2, 3])
        linked_list_2 = MyLinkedList.create_from_list([1, 2, 3])
        self.assertEqual(linked_list_1, linked_list_2)

        linked_list_1 = MyLinkedList.create_from_list([1, 2])
        linked_list_2 = MyLinkedList.create_from_list([1, 2, 3])
        self.assertNotEqual(linked_list_1, linked_list_2)

        linked_list_1 = MyLinkedList.create_from_list([1, 2, 3])
        linked_list_2 = MyLinkedList.create_from_list([1, 2])
        self.assertNotEqual(linked_list_1, linked_list_2)


    def test_append(self):
        expected_list = [1, 2]
        linked_list = MyLinkedList.create_from_list(expected_list[:1])
        linked_list.append(expected_list[-1])
        self.assertListEqual(expected_list, linked_list.to_list())

        expected_list = [1, 2, 3]
        linked_list = MyLinkedList.create_from_list(expected_list[:2])
        linked_list.append(expected_list[-1])
        self.assertListEqual(expected_list, linked_list.to_list())

    
    def test_get_nth_node(self):
        l = MyLinkedList.create_with_n_elements(9)
        nth = MyLinkedList.get_nth_node(3, l)
        self.assertEqual(nth.key, 3)
    

    def test_create_from_list_and_as_array(self):
        arr = [1, 2, 3, 4, 5]
        l = MyLinkedList.create_from_list(arr)
        arr2 = MyLinkedList.as_list(l)
        self.assertEqual(arr, arr2)
    

    def test_delete_middle_node(self):
        arr = [1, 2, 3, 4, 5]
        l = MyLinkedList.create_from_list(arr)
        fourth_node = MyLinkedList.get_nth_node(3, l)
        expected = [1, 2, 3, 5]
        MyLinkedList.delete_middle_node(fourth_node)
        self.assertEqual(expected, MyLinkedList.as_list(l))
    

    def test_add_lists(self):
        l1 = MyLinkedList.create_from_list([7, 1, 6])
        l2 = MyLinkedList.create_from_list([5, 9 ,2])
        expected = [2, 1, 9]
        self.assertEqual(expected, MyLinkedList.as_list(MyLinkedList.add_lists(l1, l2)))


class TestMyLinkedListTools(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = [
            # test_case, reversed, is_palindrome
            ([1, 2, 3], [3, 2, 1], False),
            ([1, 2, 1], [1, 2, 1], True),

            (['a', 'b', 'c'], ['c', 'b', 'a'], False),
            (['a', 'b', 'a'], ['a', 'b', 'a'], True),

            # (['abc'], ['cba'], False),
            # (['aba'], ['aba'], True),
        ]


    def test_reverse(self):
        for test_case, expected_reversed, _ in self.test_cases:
            linked_list = MyLinkedList.create_from_list(test_case)
            reversed_linked_list = MyLinkedListTools.reverse(linked_list)
            reversed_list = reversed_linked_list.to_list()
            self.assertEqual(expected_reversed, reversed_list)
        pass
        
    
    def test_is_palindrome(self):
        for test_case, _, is_palindrome in self.test_cases:
            linked_list = MyLinkedList.create_from_list(test_case)
            self.assertEqual(MyLinkedListTools.is_palindrome(linked_list), is_palindrome)


if __name__ == '__main__':
    unittest.main()
