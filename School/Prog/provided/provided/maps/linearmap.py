# Implementation of Map ADT using a single list.
class Map:
    # Creates an empty map instance.
    def __init__(self):
        self._entryList = list()
        self.keys = list()
        self.item = list()


    # Returns the number of entries in the map.
    def __len__(self):
        return len(self._entryList)

    # Determines if the map contains the given key.
    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    # Adds a new entry to the map if the key does exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, value):
        ndx = self._findPosition(key)
        self.keys.append(key)
        if ndx is not None:  # if the key was found
            self._entryList[ndx].value = value
            return False
        else:  # otherwise add a new entry
            entry = _MapEntry(key, value)
            self._entryList.append(entry)
            return True

    # Returns the value associated with the key.
    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        return self._entryList[ndx].value

    # Removes the entry associated with the key.
    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invalid map key."
        self._entryList.pop(ndx)

    # Returns an iterator for traversing the keys in the map.
    def __iter__(self):
        return _MapIterator(self.keys, self.item)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None

    def keyArray(self):
        return self.keys



# Storage class
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class _MapIterator:
        def __init__(self, key, values):
            diz = dict(zip(key, values))

        def __iter__(self):
            self.cont = 0
            return self

        def __next__(self):
            dic = list(self.__dict__.items())[self.cont]
            self.cont += 1
            return dic
