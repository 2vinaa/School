
class SparseMatrix:
    def __init__(self, rows, cols):
        if rows <= 0:
            raise ValueError("Rows must be > 0!")
        elif cols <= 0:
            raise ValueError("Columns must be > 0!")

        self._rows = rows
        self._cols = cols
        self._elements = list()

    def rows(self):
        return self._rows

    def cols(self):
        return self._cols

    def _find_position(self, row, col):
        for i, e in enumerate(self._elements):
            if row == e.row and col == e.col:
                return i
        return None

    def __setitem__(self, position, value):
        index = self._find_position(position[0], position[1])

        if index is None:
            if value == 0:
                return

            element = _MatrixElement(position[0], position[1], value)
            self._elements.append(element)
            return
        else:
            if value == 0:
                self._elements.pop(index)
                return

            self._elements[index].value = value

    def __str__(self):
        string_repr = ""
        for i in range(self._rows):
            for j in range(self._cols):
                string_repr += f"{self[i, j]}\t"
            string_repr += "\n"
        return string_repr

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, coordinates):
        position = self._find_position(coordinates[0], coordinates[1])
        return self._elements[position].value if position is not None else 0

    def add(self, o):
        assert (self._cols == o._cols and self._rows == o._rows), "These arent valid matrix"
        newmatrix = SparseMatrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                newmatrix[i,j] = self[i,j] + o[i,j]

        return newmatrix



    def subtract(self, o):
        assert (self._cols == o._cols and self._rows == o._rows), "These arent valid matrix"
        newmatrix = SparseMatrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                newmatrix[i, j] = self[i, j] - o[i, j]

        return newmatrix

    def multiply(self, o):
        assert (self._cols == o._cols and self._rows == o._rows), "These arent valid matrix"
        newmatrix = SparseMatrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                newmatrix[i, j] = self[i, j] * o[i, j]

        return newmatrix

    def transpose(self):

        newmatrix = SparseMatrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                newmatrix[i, j] = self[j, i]

        return newmatrix

    def __add__(self, o):
        return self.add(o)

    def __mul__(self, o):
        return self.multiply(o)

    def __sub__(self, o):
        return self.subtract(o)

    def sort_values(self):
        non_zero_vals = [i.value for i in self._elements]
        n = len(non_zero_vals)
        for i in range(1,n):
            value = non_zero_vals[i]
            pos = i
            while pos>0 and value <non_zero_vals[pos-1]:
                non_zero_vals[pos] = non_zero_vals[pos-1]
                pos -= 1
                non_zero_vals[pos] = value


        newmatrix = SparseMatrix(self._rows, self._cols)
        index = 0
        for i in range(self._rows):
            for j in range(self._cols):
                if self[i,j] != 0:
                    newmatrix[i,j] = non_zero_vals[index]
                    index += 1

        return newmatrix

class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value



if __name__ == "__main__":
    print("Creating matrix A (4x4)...")
    A = SparseMatrix(4, 4)
    A[0, 0] = 7
    A[0, 2] = 1
    A[1, 1] = 9
    A[2, 3] = 3
    A[3, 0] = 6
    A[3, 3] = 2
    print("Matrix A:")
    print(A)
    # Expected:
    # 7	0	1	0
    # 0	9	0	0
    # 0	0	0	3
    # 6	0	0	2

    print("Creating matrix B (4x4)...")
    B = SparseMatrix(4, 4)
    B[0, 0] = 5
    B[1, 1] = 1
    B[2, 3] = 4
    B[3, 0] = 3
    B[3, 3] = 8
    print("Matrix B:")
    print(B)
    # Expected:
    # 5	0	0	0
    # 0	1	0	0
    # 0	0	0	4
    # 3	0	0	8

    print("Testing __getitem__...")
    print("A[1,1] =", A[1, 1])  # Expected: 9
    print("A[0,3] =", A[0, 3])  # Expected: 0

    print("Testing add(A + B):")
    C = A.add(B)
    print(C)
    # Expected:
    # 12	0	1	0
    # 0	10	0	0
    # 0	0	0	7
    # 9	0	0	10

    print("Testing subtract(A - B):")
    D = A.subtract(B)
    print(D)
    # Expected:
    # 2	0	1	0
    # 0	8	0	0
    # 0	0	0	-1
    # 3	0	0	-6

    print("Testing multiply(A * B):")
    E = A.multiply(B)
    print(E)
    # Expected (matrix product):
    # 35	0	0	0
    # 0	    9	0	0
    # 0	    0	0	12
    # 18	0	0	16

    print("Testing transpose(Aᵗ):")
    F = A.transpose()
    print(F)
    # Expected:
    # 7	0	0	6
    # 0	9	0	0
    # 1	0	0	0
    # 0	0	3	2

    print("Testing magic operators:")
    print("A + B:")
    print(A + B)  # Same as A.add(B)

    print("A - B:")
    print(A - B)  # Same as A.subtract(B)

    print("A * B:")
    print(A * B)  # Same as A.multiply(B)

    print("Testing sort_values()")
    sorted_A = A.sort_values()
    print(sorted_A)
    # Expected output:
    # 1	0	2	0
    # 0	3	0	0
    # 0	0	0	6
    # 7	0	0	9