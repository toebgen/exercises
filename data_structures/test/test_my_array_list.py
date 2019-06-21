import unittest

from my_array_list import MyArrayList


class TestMyArrayList(unittest.TestCase):
    def appendWithDummyData(self, length):
        for x in range(length):
            self.array_list.append(x)

    
    def setUp(self):
        self.array_list = MyArrayList()
        

    def testExtend(self):
        expected_size_after = self.array_list.size * self.array_list.extension_factor
        self.array_list.extend()
        self.assertEqual(self.array_list.size, expected_size_after)


    def testDiminish(self):
        self.appendWithDummyData(9)
        expected_size_after = 8
        expected_index_after = 8
        self.array_list.diminish()
        self.assertEqual(self.array_list.size, expected_size_after)
        self.assertEqual(self.array_list.index, expected_index_after)
    
    
    def testAppend(self):
        self.assertEqual(len(self.array_list), 0)
        test_values = [x for x in range(10)]
        for counter, test_value in enumerate(test_values, 1):
            self.array_list.append(test_value)
            self.assertEqual(len(self.array_list), counter)
            self.assertEqual(self.array_list[counter-1], test_value)
            # TODO Test self.array_list.size ?
    

    def testPop(self):
        # Add 5 values
        self.appendWithDummyData(5)
        expected_value = 4
        # Pop 1 value, hence 4 should be left
        expected_size_after = 4
        expected_index_after = 4
        popped_value = self.array_list.pop()
        self.assertEqual(popped_value, expected_value)
        self.assertEqual(self.array_list.size, expected_size_after)
        self.assertEqual(self.array_list.index, expected_index_after)
    

    def testOperatorIn(self):
        self.appendWithDummyData(3)
        self.assertEqual(1 in self.array_list, True)
        self.assertEqual(4 in self.array_list, False)
                

if __name__ == '__main__':
    unittest.main()
