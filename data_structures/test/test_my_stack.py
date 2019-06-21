import unittest

from my_stack import MyStack


class TestMyStack(unittest.TestCase):
    def setUp(self):
        # Provide an empty stack
        self.stack = MyStack()

        # Provide a filled stack
        self.len_test_data = 5
        self.test_data = [i+1 for i in range(self.len_test_data)]
        self.filled_stack = MyStack()
        for i in self.test_data:
            self.filled_stack.push(i)
        
   
    def test_instantiation(self):
        stack = MyStack()
        self.assertEqual(None, stack.top)
        self.assertEqual(0, len(self.stack))
    

    def test_push(self):
        for i in self.test_data:
            self.stack.push(i)
            self.assertEqual(i, len(self.stack))
            self.assertEqual(i, self.stack.top.key)
    

    def test_pop(self):
        for i in reversed(self.test_data):
            data = self.filled_stack.pop()
            self.assertEqual(i-1, len(self.filled_stack))
            self.assertEqual(i, data)


    def test_peek(self):
        for i in reversed(self.test_data):
            data = self.filled_stack.peek()
            self.assertEqual(i, data)
            self.filled_stack.pop()


    def test_is_empty(self):
        stack = MyStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
