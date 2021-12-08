def fishlivesmatter(fishes, time):
    for i in range(time):
        fishes.append(fishes.pop(0))
        fishes[6] += fishes[8]
    return sum(fishes)

def main():
    fishes = [open('inputs/input6', 'r').readline().strip().split(',').count(str(i)) for i in range(8)]

    print("Part1 = {}".format(fishlivesmatter(fishes.copy(), 80)))
    print("Part2 = {}".format(fishlivesmatter(fishes.copy(), 256)))

if __name__ == '__main__':
    main()
