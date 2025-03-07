from linearset import Set

if __name__ == "__main__":
    s1 = Set(1, 2, 4, 5, 52, 98989)
    print(s1)

    s2 = Set(2,4,52, 2833328)

    print(s2.is_proper_subset(s1))

    print(s1 + s2)
    print(s1 * s2)
    print(s1 - s2)
    print(s1<s2)