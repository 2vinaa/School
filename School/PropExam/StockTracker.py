import ctypes
import random


class stockarr:
    def __init__(self, size):
        self.size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    def insert_value(self, index, value):
        if index < 0 and index > len(self):
            return IndexError("These are out of index size")
        else:
            self._elements[index] = value

    def retrieve_val(self, index):
        if index < 0 and index > len(self):
            return IndexError("These are out of index size")
        else:
            return self._elements[index]

    def average_price(self):
        x = 0
        for i in range(len(self)):
            x += self._elements[i]

        return f"This is the average price {x / len(self)}"


    def __repr__(self):
        x = []
        for i in range(len(self)):
            x.append(self._elements[i])
        return str(x)


    def __len__(self):
        return self.size

if __name__ == "__main__":



    arr = stockarr(30)

    for i in range(30):
        arr.insert_value(i, random.randint(0, 100))


    print(arr)
    print(arr.retrieve_val(17))
    print(arr.average_price())





