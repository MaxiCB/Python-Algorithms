import sys
from itertools import *

occ_total = 0


# This does not produce all possible combinations
def find_all_combos(arr, index, num, reduced):
    global occ_total
    # If reduced is less than 0 we are done
    if reduced < 0:
        return occ_total

    if reduced == 0:
        for i in range(index):
            print(arr[i], end=" ")
        print(" ")
        occ_total += 1
        return occ_total

    prev = 1 if (index == 0) else arr[index - 1]

    for k in range(prev, num + 1):
        arr[index] = k
        find_all_combos(arr, index + 1, num, reduced - k)

    # print(occ_total, 'total\n')
    return occ_total


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    arr = [0] * n
    return find_all_combos(arr, 0, n, n)


if __name__ == '__main__':
    print(eating_cookies(3))
