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
        expected_mat = [
            [0,  1,  2,  3],
            [4,  5,  6,  7],
            [8,  9,  10, 11],
            [12, 13, 14, 15],
        ]
        for i in range(n):
            for j in range(n):
                self.assertEqual(expected_mat[i][j],  mat[i, j])
        del mat

        n = 3
        mat = MyMatrix.ascending_ints(n, 1)
        expected_mat = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        for i in range(n):
            for j in range(n):
                self.assertEqual(expected_mat[i][j],  mat[i, j])


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
        mat = MyMatrix()
        mat.rotate()
        self.assertIsNotNone(mat)

        n = 1
        mat = MyMatrix.ascending_ints(n, 1)
        mat.rotate()
        expected_mat = [
            [1],
        ]
        for i in range(n):
            for j in range(n):
                self.assertEqual(expected_mat[i][j], mat[i, j])

        n = 3
        mat = MyMatrix.ascending_ints(n, 1)
        mat.rotate()
        expected_mat = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ]
        for i in range(n):
            for j in range(n):
                self.assertEqual(expected_mat[i][j], mat[i, j])


if __name__ == '__main__':
    unittest.main()
