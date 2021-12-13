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

def part2(data):
    return 0

def main():
    inp = [[int(n) for n in l.strip()] for l in open('input.sql').readlines()]
    print("Part 1 = {}".format(part1(inp)))
    print("Part 1 = {}".format(part2(inp)))
    return

if __name__ == '__main__':
    main()