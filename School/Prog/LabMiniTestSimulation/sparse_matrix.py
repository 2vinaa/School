from operator import index


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
    #projokjo

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, coordinates):
        x = self._find_position(coordinates[0], coordinates[1])
        if x is None:
            return 0
        return self._elements[x].value #The time is fixed so 1

    def add(self, other):

        assert other._cols == self._cols and other._rows == self._rows, "The rows and Cols are different"
        matrix_sum = SparseMatrix(self._rows, self._cols)

        for i in range(self._rows):
            for j in range(self._cols):
                matrix_sum[i, j] = self[i, j] + other[i, j]

        return matrix_sum #The time is O(n^2)

    def subtract(self, other):
        assert other._cols == self._cols and other._rows == self._rows, "The rows and Cols are different"
        matrix_sub = SparseMatrix(self._rows, self._cols)

        for i in range(self._rows):
            for j in range(self._cols):
                matrix_sub[i, j] = self[i, j] - other[i, j]

        return matrix_sub #The time is O(n^2)

    def multiply(self, other):
        assert (other._cols == self._cols and other._rows == self._rows) or (self._rows > other._rows), "The rows and Cols are different"
        matrix_mult = SparseMatrix(self._rows, self._cols)

        for i in range(self._rows):
            for j in range(self._cols):
                matrix_mult[i, j] = self[i, j] * other[i, j]

        return matrix_mult #The time is O(n^2)

    def transpose(self):
        matrix = SparseMatrix(self._rows, self._cols)
        for i in range(self._rows):
            for j in range(self._cols):
                matrix[i,j] = self[j,i]

        return matrix #The time is O(n^2)



    def __add__(self, other):
        return self.add(other) #The time is O(n^2)

    def __mul__(self, other):
        return self.multiply(other) #The time is O(n^2)
    def __sub__(self, other):
        return self.subtract(other) #The time is O(n^2)

    def sort_values(self):
        while True:
            choice = int(input("Enter type of sort [Bubble: 1, Selection: 2, Insertion: 3]: "))
            nonzero_values = [e.value for e in self._elements]
            if choice == 1:

                n = len(nonzero_values)
                for i in range(n - 1):
                    for j in range(n - 1 - i):
                        if nonzero_values[j] > nonzero_values[j + 1]:
                            nonzero_values[j], nonzero_values[j + 1] = nonzero_values[j + 1], nonzero_values[j]
            elif choice == 2:
                n = len(nonzero_values)
                for i in range(n - 1):
                    min_idx = i
                    for j in range(i + 1, n):
                        if nonzero_values[j] < nonzero_values[min_idx]:
                            min_idx = j
                    nonzero_values[i], nonzero_values[min_idx] = nonzero_values[min_idx], nonzero_values[i]

            elif choice == 3:
                n = len(nonzero_values)
                for i in range(1, n):
                    n = nonzero_values[i]
                    j = i - 1
                    while j >= 0 and nonzero_values[j] > n:
                        nonzero_values[j + 1] = nonzero_values[j]
                        j -= 1
                    nonzero_values[j + 1] = n
            else:
                print("Incorrect input. Try again")

            new_matrix = SparseMatrix(self.rows(), self.cols())
            index = 0
            for i in range(self.rows()):
                for j in range(self.cols()):
                    if self[i, j] != 0:
                        new_matrix[i, j] = nonzero_values[index]
                        index += 1
            return new_matrix





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