import unittest

class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    
    def append(self, data):
        self.next = Node(data)
        return self.next


def create_singly_linked_list(n):
    if (n < 1):
        return None
    root = Node()
    node = root
    previous = None
    for i in range(n):
        if (previous == None):
            node.data = i
            node.next = None
        else:
            node = Node(i)
            previous.next = node
        previous = node
    return root


def delete_middle_node(middle_node):
    print('delete_middle_node:', middle_node.data)
    middle_node.data = middle_node.next.data
    middle_node.next = middle_node.next.next


def print_singly_linked_list(root):
    print('Singly linked list:')
    while (root.next != None):
        print(root)
        root = root.next
    print(root)
        

def get_nth_node(n, root):
    for _ in range(n):
        root = root.next
    return root


def add_lists(l1, l2):
    print('add_lists')
    root, prev = None, None
    carry = 0
    while (l1 != None):
        result = Node()
        if (root == None):
            root = result
        
        digit_sum = l1.data + l2.data + carry
        carry = int(digit_sum / 10)
        result.data = digit_sum % 10

        if (prev != None):
            prev.next = result
        prev = result
        if (l1.next != None):
            l1 = l1.next
            l2 = l2.next
        else:
            if (carry != 0):
                result = Node(carry)
                prev.next = result
            break
    return root


def as_array(l):
    if (l == None):
        return None
    
    a = []
    while(True):
        a.append(l.data)

        if (l.next != None):
            l = l.next
        else:
            break
        
    return a


def as_list(arr):
    if (len(arr) <= 0):
        return None
    
    root, node = None, None
    for d in arr:
        if(node == None):
            node = Node(d)
            root = node
        else:
            node = node.append(d)
    
    return root



class TestHashMap(unittest.TestCase):
    # def setUp(self):
    #     pass
    
    def testGetNthNode(self):
        l = create_singly_linked_list(9)
        nth = get_nth_node(3, l)
        # print_singly_linked_list(l)
        self.assertEqual(nth.data, 3)
    
    def testAsListAndAsArray(self):
        arr = [1, 2, 3, 4, 5]
        l = as_list(arr)
        arr2 = as_array(l)
        self.assertEqual(arr, arr2)
    
    def testDeleteMiddleNode(self):
        arr = [1, 2, 3, 4, 5]
        l = as_list(arr)
        fourth_node = get_nth_node(3, l)
        expected = [1, 2, 3, 5]
        delete_middle_node(fourth_node)
        self.assertEqual(expected, as_array(l))
    
    def testAddLists(self):
        l1 = as_list([7, 1, 6])
        l2 = as_list([5, 9 ,2])
        expected = [2, 1, 9]
        self.assertEqual(expected, as_array(add_lists(l1, l2)))

if __name__ == '__main__':
    unittest.main()
