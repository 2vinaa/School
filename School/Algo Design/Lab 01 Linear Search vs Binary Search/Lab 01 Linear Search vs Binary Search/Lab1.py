import random as rand
import sys
import time
import matplotlib.pyplot as plt


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1, using divide and conquer
def binary_search_divide_and_conquer(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_divide_and_conquer(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_divide_and_conquer(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


def linear_function(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            pass
    return 0
# Returns index of x in arr if present, else -1, using brute force
# def brute_force(arr, low, high, x):

def random_arr(ls_size, ls_number):
    list_of_lists = []
    for i in range(ls_number):
        random_list = [rand.randint(0, sys.maxsize) for j in range(ls_size)]
        sorted_rand_list = sorted(random_list)
        list_of_lists.append(sorted_rand_list)
    return list_of_lists

def time_function(size, number_of_lists):
    x = random_arr(size, number_of_lists)  # x should be a list of presorted lists
    total_time_linear = 0
    total_time_binary = 0
    for lst in x:

        start = time.time()
        linear_function(lst, 15)
        end = time.time()
        total_time_linear += (end - start)

        startbinary = time.time()
        binary_search_divide_and_conquer(lst, 0, len(lst) - 1, 15)
        endbinary = time.time()
        total_time_binary += (endbinary - startbinary)

    averagetimebinary = total_time_binary / number_of_lists
    averagetimelinear = total_time_linear / number_of_lists

    print(f"{averagetimebinary} is binary time, {averagetimelinear} is linear time")
    return averagetimebinary, averagetimelinear


if __name__ == "__main__":
# Test array
    arr = [ 2, 3, 4, 10, 40 ]
    x = 10
 
# Function call
    result = binary_search_divide_and_conquer(arr, 0, len(arr)-1, x)
    result_lin = linear_function(arr, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")


    if result_lin != 0:
        print("Element is present at index", str(result_lin))
    else:
        print("Element is not present in array")


    # Run timing tests for different sizes
    sizes = [1000, 10000, 50000, 100000, 200000]
    times_binary = []
    times_linear = []

    for size in sizes:
        binary_t, linear_t = time_function(size, 10)
        times_binary.append(binary_t)
        times_linear.append(linear_t)

    # Plotting results
    plt.figure(figsize=(10,6))
    plt.plot(sizes, times_binary, label='Binary Search Time')
    plt.plot(sizes, times_linear, label='Linear Search Time')
    plt.xlabel('Size of Array')
    plt.ylabel('Average Time (seconds)')
    plt.title('Average Time for Search Algorithms by Array Size')
    plt.legend()
    plt.grid(True)
    plt.show()