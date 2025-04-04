# Implementation of Map ADT using a single list.
class Map:
    # Creates an empty map instance.
    def __init__(self):
        self._entryList = list()

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
        return _MapIterator(self._entryList)

    # Helper method used to find the index position of a category. If the
    # key is not found, None is returned.
    def _findPosition(self, key):
        # Iterate through each entry in the list.
        for i in range(len(self)):
            # Is the key stored in the ith entry?
            if self._entryList[i].key == key:
                return i
        # When not
        return None

    # ASSIGNMENT 2.1
    def keyArray(self):
        return [e.key for e in self._entryList]

    # ASSIGNMENT 2.2
    def __setitem__(self, key, value):
        return self.add(key, value)

    def __getitem__(self, key):
        return self.valueOf(key)


# Storage class
class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# ASSIGNMENT 2.3
# Iterator
class _MapIterator:
    # Constructs a MapIterator
    def __init__(self, theList):
        self._setItems = theList
        self._curItem = 0

    # Returns self
    def __iter__(self):
        return self

    # Return the next element
    def __next__(self):
        if self._curItem < len(self._setItems):
            item = self._setItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
