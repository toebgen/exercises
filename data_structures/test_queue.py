import unittest

from my_queue import MyQueue


class TestMyQueue(unittest.TestCase):
    def setUp(self):
        # Provide empty queue
        self.queue = MyQueue()

        # Provide filled queue
        self.len_test_data = 5
        self.test_data = [i+1 for i in range(self.len_test_data)]
        self.filled_queue = MyQueue()
        for i in self.test_data:
            self.filled_queue.push(i)


    def test_instantiation(self):
        queue = MyQueue()
        self.assertIsNotNone(queue)
        self.assertIsNone(queue.latest.top)
        self.assertIsNone(queue.oldest.top)
    

    def test_len(self):
        # Push and pop repeatedly, still one stack should always be empty
        self.assertEqual(0, len(self.queue))
        self.assertEqual(0, len(self.queue.latest))
        self.assertEqual(0, len(self.queue.oldest))

        self.queue.push(1)
        self.queue.push(1)
        self.assertEqual(2, len(self.queue))
        self.assertEqual(2, len(self.queue.latest))
        self.assertEqual(0, len(self.queue.oldest))

        self.queue.pop()
        self.assertEqual(1, len(self.queue))
        self.assertEqual(0, len(self.queue.latest))
        self.assertEqual(1, len(self.queue.oldest))


    def test_push(self):
        for i in self.test_data:
            self.queue.push(i)
            self.assertEqual(i, len(self.queue))
            self.assertEqual(i, len(self.queue.latest))
            self.assertEqual(0, len(self.queue.oldest))
            self.assertEqual(i, self.queue.latest.top.data)


    def test_pop(self):
        for i in self.test_data:
            data = self.filled_queue.pop()
            self.assertEqual(data, i)
            self.assertEqual(self.len_test_data - i, len(self.filled_queue))
            self.assertEqual(0, len(self.filled_queue.latest))
            self.assertEqual(self.len_test_data - i, len(self.filled_queue.oldest))
            if (i < self.len_test_data):
                self.assertEqual(i+1, self.filled_queue.oldest.top.data)


if __name__ == '__main__':
    unittest.main()
