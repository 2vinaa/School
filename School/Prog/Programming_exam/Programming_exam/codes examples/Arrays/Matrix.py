
from Array2D import Array2D

class Matrix:

    def __init__(self, n_rows, n_cols):
        self._grid = Array2D(n_rows, n_cols)
        self._grid.clear(0)

    def __getitem__(self, index_tuple):
        return self._grid.__getitem__(index_tuple)

    def __setitem__(self, index_tuple, value):
        self._grid.__setitem__(index_tuple, value)

    def num_rows(self):
        return self._grid.num_rows()

    def num_cols(self):
        return self._grid.num_cols()

    def scale_by(self, scalar):
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self[i, j] *= scalar

    def transpose(self):
        transposed = Matrix(self.num_cols(), self.num_rows())
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                transposed[j, i] = self[i, j]
        return transposed

    def __add__(self, otherMatrix):
        assert self.num_rows() == otherMatrix.num_rows() and self.num_cols() == otherMatrix.num_cols(), "Dimension mismatch"
        result = Matrix(self.num_rows(), self.num_cols())
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                result[i, j] = self[i, j] + otherMatrix[i, j]
        return result

    def __sub__(self, otherMatrix):
        assert self.num_rows() == otherMatrix.num_rows() and self.num_cols() == otherMatrix.num_cols(), "Dimension mismatch"
        result = Matrix(self.num_rows(), self.num_cols())
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                result[i, j] = self[i, j] - otherMatrix[i, j]
        return result

    def __mul__(self, otherMatrix):
        assert self.num_cols() == otherMatrix.num_rows(), "Incompatible matrix dimensions for multiplication"
        result = Matrix(self.num_rows(), otherMatrix.num_cols())
        for i in range(self.num_rows()):
            for j in range(otherMatrix.num_cols()):
                result[i, j] = sum(self[i, k] * otherMatrix[k, j] for k in range(self.num_cols()))
        return result