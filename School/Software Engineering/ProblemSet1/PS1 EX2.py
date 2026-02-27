from __future__ import annotations
from numpy import sqrt


class Vector:
    def __init__(self, x:int, y:int, z:int):
        self.vect = [x,y,z]

    def __add__(self, other:Vector):
        res = []
        for i in range(len(self.vect)):
            res.append(self.vect[i] + other.vect[i])
        return res

    def length(self):
        return sqrt((self.vect[0]**2)+(self.vect[1]**2)+(self.vect[2]**2))

    def scalar_product(self,scalar):
        res = []
        for i in range(len(self.vect)):
            res.append(self.vect[i] * scalar)
        return res

    def negative_prod(self):
        return self.scalar_product(-1)

    def display(self):
        for i in self.vect:
            print(i)

if __name__ == "__main__":
    v1 = Vector(1,5,10)
    v2 = Vector(-1,9,3)

    print(v1.length())
    print(v1.scalar_product(2))
    print(v1.negative_prod())
    print(v1.__add__(v2))
