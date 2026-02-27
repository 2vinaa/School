from Array import Array
from LinkedList import LinkedList

class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MapEntry):
            return self.key == other.key
        return False

    def __str__(self):
        return f"{self.key}: {self.value}"

class HashMap:
    def __init__(self, capacity=16):
        self.hash = Array(capacity)
        self.capacity = capacity
        self.size = 0

    def _hash(self, key):
        return sum((i + 1) * ord(c) for i, c in enumerate(key)) % self.capacity

    def put(self, key, value): #If the key exists, update the value.

        ind = self._hash(key)
        _map = MapEntry(key, value)

        if self.hash[ind] is None:
            self.hash[ind] = LinkedList()
            self.hash[ind].append(_map)
            self.size += 1
        else:
            updated = self.hash[ind].update(_map)
            if updated:
                return "The MapEntry Has Been Updated"
            else:
                self.hash[ind].append(_map)
                self.size += 1
                return "The MapEntry Has Been Added"

    def get(self, key):
        search_entry = MapEntry(key, None)
        ind = self._hash(key)
        if self.hash[ind] is None:
            return None
        x = self.hash[ind].find(search_entry)
        if x is not None:
            return x.value
        else:
            return None

    def remove(self, key):
        ind = self._hash(key)
        mapind = MapEntry(key, None)
        if self.hash[ind] is None:
            return "You cannot remove something that isnt there"
        else:
            x = self.hash[ind].find(mapind)
            if x is not None:
                self.hash[ind].remove(x)
                self.size -= 1
                return "item has been removed"

    def contains(self, key):
        ind = self._hash(key)
        search_entry = MapEntry(key, None)
        pass
        if self.hash[ind] is None:
            return False
        else:
            if self.hash[ind].find(search_entry):
                return True
            else:
                return False


    def __len__(self):
        return self.size

    def __str__(self):
        result = {}
        for i in range(self.capacity):
            if self.hash[i] is None:
                continue
            else:
                current = self.hash[i].head
                while current:
                    result[current.value.key] = current.value.value  # or current.data, depending on your node
                    current = current.next
        return str(result)


if __name__ == "__main__":
    print("=== HashMap Test ===")
    hmap = HashMap()

    # Insert entries
    hmap.put("Alice", 100)
    hmap.put("Bob", 200)
    hmap.put("Charlie", 300)
    hmap.put("Alice", 150)  # Update value
    print()

    # Retrieve values
    assert hmap.get("Alice") == 150
    assert hmap.get("Bob") == 200

    # Contains check
    assert hmap.contains("Charlie") is True
    assert hmap.contains("David") is False

    # Remove
    hmap.remove("Charlie")
    assert hmap.contains("Charlie") is False

    # Length
    assert len(hmap) == 2

    print("HashMap contents:", hmap)
    print("HashMap tests passed!\n")