# Implementation of the Set ADT container using a Python list.

class Set:
    # Creates an empty set instance.
    def __init__(self):
        self._theElements = list()

    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        if element in self._theElements:
            return element

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)

    # Determines if two sets are equal.
    def __eq__(self, set_b):
        if len(self) != len(set_b):
            return False
        else:
            return self.is_Subset_Of(set_b)

    # Determines if this set is a subset of setB.
    def is_Subset_Of(self, set_b):
        for element in self:
            if element not in set_b:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, set_b):
        new_set = Set()
        new_set._theElements.extend(self._theElements)
        for element in set_b:
            if element not in self:
                new_set._theElements.append(element)
        return new_set

    # Creates a new set from the intersection: self set and setB.
    def intersect(self, set_b):
        new_int = Set()
        for element in self:
            if element in set_b:
                new_int._theElements.append(element)
        return new_int



    # Creates a new set from the difference: self set and setB.
    def difference(self, set_b):
        new_set = Set()
        for element in self:
            if element not in set_b:
                new_set._theElements.append(element)

        return new_set

    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return iter(self._theElements)
