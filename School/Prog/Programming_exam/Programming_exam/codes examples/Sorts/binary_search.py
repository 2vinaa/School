import time
import random

# Function to perform linear search
def linear_search(items, key):
    # Iterate through the list
    for i, item in enumerate(items):
        # If the key is found, return its index
        if key == item:
            return i
    # If the key is not found, return -1
    return -1

# Function to perform binary search (on a sorted list)
def binary_search(items, key):
    l = 0  # Lower bound of the search range
    h = len(items) - 1  # Upper bound of the search range

    while l <= h:
        mid = (l + h) // 2  # Find the middle index
        if items[mid] == key:
            return mid  # Key found, return index
        elif items[mid] < key:
            l = mid + 1  # Search in the right half
        else:
            h = mid - 1  # Search in the left half

    return -1  # If the key is not found, return -1

# Function to generate a sorted list of random integers
def generate_random_sorted_list(n):
    l = list()  # Initialize an empty list
    for i in range(n):
        l.append(random.randint(0, 10000000))  # Add random numbers in the range 0-10,000,000
    l.sort()  # Sort the list in ascending order
    return l  # Return the sorted list

if __name__ == '__main__':
    # Generate a sorted list with 10,000,000 random numbers
    my_list = generate_random_sorted_list(10000000)

    # Measure execution time for binary search
    t1 = time.time()
    print(binary_search(my_list, 4500))  # Search for the number 4500
    t2 = time.time()
    print("Execution time (binary search): {}".format(t2 - t1))

    # Measure execution time for linear search
    t1 = time.time()
    print(linear_search(my_list, 4500))  # Search for the number 4500
    t2 = time.time()
    print("Execution time (linear search): {}".format(t2 - t1))