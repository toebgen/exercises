
class MyLinkedList():
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next
    
    
    def __str__(self):
        result_str = '['
        node = self
        while(node.next != None):
            result_str += str(node.key) + ', '
            node = node.next
        result_str += str(node.key) + ']'
        return result_str
    
    
    def append(self, key):
        """ Appends key to self """
        started_from = self
        runner = self
        while(runner.next != None):
            runner = runner.next
        runner.next = MyLinkedList(key=key, next=None)
        return started_from


    def to_list(self):
        return self.as_list(self)
    
    
    @staticmethod
    def create_with_n_elements(n):
        if (n < 1):
            return None
        root = MyLinkedList()
        node = root
        previous = None
        for i in range(n):
            if (previous == None):
                node.key = i
                node.next = None
            else:
                node = MyLinkedList(i, None)
                previous.next = node
            previous = node
        return root


    @staticmethod
    def delete_middle_node(middle_node):
        middle_node.key = middle_node.next.key
        middle_node.next = middle_node.next.next


    @staticmethod
    def print_singly_linked_list(root):
        print('Singly linked list:')
        while (root.next != None):
            print(root)
            root = root.next
        print(root)
        

    @staticmethod
    def get_nth_node(n, root):
        for _ in range(n):
            root = root.next
        return root


    @staticmethod
    def add_lists(l1, l2):
        root, prev = None, None
        carry = 0
        while (l1 != None):
            result = MyLinkedList()
            if (root == None):
                root = result
            
            digit_sum = l1.key + l2.key + carry
            carry = int(digit_sum / 10)
            result.key = digit_sum % 10

            if (prev != None):
                prev.next = result
            prev = result
            if (l1.next != None):
                l1 = l1.next
                l2 = l2.next
            else:
                if (carry != 0):
                    result = MyLinkedList(carry)
                    prev.next = result
                break
        return root


    @staticmethod
    def as_list(the_linked_list):
        """ Returns given  MyLinkedList as (python) list """
        if (the_linked_list == None):
            return None
        
        result_list = []
        while(True):
            result_list.append(the_linked_list.key)

            if (the_linked_list.next != None):
                the_linked_list = the_linked_list.next
            else:
                break
            
        return result_list


    @staticmethod
    def create_from_list(the_list):
        if (len(the_list) <= 0):
            return None
        
        root, node = None, None
        for d in the_list:
            if(node == None):
                node = MyLinkedList(d)
                root = node
            else:
                node = node.append(d)
        
        return root
