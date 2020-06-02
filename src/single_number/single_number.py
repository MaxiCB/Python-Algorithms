'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
'''
Given a non-empty array of integers where every element appears twice except for one.
Find that single number.
You may assume that there will always be one odd-number-out and every other number
in the input shows up exactly twice.
'''
# O(log n)
def single_number(arr):
    # Create a set for reference to all values without dupes
    i=set(arr)
    # Iterate over the set
    for n in i:
        # Check for count of one in input arr
        if arr.count(n) == 1:
            return n

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")