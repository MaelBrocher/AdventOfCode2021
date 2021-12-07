import numpy as np

def main():
    crabs = [int(crab) for crab in open("input.sql", "r").readline().split(',')]

    print("Part 1: {}".format(int(sum(abs(crab - np.median(crabs)) for crab in crabs))))

    print("Part 2: {}".format(int(sum(abs(crab - (round(np.mean(crabs))-1)) * (abs(crab - (round(np.mean(crabs))-1))+1)//2 for crab in crabs))))

if __name__ == '__main__':
    main()