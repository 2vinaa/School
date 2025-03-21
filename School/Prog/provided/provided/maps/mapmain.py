from linearmap import Map

if __name__ == "__main__":

    m1 = Map()

    m1.add("sfrongus", 2)
    m1.add("smongus", 5)
    m1.add("smingus", 89)
    print(m1.keyArray())

    print(m1.__iter__().__next__())
