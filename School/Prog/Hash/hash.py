from arr import Array

class Hash:
    def __init__(self, len):
        self.hash = Array(len)
        self.flag = "|>"

    def hash_function(self, name:str):
        x = 0
        for element in name:
            x += ord(element)
        return x % len(self.hash)

    def insert(self, item):
        if item in self:
            return "You cant add an item with the same key"
        else:
            index = self.hash_function(item)
            if self.hash[index] is None:
                self.hash[index] = item
            else:
                counter = 0
                for i in range(len(self.hash)):
                    if self.hash[i] is not None:
                        counter +=1
                if counter == len(self.hash):
                    return "You cannot add to this Hash as it is full"

                while True:
                    index = (index + 1) % len(self.hash)
                    if self.hash[index] is not None:
                        pass
                    elif self.hash[index] is None or self.hash[index] == self.flag:
                        self.hash[index] = item
                        return f"{item} has been added at {index}"
                    else:
                        counter = 0
                        for i in range(len(self.hash)):
                            if self.hash[i] is not None:
                                counter += 1
                        if counter == len(self.hash):
                            return "You cannot add to this Hash as it is full"

    def remove(self, item):
        if item in self:
            index = self.hash_function(item)
            self.hash[index] = self.flag
            return f"{item} has been removed"
        else:
            return "Cant remove an item not contained"

    def __contains__(self, item):
        start_idx = self.hash_function(item)
        index = start_idx

        for i in range(len(self.hash)):
            current = self.hash[index]
            if current is None:
                return False
            if current == item:
                return True
            index = (index + 1) % len(self.hash)
            if index == start_idx:
                break
        return False


if __name__ == "__main__":