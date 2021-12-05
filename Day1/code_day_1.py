def count(data, window=1):
    return sum(1 for d1, d2 in zip(data, data[window:]) if d1 < d2)

def main():
    f = open("input.txt", "r")
    data = [int(line) for line in f.readlines()]
    print("Part 1 = {}".format(count(data)))
    print("Part 2 = {}".format(count(data, window=3)))
    
if __name__ == '__main__':
    main()