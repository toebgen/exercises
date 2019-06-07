import unittest


class ArrayList():
    def __init__(self, *args, **kwargs):
        # Instantiate initial fixed size array
        self.size = 1
        self.array = [None] * self.size
        self.index = -1  # Points to last used index in ArrayList
        self.extension_factor = 2

        return super().__init__(*args, **kwargs)
    

    def extend(self):
        """
        Extend current fixed array size by self.extension_factor.
        Copy saved content over.
        """
        new_size = self.size * self.extension_factor
        new_array = [None] * new_size
        new_array[:self.size] = self.array
        self.array = new_array
        self.size = new_size
        # Don't touch self.index
    

    def diminish(self):
        """
        Reduce current fixed array size by self.extension_factor.
        """
        if self.size <= 1:
            # Won't diminish further
            return

        new_size = int(self.size / self.extension_factor)
        new_array = self.array[:new_size]
        self.array = new_array
        self.size = new_size
        # Make sure this is pointing inside the current size
        self.index = self.size


    def append(self, value):
        """ Append at the end of array. Extend array size if necessary. """
        # TODO: Don't allow multiple values as parameter

        if (self.index + 1) == self.size:
            # Current array is full -> extend
            self.extend()
        self.array[self.index + 1] = value
        self.index += 1
    

    def pop(self):
        """
        RetRemove and return last element from the array
        """
        if (self.index < 0):
            # ArrayList is empty!
            return None

        last_element = self.array[self.index]
        self.array[self.index] = None
        self.index -= 1

        if self.index <= (self.size / self.extension_factor):
            self.diminish()

        return last_element


    def __getitem__(self, index):
        """ [] operator, return value """
        return self.array[index]
    

    def __len__(self):
        return self.index + 1
    

    def __in__(self, value):
        for val in self.array:
            if val == value:
                return True
        return False


class TestArrayList(unittest.TestCase):
    def appendWithDummyData(self, length):
        for x in range(length):
            self.array_list.append(x)

    
    def setUp(self):
        self.array_list = ArrayList()
        

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
