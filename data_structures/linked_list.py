
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


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


if __name__ == '__main__':
    root = create_singly_linked_list(10)
    print('root:', root)
    print_singly_linked_list(root)
    nth_node = get_nth_node(3, root)
    print('nth_node:', nth_node)
    delete_middle_node(nth_node)
    print_singly_linked_list(root)

    l1 = create_singly_linked_list(1)
    l2 = create_singly_linked_list(1)
    l1.data = 8
    l2.data = 5
    print_singly_linked_list(l1)
    print_singly_linked_list(l2)
    result = add_lists(l1, l2)
    print_singly_linked_list(result)
