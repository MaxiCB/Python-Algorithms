import sys
from itertools import *


def rock_paper_scissors(n, arr=['rock', 'paper', 'scissors']):
    if len(arr) == 0:
        return 0
    # Convert the list of tuples into a list of lists (This applies to all returns below)
    # This does not show all possible permutations possible
    # return [list(ele) for ele in list(combinations_with_replacement(arr, n))]
    # This does not do have the ability to repeat elements multiple times
    # return [list(ele) for ele in list(permutations(arr, n))]
    #
    # What I was looking for is called Cartesian Product.
    # This provides repeating permutation and all possible outcomes
    return [list(ele) for ele in list(product(arr, repeat=n))]


if __name__ == "__main__":
    print(rock_paper_scissors(2))


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
