'''
Input: a List of integers
Returns: a List of integers
'''
'''
Moves each non-zero integer to the left side of the array
Non-zero integers do not have to be sorted
'''
def moving_zeroes(arr):
    # Iterate over the array
    # Check if element is non-zero
    # If non-zero move to left side
    # If zero move to right side

    # Could use a supporting array for values
    zeros = []
    non_zero = []
    for item in arr:
        if item == 0:
            zeros.append(item)
        else:
            non_zero.append(item)
    non_zero += zeros
    return non_zero



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")