from School.Prog.Hash.arr import Array, _ArrayIterator, Array2D


if __name__ == "__main__":


    x = Array2D(int(input("Send the numb row array\n")), int(input("Send the numb column of the array\n")))
    Array2D.__setitem__(x, [int(input("Val 1 of tuple\n")), int(input("Val 2 of Tuple\n"))], int(input("Added Value\n")))
    Array2D.__getitem__(x,[int(input("Val 1 of tuple\n")), int(input("Val 2 of Tuple\n"))])
    Array2D.numRows(x)
    Array2D.numCols(x)
    Array2D.clear(x, 0)


    x = Array(int(input("Send the length of the array\n")))
    for i in range(len(x)):
        print(Array.__setitem__(x, int(input("At what index?\n")), input("What to add?\n")))




    print(Array.__getitem__(x, int(input("At what index?\n"))))
    print(Array.clear(x, int(input("What Value to clear everything?\n"))))

    y = _ArrayIterator(x)
    print(_ArrayIterator.__next__(y))