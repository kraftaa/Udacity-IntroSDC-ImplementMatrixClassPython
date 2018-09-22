import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return self.g[0][0]
        elif self.h == 2:
            return (self.g[0][0] * self.g[1][1]  - self.g[0][1] * self.g[1][0])

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        total_tense = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    total_tense += self.g[i][j]
        return total_tense


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        elif self.h  == 1:
            new_row = [1/self.g[0][0]]
            inverse.append(new_row)

        elif (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]) == 0:
            raise ValueError('The matrix is non-invertible')
        else:
            denom = 1/(self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])

            first = self.g[0][0]
            last = self.g[1][1]
            for i in range(self.h):
                new_row = []
                for j in range(self.h):
                    if i == j == 0:
                        new_row.append(last * denom)
                    elif i == j == 1:
                        new_row.append(first * denom)
                    else:
                        new_row.append(-self.g[i][j] * denom)
                inverse.append(new_row)

        return Matrix(inverse)



    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for j in range(self.w):
            new_row = []
            for i in range(self.h):
                new_row.append(self.g[i][j])
            matrix_transpose.append(new_row)
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            matrixSum.append(row)

        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        # if -self:
        #
        negative_Matrix = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self.g[i][j] * (-1))
            negative_Matrix.append(new_row)
        return Matrix(negative_Matrix)
        # neg_new = negative_Matrix.__repr__()
        # return neg_new
        # s = ""
        # for row in negative_Matrix:
        #     s += " ".join(["{} ".format(x) for x in row])
        #     s += "\n"
        # return s

        # for i in range(len(negative_Matrix)):
        #
        #     for j in range(len(negative_Matrix[0])):
        #         print(negative_Matrix[i][j], '\t', end = '')
        #
        #     print('\n')
        #
        # return negative_Matrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        matrixSub = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrixSub.append(row)

        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #
        product = []

        matrixB_tran = other.T()

        # matrixB_tran = T(other)
        for i in self.g:

            new_row = []
            for j in matrixB_tran:
                total = 0
                for x in range(len(j)):
                    temp = i[x] * j[x]
                    total += temp
                new_row.append(total)
            product.append(new_row)
        return Matrix(product)



    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """

        if isinstance(other, numbers.Number):
            pass
            #
            # TODO - your code here
            #
            new_Matrix = []

            for i in range(self.h):
                new_row = []
                for j in range(self.w):
                    new_row.append(self.g[i][j] * (other))
                new_Matrix.append(new_row)

            return Matrix(new_Matrix)
