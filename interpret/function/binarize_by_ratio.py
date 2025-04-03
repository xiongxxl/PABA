import numpy as np
def binarize_by_ratio(arr,ratio):
    #acording to ratio binarize the array
    #import numpy as np
    #arr = np.random.rand(4, 5)
    # print("Original array:")
    # print(arr)
    flat_arr = arr.flatten()
    sorted_indices = np.argsort(flat_arr)
    # front ratio to set 0
    cutoff = int(len(flat_arr) * ratio)
    # Create a new one-dimensional array.
    new_flat_arr = np.ones_like(flat_arr)
    new_flat_arr[sorted_indices[:cutoff]] = 0
    # Convert the one-dimensional array back into a two-dimensional array.
    new_arr = new_flat_arr.reshape(arr.shape)
    return(new_arr)