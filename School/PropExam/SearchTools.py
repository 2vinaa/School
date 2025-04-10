from random import randint


class StudentDirectory:
    def __init__(self):
        self.lista = []


    def add_unit_to_list(self, unit):
        if unit not in self.lista:
            self.lista.append(unit)




    def sort_list(self):
        n = len(self.lista)

        for i in range(n-1):
            for j in range(n-i-1):
                if self.lista[j] > self.lista[j+1]:
                    tmp = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = tmp



    def linearsearch(self, value):
        self.sort_list()
        n = len(self.lista)
        for i in range(n):
            if self.lista[i] == value:
                return f"The {value} has been found in position {i}"

            else:
                return "The value is not in the list"


    def binary_search(self, target):
        self.sort_list()
        low = 0
        high = len(self.lista) - 1

        while low <= high:
            midpoint = (high+low) // 2
            if self.lista[midpoint] == target:
                return f"The {target} has been found in position {midpoint}"
            elif target < self.lista[midpoint]:
                high = midpoint-1
            else:
                low = midpoint+1

        return "The value is not in the list"



if __name__ == "__main__":


    a = StudentDirectory()
    a.add_unit_to_list(139203)
for i in range(10):
    a.add_unit_to_list(randint(100000, 999999))

print(a.binary_search(139203))
print(a.linearsearch(139203))




