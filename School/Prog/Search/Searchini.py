def binary_search(theValues, target):
    low = 0
    high = len(theValues)-1

    while low <= high:
        mid = (high + low) // 2

        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False



if __name__ == "__main__":

    target_val = [50,11,91,77,93,53,19,40,6,19,23,38,80,22,5,39,41,56,36,58]
    alpha = sorted(target_val)

    print(binary_search(alpha, 6))

