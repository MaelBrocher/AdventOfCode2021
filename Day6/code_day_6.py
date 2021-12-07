def fishlivesmatter(fishes, time):
    for i in range(time):
        fishes.append(fishes.pop(0))
        fishes[6] += fishes[8]
    return sum(fishes)

def main():
    fishes = [0] * 9
    fresh_fishes = [0] * 9
    f = open('input.sql', 'r').readline().split(',')
    for fish in f:
        fishes[int(fish)] += 1
    for fish in f:
        fresh_fishes[int(fish)] += 1

    print("Part1 = {}".format(fishlivesmatter(fishes, 80)))
    print("Part2 = {}".format(fishlivesmatter(fresh_fishes, 256)))

if __name__ == '__main__':
    main()
