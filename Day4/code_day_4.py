from itertools import chain
import sys

def compute(boards, numbers, lastboard=False):
    drawn, remaining = set(), set(range(len(boards)))
    for number in map(int, numbers.split(",")):
        drawn.add(number)
        for i in set(remaining):
            if any(line <= drawn for line in boards[i]):
                remaining.remove(i)
                if len(remaining) == len(boards) - 1 or not remaining:
                    print(number * sum(set.union(*boards[i]) - drawn))

def main():
    numbers, *data = open("input.sql", "r").read().strip().split("\n\n")

    boards = []
    for board in data:
        rows = [
            [int(x) for x in row.split()] for row in board.split("\n")
        ]
        boards.append([set(line) for line in chain(rows, zip(*rows))])
    compute(boards, numbers)
    return

if __name__ == '__main__':
    main()