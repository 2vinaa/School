def find_position_in_memory(indexes, dimension):
    # Ensure the number of indexes matches the number of dimensions
    assert len(indexes) == len(dimension)

    dim = len(dimension)  # Number of dimensions
    index = 0             # Final computed memory position

    # Loop over each dimension
    for i in range(dim):
        partial_result = indexes[i]  # Start with the current index value

        # Multiply by the size of all dimensions after i
        for k in range(i + 1, dim):
            partial_result *= dimension[k]

        # Add the partial result to the total index
        index += partial_result

    return index  # Return the computed linear memory position


# Example usage: computes the flat memory index of element (2, 3, 4, 5)
# in a 4D array with shape (4, 5, 6, 7), assuming row-major order
print(find_position_in_memory(indexes=(2, 3, 4, 5), dimension=(4, 5, 6, 7)))