from multiarray import MultiArray

if __name__ == '__main__':
    m = MultiArray(3, 3, 3)
    m[0, 2, 1] = 42
    print(m[0, 2, 1])
