import ctypes

class Array:
    def __init__(self, size):
        assert size > 0, "size must be > 0"
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def clear(self, value):
        # Fill the array with a default value
        for i in range(len(self)):
            self[i] = value

    def __len__(self):
        return self._size

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Index out of range"
        self._elements[index] = value

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Index out of range"
        return self._elements[index]

    def __iter__(self):
        return ArrayIterator(self)


class ArrayIterator:
    def __init__(self, my_array):
        self._my_array = my_array
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self._my_array):
            element = self._my_array[self._current_index]
            self._current_index += 1
            return element
        raise StopIteration