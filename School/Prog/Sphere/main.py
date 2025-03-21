from txtbook import _BagIterator

if __name__ == "__main__":

    x = _BagIterator(["banana", "africa", "scemo_tommaso", "albania"])



    while True:
        try:
            y = x.__next__()
            print(y)
        except StopIteration:
            break


