import unittest

from my_matrix import MyMatrix


class TestMatrix(unittest.TestCase):
    def test_instantiation(self):
        mat = MyMatrix()
        self.assertEqual(0, len(mat))

        n = 3
        mat = MyMatrix.rows(n)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(None, mat[0, 0])

        mat = MyMatrix.rows(n, init_type=0)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(0, mat[0, 0])

        mat = MyMatrix.rows_cols(3, 2)
        self.assertEqual(None, mat[2, 1])

        mat = MyMatrix.rows_cols(3, 2, init_type=0)
        self.assertEqual(0, mat[2, 1])
    
    
    def test_str(self):
        mat = MyMatrix.rows_cols(3, 2, init_type=0)
        expected = '0, 0,\n0, 0,\n0, 0'
        self.assertEqual(expected, str(mat))
    

    def test_set_item(self):
        mat = MyMatrix.rows_cols(3, 2, init_type=0)
        mat[0, 0] = 1
        self.assertEqual(1, mat[0, 0])
        self.assertEqual(0, mat[0, 1])
        self.assertEqual(0, mat[1, 0])

    
    def test_identity(self):
        n = 3
        mat = MyMatrix.identity(n)
        for row in range(n):
            for col in range(n):
                el = mat[row, col]
                if (row == col):
                    self.assertEqual(1, el)
                else:
                    self.assertEqual(0, el)


    def test_ones(self):
        n = 3
        mat = MyMatrix.ones(n)
        self.assertEqual(n*n, len(mat))
        for i in range(n):
            for j in range(n):
                self.assertEqual(1, mat[i, j])
    

    def test_zeros(self):
        n = 3
        mat = MyMatrix.zeros(n)
        self.assertEqual(n*n, len(mat))
        for i in range(n):
            for j in range(n):
                self.assertEqual(0, mat[i, j])
    

    def test_ascending_ints(self):
        n = 4
        mat = MyMatrix.ascending_ints(n)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(0,  mat[0, 0])
        self.assertEqual(1,  mat[0, 1])
        self.assertEqual(2,  mat[0, 2])
        self.assertEqual(9,  mat[2, 1])
        self.assertEqual(14,  mat[3, 2])
        self.assertEqual(15,  mat[3, 3])
        del mat

        n = 3
        mat = MyMatrix.ascending_ints(n, 1)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(1,  mat[0, 0])
        self.assertEqual(2,  mat[0, 1])
        self.assertEqual(3,  mat[0, 2])
        self.assertEqual(7,  mat[2, 0])
        self.assertEqual(8,  mat[2, 1])
        self.assertEqual(9,  mat[2, 2])


    def test_len(self):
        mat = MyMatrix()
        self.assertEqual(0, len(mat))

        n = 3
        mat = MyMatrix.rows(n)
        self.assertEqual(n*n, len(mat))

        mat = MyMatrix.rows_cols(3, 2)
        self.assertEqual(6, len(mat))
    
    
    def test_shape(self):
        mat = MyMatrix.rows_cols(3, 2)
        self.assertEqual((3, 2), mat.shape())
    

    def test_zero_matrix(self):
        n = 3
        mat = MyMatrix.ones(n)
        zero_index = 1
        mat[zero_index, zero_index] = 0
        MyMatrix.zero_matrix(mat)
        # print('\n')
        # print(mat)
        for row in range(n):
            for col in range(n):
                if row == zero_index or col == zero_index:
                    self.assertEqual(0, mat[row, col])
                else:
                    self.assertEqual(1, mat[row, col])


    def test_rotate(self):
        pass


if __name__ == '__main__':
    unittest.main()
