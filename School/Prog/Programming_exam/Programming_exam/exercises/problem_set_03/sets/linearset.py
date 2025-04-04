# Implementation of the Set ADT container using a Python list.

class Set:
    # ASSIGNMENT 1.2
    # Creates an empty set instance.
    def __init__(self, *initElements):
        self._theElements = list()

        for ie in initElements:
            self.add(ie)

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # ASSIGNMENT 1.4
    def __str__(self):
        return "{" + ", ".join([str(e) for e in self._theElements]) + "}"

    # ASSIGNMENT 1.5
    def __add__(self, subB):
        return self.union(subB)

    def __mul__(self, subB):
        return self.intersect()

    def __sub__(self, subB):
        return self.difference(subB)

    def __lt__(self, subB):
        return self.isSubsetOf(subB)

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet

    # ASSIGNMENT 1.1
    # Creates a new set from the intersection of this set and setB.
    def intersect(self, setB):
        newset = Set()
        for element in self:
            if element in setB:
                newset._theElements.append(element)
        return newset

    # ASSIGNMENT 1.1
    # Creates a new set from the difference of this set and setB
    def difference(self, setB):
        newset = Set()
        for element in self:
            if element not in setB:
                newset._theElements.append(element)
        return newset

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self._theElements)

    # ASSIGNMENT 1.3
    def is_proper_subset(self, setB):
        if self == setB:
            return False
        return self.isSubsetOf(setB)


# ASSIGNMENT 1.6
class _SetIterator:
    # Constructs a SetIterator
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
