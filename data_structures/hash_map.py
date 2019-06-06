import unittest


class HashMap():
    def __init__(self, *args, **kwargs):
        # Instantiate initial fixed size array
        self.array_length = 64
        self.array = [None] * self.array_length
        self.num_saved_elements = 0

        return super().__init__(*args, **kwargs)
    

    def key2index(self, key):
        return key % self.array_length


    def insert(self, key, value):
        """ insert value at key to the map """
        index = self.key2index(key)
        if self.array[index] == None:
            self.array[index] = value
        else:
            self.array[index].append(value)
        self.num_saved_elements += 1
    

    def __getitem__(self, key):
        """ [key] operator, return value """
        index = self.key2index(key)
        return self.array[index]
    

    def fill_ratio(self):
        return float(self.num_saved_elements / self.array_length)


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.map = HashMap()

        get_n_test_cases = lambda n : [(i, 'val'+str(i)) for i in range(n)]
        self.test_cases = get_n_test_cases(10)
        # self.test_cases.append((100, 'val100'))
        # self.test_cases.append((1000, 'val1000'))
        # self.test_cases.append((111111, 'val11111'))
        print(self.test_cases)
    
    
    def testInsertAndAccessSingle(self):
        pair1 = (1, 'tree')
        self.map.insert(pair1[0], pair1[1])
        self.assertEqual(self.map[pair1[0]], pair1[1])
    

    def testInsertAndAccessMany(self):
        for key, value in self.test_cases:
            self.map.insert(key, value)
            self.assertEqual(self.map[key], value)
            

if __name__ == '__main__':
    unittest.main()
