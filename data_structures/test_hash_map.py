import unittest

from hash_map import HashMap

class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.map = HashMap()

        get_n_test_cases = lambda n : [(i, 'val'+str(i)) for i in range(n)]
        self.test_cases = get_n_test_cases(99)

        # The following cases will cause collisions
        self.test_cases.append((100, 'val100'))
        self.test_cases.append((1000, 'val1000'))
        self.test_cases.append((111111, 'val11111'))
    
    
    def test_insert_and_access_single(self):
        pair1 = (1, 'tree')
        self.map.insert(pair1[0], pair1[1])
        self.assertEqual(self.map[pair1[0]], pair1[1])
    

    def test_insert_and_access_many_no_collisions(self):
        for key, value in self.test_cases[:10]:
            self.map.insert(key, value)
            self.assertEqual(self.map[key], value)


    def test_insert_and_access_many_with_collisions(self):
        for key, value in self.test_cases:
            self.map.insert(key, value)
            self.assertEqual(self.map[key], value)
    

    def test_key_error_raise(self):
        with self.assertRaises(KeyError): self.map[1]
            

if __name__ == '__main__':
    unittest.main()
