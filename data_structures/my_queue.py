from my_stack import MyStack


class MyQueue():
    """ Queue implementation using 2 stacks """

    def __init__(self):
        self.latest = MyStack()
        self.oldest = MyStack()
    

    def __len__(self):
        # Data in Queue should always be in one of the two internal stacks
        len_latest, len_oldest = len(self.latest), len(self.oldest)
        if (len_latest > len_oldest):
            return len_latest
        return len_oldest


    def is_empty(self):
        return self.latest.is_empty() and self.oldest.is_empty()


    def move(self, from_stack, to_stack):
        """ Move top element from from_stack (pop) onto to_stack (push) """
        to_stack.push(from_stack.pop())


    def push(self, data):
        while (self.oldest.is_empty() != True):
            self.move(self.oldest, self.latest)
        self.latest.push(data)
    

    def pop(self):
        while(self.latest.is_empty() != True):
            self.move(self.latest, self.oldest)
        return self.oldest.pop()
    