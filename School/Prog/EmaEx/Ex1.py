

class Set:
    def __init__(self, *init_elements):
        self.the_elements = []
        for element in init_elements:
            if element not in self.the_elements:
                self.the_elements.append(element)


    def __len__(self):
        return len(self.the_elements)


    def add_element(self, element):
        if element not in self.the_elements:
            self.the_elements.append(element)
            return "Element has been added"
        return "Element is already added"


    def remove_element(self, element):
        if element not in self.the_elements:
            self.the_elements.remove(element)
            return "Element has been removed"
        return "Element wasnt in the set"


    def union(self, other):
        initialiunion = []
        true_union = []
        for element in self.the_elements:
            initialiunion.append(element)

        for element in other.the_elements:
            initialiunion.append(element)

        for i in initialiunion:
            if i not in true_union:
                true_union.append(i)
            else:
                pass

        return true_union



    def intersection(self, other):
        iniintersect = []
        trueintersect = []

        for element in self.the_elements:
            iniintersect.append(element)

        for element in other.the_elements:
            if element in iniintersect:
                trueintersect.append(element)
            else:
                pass

        return trueintersect


    def subset(self, other):
        check = 0
        if len(self.the_elements) > len(other.the_elements):
            for i in self.the_elements:
                for j in other.the_elements:
                    if i == j:
                        check += 1
                    else:
                        pass

                    if check == len(other.the_elements):
                        return f"{other} is a subset of {self}"

        else:
            return "This cannot be a subset as A is smaller than B"



    def difference(self,other):
        newdiff = []
        for i in self.the_elements:
            if i not in other.the_elements:
                newdiff.append(i)

        return newdiff


    def __add__(self, set_b):
        return self.union(set_b)

    def __mul__(self, set_b):
        return self.intersection(set_b)

    def __sub__(self, set_b):
        return self.difference(set_b)






