from Maps import Map, _MapEntry

if __name__ == "__main__":
    map1 = Map()

    map1.add("banana", "alpha")
    map1.add("dsadsad", "deha")
    map1.add("ban", "aa")

    print(list(map1))

    print(map1.valueOf("banana"))

    map1.remove(input("What to remove\n"))

    print(map1._findPosition(input("What key?\n")))



