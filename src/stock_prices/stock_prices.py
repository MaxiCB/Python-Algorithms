
import argparse


def find_max_profit(prices):
    largest = 0
    smallest = prices[0]
    for i in prices:
        # Iterate over all prices and find the largest
        # Set the smallest temporarily to the very first iteration then the check can happen
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i

    best_margin = largest - smallest
    print(best_margin)
    return best_margin


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
