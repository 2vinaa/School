# Define a custom Set class using lists as the underlying data structure
class Set:
    # Constructor: Initializes an empty list to store set elements
    def __init__(self):
        self.elements = []

    # Adds an element to the set if it is not already present
    def add(self, element):
        assert element not in self.elements, "Elements must be unique!"
        self.elements.append(element)  # Append if unique

    # Removes an element if it exists in the set, raises an error if not
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)  # Remove if found
        else:
            # Raise an error if the element is not in the set
            raise KeyError(f"Element {element} not found in the set")

    # Checks if an element is in the set (returns True or False)
    def contains(self, element):
        return element in self.elements

    # Creates a new set that is the union of the current set and another set
    def union(self, other_set):
        new_set = Set()
        # Copy current elements to the new set
        new_set.elements = self.elements[:]
        # Add elements from the other set if they are not already included
        for element in other_set.elements:
            if element not in new_set.elements:
                new_set.elements.append(element)
        return new_set

    # Creates a new set that is the intersection of the current set and another set
    def intersection(self, other_set):
        new_set = Set()
        # Add elements that exist in both sets
        for element in self.elements:
            if element in other_set.elements:
                new_set.add(element)
        return new_set

    # Creates a new set with elements in the current set but not in the other set
    def difference(self, other_set):
        new_set = Set()
        # Add elements that are only in the current set
        for element in self.elements:
            if element not in other_set.elements:
                new_set.add(element)
        return new_set

    # Checks if the current set is a subset of another set
    def is_subset_of(self, other_set):
        # Return False if any element is missing in the other set
        for element in self.elements:
            if element not in other_set.elements:
                return False
        return True

    # Returns the number of elements in the set
    def __len__(self):
        return len(self.elements)

    # Returns a string representation of the set for easy printing
    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"