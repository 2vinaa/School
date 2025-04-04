from Matrix import Matrix

if __name__ == "__main__":
    A = Matrix(3, 3)
    B = Matrix(3, 3)

    A[0, 0], A[0, 1], A[0, 2] = 1, 2, 3
    A[1, 0], A[1, 1], A[1, 2] = 4, 5, 6
    A[2, 0], A[2, 1], A[2, 2] = 7, 8, 9

    B[0, 0], B[0, 1], B[0, 2] = 9, 8, 7
    B[1, 0], B[1, 1], B[1, 2] = 6, 5, 4
    B[2, 0], B[2, 1], B[2, 2] = 3, 2, 1

    print("Matrix A:")
    for i in range(A.num_rows()):
        print([A[i, j] for j in range(A.num_cols())])

    print("\nMatrix B:")
    for i in range(B.num_rows()):
        print([B[i, j] for j in range(B.num_cols())])

    C = A + B
    print("\nA + B:")
    for i in range(C.num_rows()):
        print([C[i, j] for j in range(C.num_cols())])

    D = A * B
    print("\nA * B:")
    for i in range(D.num_rows()):
        print([D[i, j] for j in range(D.num_cols())])

    E = A - B
    print("\nA - B:")
    for i in range(E.num_rows()):
        print([E[i, j] for j in range(E.num_cols())])

    A.scale_by(2)
    print("\nA scaled by 2:")
    for i in range(A.num_rows()):
        print([A[i, j] for j in range(A.num_cols())])

    F = A.transpose()
    print("\nTranspose of A:")
    for i in range(F.num_rows()):
        print([F[i, j] for j in range(F.num_cols())])
