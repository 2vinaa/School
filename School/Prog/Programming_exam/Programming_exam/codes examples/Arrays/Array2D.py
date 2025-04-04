
from Array import Array

class Array2D:

    def __init__(self, n_rows, n_cols):
        assert n_rows > 0 and n_cols > 0, "Invalid n of rows/cols"
        self._n_rows = n_rows
        self._n_cols = n_cols
        self._elements = Array(n_rows)

        for i in range(n_cols):
            self._elements[i] = Array(n_cols)

    def __getitem__(self, index_tuple):
        assert len(index_tuple) == 2, "Invalid indexes"
        row_index = index_tuple[0]
        col_index = index_tuple[1]
        assert 0 <= row_index < self._n_rows, "Invalid row index"
        assert 0 <= col_index < self._n_cols, "Invalid col index"

        return self._elements[row_index][col_index]

    def __setitem__(self, index_tuple, value):
        assert len(index_tuple) == 2, "Invalid indexes"
        row_index = index_tuple[0]
        col_index = index_tuple[1]
        assert 0 <= row_index < self._n_rows, "Invalid row index"
        assert 0 <= col_index < self._n_cols, "Invalid col index"

        self._elements[row_index][col_index] = value

    def num_rows(self):
        return self._n_rows

    def num_cols(self):
        return self._n_cols

    def clear(self, value=None):
        for i in range(self._n_rows):
            self._elements[i].clear(value)


