from linearmap import Map

if __name__ == '__main__':
    m = Map()
    m.add("foo", 1)
    m.add("bar", 3)
    m.add("baz", 3)
    for entry in m:
        print(f"{entry.key} - {entry.value}", end="\t")
