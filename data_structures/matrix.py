import unittest


class Matrix():
    """
    Class defining matrix as list of rows, containing list of values
    """

    def __init__(self, rows=None, cols=None, zeros=False):
        if zeros:
            init_type = 0
        else:
            init_type = None
        
        if rows == None:
            self.mat = [[]]
        else:
            if cols == None:
                cols = 1
            self.mat = [ [init_type] * cols] * rows
    

    def __len__(self):
        """ Return number of elements in total """
        return ( len(self.mat) * len(self.mat[0]) )
    

    def shape(self):
        """ Return (rows, cols) """
        return (len(self.mat), len(self.mat[0]))


    def __getitem__(self, index_tuple=(0, 0)):
        return self.mat[index_tuple[0]][index_tuple[1]]
    

    def row(self, index):
        return self.mat[index]
    

    @classmethod
    def rows(cls, rows, zeros=False):
        return cls(rows=rows, zeros=zeros)
    

    @classmethod
    def rows_cols(cls, rows, cols, zeros=False):
        return cls(rows=rows, cols=cols, zeros=zeros)


class TestMatrix(unittest.TestCase):
    def testInstantiation(self):
        mat = Matrix()
        self.assertEqual(0, len(mat))

        mat = Matrix.rows(3)
        self.assertEqual(3, len(mat))
        self.assertEqual(None, mat[0, 0])

        mat = Matrix.rows(3, True)
        self.assertEqual(3, len(mat))
        self.assertEqual(0, mat[0, 0])

        mat = Matrix.rows_cols(3, 2)
        self.assertEqual(None, mat[2, 1])

        mat = Matrix.rows_cols(3, 2, zeros=True)
        self.assertEqual(0, mat[2, 1])
    
    
    def testLenMethod(self):
        mat = Matrix()
        self.assertEqual(0, len(mat))

        mat = Matrix.rows(3)
        self.assertEqual(3, len(mat))

        mat = Matrix.rows_cols(3, 2)
        self.assertEqual(6, len(mat))
    
    
    def testShapeMethod(self):
        mat = Matrix.rows_cols(3, 2)
        self.assertEqual((3, 2), mat.shape())


if __name__ == '__main__':
    unittest.main()
