import ctypes

class Array:

    def __init__(self, size):
        # print("called __init__ method")
        assert size > 0, "size must be > 0" # 1
        self._size = size # 1
        py_array_type = ctypes.py_object * size # N
        self._elements = py_array_type() # 1
        self.clear(None) # N

    def clear(self, value): # N
        # print("called clear method")
        for i in range(len(self)):
            self[i] = value

    def __len__(self):
        # print("called __len__ method")
        return self._size # 1

    def __setitem__(self, index, value):
        # print("called __setitem__ method")
        assert 0 <= index < len(self), "Index out of range" # 1
        self._elements[index] = value # 1

    def __getitem__(self, index):
        # print("called __getitem__ method")
        assert 0 <= index < len(self), "Index out of range" # 1
        return self._elements[index] # 1

    def __iter__(self):
        # print("called __iter__ method")
        return ArrayIterator(self) # 1


class ArrayIterator:

    def __init__(self, my_array):
        # print("called __init__ method ArrayIterator")
        self._my_array = my_array # 1
        self._current_index = 0 # 1

    def __iter__(self):
        # print("called __iter__ method ArrayIterator")
        return self

    def __next__(self):
        # print("called __next__ method ArrayIterator")
        if self._current_index < len(self._my_array):
            element = self._my_array[self._current_index]
            self._current_index += 1
            return element
        raise StopIteration