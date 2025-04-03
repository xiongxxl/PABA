import numpy as np
def binarize_by_ratio(arr,ratio):


    flat_arr = arr.flatten()
    # 对一维数组进行排序并获取排序后的索引
    sorted_indices = np.argsort(flat_arr)

    # front ratio to set 0
    cutoff = int(len(flat_arr) * ratio)
    # Create a new one-dimensional array.
    new_flat_arr = np.ones_like(flat_arr)

    new_flat_arr[sorted_indices[:cutoff]] = 0

    # Avatar
    # Reshape the one-dimensional array back into a two-dimensional array.
    new_arr = new_flat_arr.reshape(arr.shape)

    #print("Processed array:")
    #print(new_arr)
    return(new_arr)

if __name__ =="__main__":
    # acording to ratio binarize the array
    # Create a sample two-dimensional array.
    arr = np.random.rand(5, 5)  # Generate a 4x5 random array.

    print("Original array:")
    print(arr)
    ratio=0.9
    new_arr=binarize_by_ratio(arr, ratio)
    print(new_arr)
