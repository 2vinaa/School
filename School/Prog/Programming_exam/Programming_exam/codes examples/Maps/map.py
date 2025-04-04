# Define a helper class to represent key-value pairs
class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # Allow comparison between MapEntry objects based on the key
    def __eq__(self, other):
        if isinstance(other, MapEntry):
            return self.key == other.key
        return False

    # Provide a string representation for printing
    def __str__(self):
        return f"{self.key}: {self.value}"


# Define the Map ADT using a list of MapEntry objects
class Map:
    def __init__(self):
        self.entries = []  # List to store MapEntry objects

    # Adds a key-value pair or updates the value if the key already exists
    def add(self, key, value):
        for entry in self.entries:
            if entry.key == key:
                entry.value = value  # Update value if key exists
                return
        # If key does not exist, create a new MapEntry and add it
        self.entries.append(MapEntry(key, value))

    # Removes a key-value pair by key
    def remove(self, key):
        for i, entry in enumerate(self.entries):
            if entry.key == key:
                self.entries.pop(i)
                return
        raise KeyError(f"Key {key} not found in the map")

    # Returns the value associated with a key
    def value_of(self, key):
        for entry in self.entries:
            if entry.key == key:
                return entry.value
        raise KeyError(f"Key {key} not found in the map")

    # Checks if a key exists in the map
    def __contains__(self, key):
        return any(entry.key == key for entry in self.entries)

    # Returns the number of key-value pairs in the map
    def __len__(self):
        return len(self.entries)

    # Returns a string representation of the map for easy printing
    def __str__(self):
        return "{" + ", ".join(str(entry) for entry in self.entries) + "}"
