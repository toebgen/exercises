from my_linked_list import MyNode


class MyStack():
    """
    Simple Stack implementation using a LinkedList.
    """
    
    def __init__(self):
        """ Initialize empty stack, self.top is always pointing to latest element """
        self.top = None
    
        
    def __len__(self):
        """ Naive implementation, would be better to hold a separate len member. """
        if self.top == None:
            return 0

        len = 1
        runner = self.top
        while(runner.next != None):
            len += 1
            runner = runner.next
        return len
    
    
    def push(self, data):
        """
        Push in front of current top.
        Example: Pushing 1, 2 and then 3 results in: 3->2->1.
        """
        new = MyNode(data)
        new.next = self.top
        self.top = new
        return self.top
    

    def pop(self):
        """ Remove and return latest element (top) from stack """
        data = self.top.data
        self.top = self.top.next
        return data
    

    def peek(self):
        return self.top.data
    

    def is_empty(self):
        return self.top == None
