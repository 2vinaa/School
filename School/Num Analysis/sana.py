import numpy as np

if __name__ == "__main__":


    A = np.array([[2, -5, -11, 0], [-9, 4, 6, 13], [4, 7, 12, -2]])
    print("A =", A)
    print("3rd element of 2nd row: ", A[1][2])  # 3rd element of 2nd row
    print("Second row: ", A[1, :])  # 2nd row
    print("Third column: ", A[:, 2])#odio questa app