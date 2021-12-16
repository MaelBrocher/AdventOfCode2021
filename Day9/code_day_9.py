from collections import Counter

def is_lowest(x, y, data):
    values = []
    for xt, yt in zip([x,x,x+1,x-1],[y+1,y-1,y,y]):
        try :
            if xt >= 0 and yt >= 0:
                values.append(data[xt][yt])
        except IndexError:
            pass
    return all(v > data[x][y] for v in values)

def part1(data):
    res = [[data[x][y]+1 for y in range(0, len(data[x])) if is_lowest(x,y,data)] for x in range(0,len(data))]
    return sum(map(sum,res))

def zoomba(data,x,y):
    downhill = None
    for dx, dy in zip([x,x,x+1,x-1],[y+1,y-1,y,y]):
        if dx in range(len(data)) and dy in range(len(data[0])):
            if data[x][y] > data[dx][dy]:
                downhill = (dx, dy)
    if downhill is None:
        return (x, y)
    return zoomba(data,*downhill)

def part2(data):
    basins = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] != 9:
                basins.append(zoomba(data, x, y))
    ret = 1
    for b, common in Counter(basins).most_common(3):
        ret *= common
    return ret

def main():
    inp = [[int(n) for n in l.strip()] for l in open('input.sql').readlines()]
    print("Part 1 = {}".format(part1(inp)))
    print("Part 1 = {}".format(part2(inp)))
    return

if __name__ == '__main__':
    main()