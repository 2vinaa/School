import random
import time


# Function to generate a list of n random integers in the range 0 to 10,000,000
def generate_random_list(n):
    l = list()
    for i in range(n):
        l.append(random.randint(0, 10000000))
    return l


# Function to check if a list is sorted in ascending order
def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


# Selection sort algorithm
# Finds the smallest element in the unsorted portion and swaps it with the first unsorted element
def selection_sort(l):
    for i in range(len(l) - 1):
        min_idx = i
        # Find the minimum element in the remaining unsorted portion
        for j in range(i + 1, len(l)):
            if l[j] < l[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted portion
        if l[min_idx] < l[i]:
            l[i], l[min_idx] = l[min_idx], l[i]
    return l


# Bubble sort algorithm
# Repeatedly swaps adjacent elements if they are in the wrong order
def bubble_sort(l):
    n = len(l)

    # If the list is already sorted, return it immediately
    if is_sorted(l):
        return l

    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l


# Insertion sort algorithm
# Builds the sorted list one element at a time by inserting elements in the correct position
def insertion_sort(l):
    for i in range(1, len(l)):
        value = l[i]
        pos = i
        # Shift elements to the right to find the correct position for the current element
        while pos > 0 and value < l[pos - 1]:
            l[pos] = l[pos - 1]
            pos -= 1
        l[pos] = value
    return l


if __name__ == '__main__':
    n = 7000  # Number of elements in the list

    # Measure execution time of Bubble Sort
    my_list = generate_random_list(n)
    t1 = time.time()
    bubble_sort(my_list)
    t2 = time.time()
    print("execution time bubble sort: {}".format(t2 - t1))

    # Measure execution time of Selection Sort
    my_list = generate_random_list(n)
    t1 = time.time()
    selection_sort(my_list)
    t2 = time.time()
    print("execution time selection sort: {}".format(t2 - t1))

    # Measure execution time of Insertion Sort
    my_list = generate_random_list(n)
    t1 = time.time()
    insertion_sort(my_list)
    t2 = time.time()
    print("execution time insertion sort: {}".format(t2 - t1))
