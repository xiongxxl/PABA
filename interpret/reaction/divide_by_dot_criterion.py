

def divide_by_dot_criterion(dot_criterion,functional_arrays):
    # Initialize two lists.
    less_dot_criterion = []
    greater_equal_dot_criterion= []
    # Iterate through each tuple.
    for t in functional_arrays:
        # Evaluate each element in the tuple.
        if all(x < dot_criterion for x in t):
            less_dot_criterion.append(t)
        else:
            greater_equal_dot_criterion.append(t)
    return less_dot_criterion,greater_equal_dot_criterion

if __name__ == "__main__":
    dot_criterion=8
    functional_arrays=((9, 10), (4,), (8,), (0,), (3, 4), (7, 8))
    less_dot_criterion,greater_equal_dot_criterion=divide_by_dot_criterion(dot_criterion,functional_arrays)

    # 输出分类结果
    print("less than dot_criterion.:", less_dot_criterion)
    print("greater than or equal to dot_criterion:", greater_equal_dot_criterion)