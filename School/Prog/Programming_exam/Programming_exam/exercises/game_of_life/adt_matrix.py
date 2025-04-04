from adt_array import Array2D


class Matrix:
    # Creates a matrix of size numRows x numCols initialized to 0.
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)

    # Returns the number of rows in the matrix.
    def numRows(self):
        return self._theGrid.numRows()

    # Returns the number of columns in the matrix.
    def numCols(self):
        return self._theGrid.numCols()

    # Returns the value of element (i, j): x[i,j]
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0], ndxTuple[1]]

    # Sets the value of element (i,j) to the value s: x[i,j] = s
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

    # Scales the matrix by the given scalar.
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scalar

    # Creates and returns a new matrix that results from matrix addition.
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] + rhsMatrix[r, c]
        return newMatrix

    # Creates and returns a new matrix that results from matrix subtraction.
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "Matrix sizes not compatible for the add operation."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r, c] = self[r, c] - rhsMatrix[r, c]
        return newMatrix

    # Creates and returns a new matrix resulting from matrix multiplication.
    def __mul__(self, rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows(), "Lefthand matrix column size must be equal to righthand matrix row size."
        # Create the new matrix.
        newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())

        # multiply
        for i in range(self.numRows()):
            for j in range(rhsMatrix.numCols()):
                for k in range(rhsMatrix.numRows()):
                    # resulted matrix
                    newMatrix[i, j] += self[i, k] * rhsMatrix[k, j]

        return newMatrix

    # Creates and returns a new matrix  that is the transpose of this matrix.
    def transpose(self):
        newMatrix = Matrix(self.numCols(), self.numRows())

        for i in range(self.numRows()):
            for j in range(self.numCols()):
                newMatrix[j, i] = self[i, j]
        return newMatrix
