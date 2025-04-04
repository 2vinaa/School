class SparseMatrix:
    def __init__(self, rows, cols):
        # Check for valid matrix dimensions
        if rows <= 0:
            raise ValueError("Rows must be > 0!")
        elif cols <= 0:
            raise ValueError("Columns must be > 0!")

        self._rows = rows
        self._cols = cols
        # List to store non-zero elements
        self._elements = list()

    def rows(self):
        return self._rows

    def cols(self):
        return self._cols

    def _find_position(self, row, col):  # O(n) where n = number of non-zero elements
        # Search for the position of a non-zero element
        for i, e in enumerate(self._elements):
            if row == e.row and col == e.col:
                return i
        return None

    def __setitem__(self, position, value):  # O(n)
        # Set an element at the given position
        index = self._find_position(position[0], position[1])

        if index is None:
            if value == 0:
                return  # Skip storing zero
            element = _MatrixElement(position[0], position[1], value)
            self._elements.append(element)
        else:
            if value == 0:
                self._elements.pop(index)  # Remove if set to zero
            else:
                self._elements[index].value = value

    def __str__(self):  # O(r * c)
        # Return string representation of the matrix
        string_repr = ""
        for i in range(self._rows):
            for j in range(self._cols):
                string_repr += f"{self[i, j]}\t"
            string_repr += "\n"
        return string_repr

    def __repr__(self):
        # Used for printing the object
        return self.__str__()

    def __getitem__(self, coordinates):  # O(n)
        # Retrieve element at given coordinates
        position = self._find_position(coordinates[0], coordinates[1])
        return self._elements[position].value if position is not None else 0

    def add(self, o):  # O(n)
        # Matrix addition
        if self._rows != o.rows() or self._cols != o.cols():
            raise ValueError("Matrix dimensions must match")
        result = SparseMatrix(self._rows, self._cols)
        for e in self._elements:
            result[e.row, e.col] = e.value
        for e in o._elements:
            result[e.row, e.col] = result[e.row, e.col] + e.value
        return result

    def subtract(self, o):  # O(n)
        # Matrix subtraction
        if self._rows != o.rows() or self._cols != o.cols():
            raise ValueError("Matrix dimensions must match")
        result = SparseMatrix(self._rows, self._cols)
        for e in self._elements:
            result[e.row, e.col] = e.value
        for e in o._elements:
            result[e.row, e.col] = result[e.row, e.col] - e.value
        return result

    def multiply(self, o):  # O(r * c * sd)
        # Matrix multiplication
        if self._cols != o.rows():
            raise ValueError("Matrix dimensions are not aligned for multiplication")

        result = SparseMatrix(self._rows, o.cols())

        for i in range(self.rows()):  # Iterate over result rows
            for j in range(o.cols()):  # Iterate over result columns
                for k in range(self.cols()):  # Iterate over shared dimension
                    result[i, j] += self[i, k] * o[k, j]

        return result

    def transpose(self):  # O(n)
        # Transpose the matrix
        result = SparseMatrix(self._cols, self._rows)
        for e in self._elements:
            result[e.col, e.row] = e.value
        return result

    def __add__(self, o):
        return self.add(o)  # Magic operator for +

    def __sub__(self, o):
        return self.subtract(o)  # Magic operator for -

    def __mul__(self, o):
        return self.multiply(o)  # Magic operator for *

    def sort_values(self):  # O(n^2) where n is the number of nonzero elements
        # Sort values and maintain original positions order
        values = []
        for v in self._elements:
            values.append(v.value)

        # Bubble sort values
        n = len(values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]

        # Sort positions by row, then by column
        positions = self._elements[:]
        for i in range(len(positions)):
            for j in range(0, len(positions) - i - 1):
                a, b = positions[j], positions[j + 1]
                if (a.row > b.row) or (a.row == b.row and a.col > b.col):
                    positions[j], positions[j + 1] = positions[j + 1], positions[j]

        # Create a new matrix with sorted values
        result = SparseMatrix(self._rows, self._cols)
        for i in range(len(positions)):
            e = positions[i]
            result[e.row, e.col] = values[i]

        return result

    def sort_values1(self): # O(r * c)
        # Sort values and maintain original positions order
        values = []
        for v in self._elements:
            values.append(v.value)

        # Bubble sort values
        n = len(values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if values[j] > values[j + 1]:
                    values[j], values[j + 1] = values[j + 1], values[j]

        index = 0

        result = SparseMatrix(self._rows, self._cols)

        for i in range(self._rows):
            for j in range(self._cols):
                if self[i, j] != 0:
                    result[i,j] = values[index]
                    index += 1

        return result



class _MatrixElement:
    def __init__(self, row, col, value):
        # Simple container for matrix element
        self.row = row
        self.col = col
        self.value = value


if __name__ == "__main__":
    # Demo and test section
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

    print("Creating matrix B (4x4)...")
    B = SparseMatrix(4, 4)
    B[0, 0] = 5
    B[1, 1] = 1
    B[2, 3] = 4
    B[3, 0] = 3
    B[3, 3] = 8
    print("Matrix B:")
    print(B)

    print("Testing __getitem__...")
    print("A[1,1] =", A[1, 1])  # Should return 9
    print("A[0,3] =", A[0, 3])  # Should return 0

    print("Testing add(A + B):")
    C = A.add(B)
    print(C)

    print("Testing subtract(A - B):")
    D = A.subtract(B)
    print(D)

    print("Testing multiply(A * B):")
    E = A.multiply(B)
    print(E)

    print("Testing transpose(Aᵗ):")
    F = A.transpose()
    print(F)

    print("Testing magic operators:")
    print("A + B:")
    print(A + B)

    print("A - B:")
    print(A - B)

    print("A * B:")
    print(A * B)

    print("Testing sort_values()")
    sorted_A = A.sort_values()
    print(sorted_A)