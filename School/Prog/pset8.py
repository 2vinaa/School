"""def primenumber(inputnumber):
    if inputnumber <= 1:
        return True
    
    for i in range(2, inputnumber//2 + 1):
        if inputnumber % i == 0:
            return False
        
    return True

if __name__ == "__main__":
    for j in range(101):
        if primenumber(j) == True:
            print(f"{j} is a prime number")"""



#-------------------------------------------------------------------------------------------------------------------------

"""import math

def calculate_term(x, n):
    term = 1
    for j in range(1, n+1):
        term *= x / j
    return term


def sin(x, num_terms):
    sign = 1
    term = 0
    for i in range(0, num_terms):
        term += sign * calculate_term(x, i*2 + 1)
        
        sign = -sign
    return term

def cos(x, num_terms):
    sign = 1
    term = 0
    for i in range(0, num_terms):
        term += sign * calculate_term(x,i * 2)
        sign = -sign
    return term


if __name__ == "__main__":
    values = [0, math.pi/6, math.pi/4, math.pi/3 , math.pi/2]

    for x in values:
        print(f"sin = {math.sin(x)}")
        for i in range(1,11):
            print(f"sin = {sin(x, i)} with term {i}")

    for y in values:
        print(f"cos = {math.cos(y)}")
        for j in range(1,11):
            print(f"cos = {cos(y, j)} with term {j}")"""

#--------------------------------------------------------------------------------------------------------------------------------------------------
from random import randint


def trivector(x,y,z):
    x = int(input("insert the x value"))
    y = int(input("insert the y value"))
    z = int(input("insert the z value"))
    vector = []
    vector.append(x)
    vector.append(y)
    vector.append(z)
    return vector

def randvect(x,y,z):
    lowerlimitr = int(input("Insert the lower limit"))
    upperlimitr = int(input("Insert the upper limit"))
    if lowerlimitr >= upperlimitr:
        print("not possible, reinsert the lower limit")
        lowerlimitr = int(input("Insert the lower limit"))

    x = randint(lowerlimitr, upperlimitr)
    y = randint(lowerlimitr, upperlimitr)
    z = randint(lowerlimitr, upperlimitr)
    vector = []
    vector.append(x)
    vector.append(y)
    vector.append(z)
    return vector

def vecprint(vector1, vector2):
    print(vector1)
    print(vector2)

def vectsum(vector1, vector2):
    vectorxs = vector1 + vector2
    return vector1 + vector2

def vectmult(vector, scalar):
    scalar = int(input("Insert the scalar"))
    return vector * scalar



if __name__ == "__main__":

    x = 0
    y = 0
    z = 0
    vec1 = trivector(x , y ,z)
    print(vec1)