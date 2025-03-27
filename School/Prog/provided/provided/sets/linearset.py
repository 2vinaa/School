# Implementation of the Set ADT container using a Python list.


class Set:
    def __init__(self, *init_elements):
        self._theElements = list()
        for i in init_elements:
            self._theElements.append(i)

    def __str__(self):
        x = str(self._theElements)
        y = x.replace("[","{").replace("]", "}")
        return y



    # Returns the number of items in the set.
    def __len__(self):
        return len(self._theElements)

    # Determines if an element is in the set.
    def __contains__(self, element):
        return element in self._theElements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self._theElements:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self, "The element must be in the set."
        self._theElements.remove(element)
    
        # Determines if two sets are equal.
    def __eq__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

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

    def is_proper_subset(self, set_b):
        list1 = []
        list2 = []
        counter1 = 0
        if self.isSubsetOf(set_b) == True:
            for i in set_b:
                list2.append(i)
            for j in self._theElements:
                list1.append(j)

            list1.sort()
            list2.sort()
            if len(list1) > len(list2):
                return False
            if len(list2) > len(list1):
                alpha = len(list1)

            for x in range(alpha):
                if list1[x] == list2[x]:
                    counter1 += 1

            if counter1 == alpha:
                return "These two aren't proper subset"
            else:
                return "These are proper subset"


    def __add__(self, set_b):
        return self.union(set_b)

    def __mul__(self, set_b):
        return self.intersect(set_b)

    def __sub__(self, set_b):
        return self.difference(set_b)

    def __lt__(self, set_b):
        return self.isSubsetOf(set_b)
    # Returns an iterator for traversing the list of items.
    def __iter__(self):
        return iter(self._theElements)