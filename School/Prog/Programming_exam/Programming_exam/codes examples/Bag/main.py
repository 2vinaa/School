# Example usage
from Bag import Bag

if __name__ == "__main__":
    bag = Bag()
    bag.add("apple")
    bag.add("banana")
    bag.add("cherry")

    print("Bag contains:")
    for item in bag:
        print(item)

    print("\nRemoving 'banana'...")
    bag.remove("banana")

    print("\nBag now contains:")
    for item in bag:
        print(item)