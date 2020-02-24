import sys
from collections import namedtuple
from operator import itemgetter

Item = namedtuple('Item', ['index', 'size', 'value'])


def knapsack_solver(items, capacity, cache=[]):
    temp_list = items

    temp_capacity = capacity

    output = cache

    temp_highest = 0
    temp_index = 0
    temp_size = 0

    temp_lowest = min(temp_list, key=itemgetter(2))[2]

    while temp_capacity > temp_lowest:

        if len(temp_list) > 1:
            for item in temp_list:
                if item.value > temp_highest:
                    temp_highest = item.value
                    temp_index = item.index - 1
                    temp_size = item.size
                    if temp_capacity > temp_size:
                        temp_capacity -= temp_size
                        output.append(temp_list[temp_index])
                        temp_list.remove(temp_list[temp_index])
                        temp_highest = 0
                        temp_index = 0
                        temp_size = 0
                    else:
                        print('here')
                        temp_index = item.index - 1
                        temp_list.remove(temp_list[temp_index])
        else:
            print(output)
    print(output)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')
