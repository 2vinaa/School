
from map import Map

if __name__ == '__main__':
    # Create a map and add some key-value pairs
    phone_book = Map()
    phone_book.add("Alice", "123-456")
    phone_book.add("Bob", "987-654")
    phone_book.add("Eve", "555-666")

    # Print the map
    print("Phone Book:", phone_book)

    # Access a value by key
    print("Alice's number:", phone_book.value_of("Alice"))

    # Update a value
    phone_book.add("Alice", "111-222")
    print("Updated Phone Book:", phone_book)

    # Check if a key exists
    print("Is Bob in the phone book?", "Bob" in phone_book)

    # Remove a key-value pair
    phone_book.remove("Eve")
    print("After removing Eve:", phone_book)
