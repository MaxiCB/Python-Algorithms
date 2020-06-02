import sys
from collections import namedtuple
from operator import itemgetter

Item = namedtuple('Item', ['index', 'size', 'value', 'weight'])
ModItem = namedtuple('ModItem', ['index', 'size', 'value', 'weight'])

def knapsack_solver(items, capacity, cache=[]):
    temp = []
    for item in items:
        temp.append(ModItem(item.index, item.size, item.value, item.value*100//item.size))
    temp.sort(key=lambda item:item[3], reverse=True)
    curr = 0
    chosen = []
    value = 0
    for item in temp:
        if(curr <= capacity) and (curr + item.size) < capacity:
            curr += item.size
            chosen.append(item.index)
            value += item.value
    chosen.sort()
    return {"Value": value, "Chosen": chosen}

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
