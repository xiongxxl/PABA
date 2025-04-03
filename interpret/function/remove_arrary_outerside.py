import numpy as np
def remove_outer_layer(square_matrix):
    # Calculate the size of the new array
    n = len(square_matrix)
    inner_size = n - 2
    # Create a new array to store the internal elements.
    inner_matrix = [[0] * inner_size for _ in range(inner_size)]

    # Copy the internal elements to the new array
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            inner_matrix[i - 1][j - 1] = square_matrix[i][j]
            inner_matrix=np.array(inner_matrix)
    return inner_matrix
