from set import Set
from random import randint

if __name__ == "__main__":

    set1 = Set()
    set2 = Set()

    for i in range(10):
        set1.add(randint(1, 20))
        set2.add(randint(1, 20))

    for element in set1:
        print(element)
    for element in set2:
        print(element)

    x = set1.remove(int(input("What element to remove\n")))
    for element in set1:
        print(element)

    print(set1.is_Subset_Of(set2))


    x = set1.union(set2)
    print(list(x))

    y = set1.intersect(set2)
    print(list(y))

    z = set1.difference(set2)
    print(list(z))