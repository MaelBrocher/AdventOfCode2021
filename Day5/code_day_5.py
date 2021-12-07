import numpy as np

def overlap(positions, diag=False):
    tab = [[0 for i in range(max(positions)[0][0]+1)] for i in range(max(positions)[0][0]+1)]
    for line in positions:
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                tab[i][x1] += 1
        elif y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                tab[y1][i] += 1
    flat = np.concatenate(tab)
    return len([l for l in flat if l > 1])

def main():
    positions = [[[int(p) for p in pos.split(',')] for pos in line.split(' -> ')] for line in open("input.sql", 'r').readlines()] 
    print("Part 1 = {}".format(overlap(positions)))
    print("Part 1 = {}".format(overlap(positions, True)))

if __name__ == '__main__':
    main()