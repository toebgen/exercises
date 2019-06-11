import unittest


class Matrix():
    """
    Class defining matrix as list of rows, containing list of values
    """

    def __init__(self, rows=None, cols=None, init_type=None):
        if rows == None:
            self.mat = [[]]
        else:
            if cols == None:
                cols = rows
            self.mat = [[init_type for x in range(cols)] for y in range(rows)]
    

    def __len__(self):
        """ Return number of elements in total """
        return ( len(self.mat) * len(self.mat[0]) )
    

    def shape(self):
        """ Return (rows, cols) """
        return (len(self.mat), len(self.mat[0]))


    def __getitem__(self, index_tuple=(0, 0)):
        return self.mat[index_tuple[0]][index_tuple[1]]
    

    def __setitem__(self, index_tuple, value):
        self.mat[index_tuple[0]][index_tuple[1]] = value
    

    def __str__(self):
        s = ''
        for row in self.mat:
            for el in row:
                s += str(el) + ', '
            s = s[:-1]
            s += '\n'
        return s[:-2]
    

    def row(self, index):
        return self.mat[index]
    

    @classmethod
    def rows(cls, rows, init_type=None):
        """ rows x rows matrix """
        return cls(rows=rows, cols=rows, init_type=init_type)
    

    @classmethod
    def rows_cols(cls, rows, cols, init_type=None):
        """ rows x cols matrix """
        return cls(rows=rows, cols=cols, init_type=init_type)
    

    @classmethod
    def identity(cls, n):
        """ Make identity matrix (nxn) """
        mat = cls(n, n, init_type=0)
        for i in range(n):
            mat.mat[i][i] = 1
        return mat
    
    @classmethod
    def ones(cls, n):
        return cls(n, init_type=1)
    

    @classmethod
    def zeros(cls, n):
        return cls(n, init_type=0)
    

    @staticmethod
    def zero_matrix(mat):
        """
        If an element in an MxN matrix is 0, set entire row and column to zero.
        Cf. Cracking the Coding Interview: 1.8.
        """
        # Find rows and columns with zeros first
        zero_rows, zero_cols = set(), set()
        rows, cols = mat.shape()
        for row in range(rows):
            for col in range(cols):
                if mat[row, col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        
        # Set rows and cols with zeros completely to zero
        for row in range(rows):
            for col in range(cols):
                if row in zero_rows or col in zero_cols:
                    mat[row, col] = 0


class TestMatrix(unittest.TestCase):
    def testInstantiation(self):
        mat = Matrix()
        self.assertEqual(0, len(mat))

        n = 3
        mat = Matrix.rows(n)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(None, mat[0, 0])

        mat = Matrix.rows(n, init_type=0)
        self.assertEqual(n*n, len(mat))
        self.assertEqual(0, mat[0, 0])

        mat = Matrix.rows_cols(3, 2)
        self.assertEqual(None, mat[2, 1])

        mat = Matrix.rows_cols(3, 2, init_type=0)
        self.assertEqual(0, mat[2, 1])
    
    
    def testStr(self):
        mat = Matrix.rows_cols(3, 2, init_type=0)
        expected = '0, 0,\n0, 0,\n0, 0'
        self.assertEqual(expected, str(mat))
    

    def testSetItem(self):
        mat = Matrix.rows_cols(3, 2, init_type=0)
        mat[0, 0] = 1
        self.assertEqual(1, mat[0, 0])
        self.assertEqual(0, mat[0, 1])
        self.assertEqual(0, mat[1, 0])

    
    def testIdentity(self):
        n = 3
        mat = Matrix.identity(n)
        for row in range(n):
            for col in range(n):
                el = mat[row, col]
                if (row == col):
                    self.assertEqual(1, el)
                else:
                    self.assertEqual(0, el)


    def testOnes(self):
        n = 3
        mat = Matrix.ones(n)
        self.assertEqual(n*n, len(mat))
        for i in range(n):
            for j in range(n):
                self.assertEqual(1, mat[i, j])
    

    def testZeros(self):
        n = 3
        mat = Matrix.zeros(n)
        self.assertEqual(n*n, len(mat))
        for i in range(n):
            for j in range(n):
                self.assertEqual(0, mat[i, j])


    def testLenMethod(self):
        mat = Matrix()
        self.assertEqual(0, len(mat))

        n = 3
        mat = Matrix.rows(n)
        self.assertEqual(n*n, len(mat))

        mat = Matrix.rows_cols(3, 2)
        self.assertEqual(6, len(mat))
    
    
    def testShapeMethod(self):
        mat = Matrix.rows_cols(3, 2)
        self.assertEqual((3, 2), mat.shape())
    

    def testZeroMatrix(self):
        n = 3
        mat = Matrix.ones(n)
        zero_index = 1
        mat[zero_index, zero_index] = 0
        Matrix.zero_matrix(mat)
        print('\n')
        print(mat)
        for row in range(n):
            for col in range(n):
                if row == zero_index or col == zero_index:
                    self.assertEqual(0, mat[row, col])
                else:
                    self.assertEqual(1, mat[row, col])


if __name__ == '__main__':
    unittest.main()
