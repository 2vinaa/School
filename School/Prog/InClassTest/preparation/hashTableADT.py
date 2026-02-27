from custom_array import Array

class HashTableAdt:

    def __init__(self, capacity):
        self.capacity = capacity
        self.array = Array(capacity)
        self.flag = "|>"  # Special marker for deleted items

    def __hash(self, key):
        x = 0
        for char in key:
            x += ord(char)
        return x % self.capacity

    def __is_empty(self, index):
        return self.array[index] is None or self.array[index] == self.flag

    def __get_key(self, value):
        start_index = self.__hash(value)
        index = start_index

        while self.array[index] is not None:
            if self.array[index] == value:
                return index
            index = (index + 1) % self.capacity
            if index == start_index:
                break

        return None

    def insert(self, value):
        if value in self:
            raise ValueError(f"{value} is already in the hash table")

        start_index = self.__hash(value)
        index = start_index

        while not self.__is_empty(index):
            index = (index + 1) % self.capacity
            if index == start_index:
                raise OverflowError("Hash table is full")

        self.array[index] = value

    def remove(self, value):
        index = self.__get_key(value)
        if index is not None:
            self.array[index] = self.flag

    def __contains__(self, value):
        return self.__get_key(value) is not None


# Example usage and tests
my_hash_table = HashTableAdt(capacity=10)

my_hash_table.insert("Anna")
my_hash_table.insert("Luca")
my_hash_table.insert("Kevin")
my_hash_table.insert("Jonathan")
my_hash_table.insert("Marco")

#try:
    #my_hash_table.insert("Luca")  # should raise ValueError
#except ValueError as e:
    #print("Expected error:", e)

my_hash_table.remove("Jonathan")

assert "anna" not in my_hash_table, "__contains__ should be case-sensitive and return False"
assert "Jonathan" not in my_hash_table, "__contains__ should return False after removal"