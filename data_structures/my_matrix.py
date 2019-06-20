
class MyMatrix():
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
        """
        Returns the matrix as string in the form of e.g.:
        0, 0,
        0, 0,
        """
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
        """ Creates rows x rows matrix """
        return cls(rows=rows, cols=rows, init_type=init_type)
    

    @classmethod
    def rows_cols(cls, rows, cols, init_type=None):
        """ Creates rows x cols matrix """
        return cls(rows=rows, cols=cols, init_type=init_type)
    

    @classmethod
    def identity(cls, n):
        """ Creates identity matrix (nxn) """
        mat = cls(n, n, init_type=0)
        for i in range(n):
            mat.mat[i][i] = 1
        return mat
    
    @classmethod
    def ones(cls, n):
        """ Creates nxn matrix, initialized with 1's """
        return cls(n, init_type=1)
    

    @classmethod
    def zeros(cls, n):
        """ Creates nxn matrix, initialized with 0's """
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
