# Input - List && Int
# Output - List

# Sliding window of available elements
# Window is i+k
# Grab max value in the window
# Append it to a output list

# This hangs when testing with large input
# O(N2)?
def sliding_window_max_trash(nums, k):
    output = []
    temp = []

    for i, _ in enumerate(nums):
        if i + k <= len(nums):
            for j in range(i, i+k):
                if j < len(nums):
                    temp.append(nums[j])
            temp.sort()
            temp.reverse()
            output.append(temp[0])
            temp.clear()
    return output

def sliding_window_max(nums, k):
    output = []
    curr_index = 0

    while curr_index + k != len(nums) + 1:
        temp = []
        for i in range(k):
            temp.append(nums[curr_index + i])
        output.append(max(temp))
        curr_index += 1
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")