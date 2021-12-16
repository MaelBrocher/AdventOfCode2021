from colorama import *
init(autoreset=True)

def pliemoicebordel(origami, fold, part1):
    for f in fold:
        no = set()
        for (x,y) in origami[-1]:
            if f[0] == 'y' and y > f[1]: 
                y = (2*f[1]) - y
            elif f[0] == 'x' and x > f[1]:
                x = (2*f[1]) - x
            no.add((x,y))
        origami.append(no)
        if part1:
            break
    last = {'x': max([i[0] for i in origami[-1]]), 'y': max([i[1] for i in origami[-1]])}
    first = {'x': min([i[0] for i in origami[-1]]), 'y': min([i[1] for i in origami[-1]])}
    if part1 == False:
        for r in range(first['y'],last['y']+1):
            for c in range(first['x'],last['x']+1):
                if (c,r) in origami[-1]:
                    print(Fore.RED + '▓', end='')
                else:
                    print(' ', end='')
            print('\n', end='')
    if part1 :
        return len(origami[-1])


def main():
    coords, fold = open('input.sql').read().split('\n\n')
    coords = {(int(i[0]), int(i[1])) for i in [i.split(',') for i in coords.split()]}
    fold = [[j.split('=')[0],int(j.split('=')[1])] for j in [i.split(' ')[2] for i in fold.split('\n')]]
    print("Part1 = {}".format(pliemoicebordel([list(coords)], fold, True)))
    print("Part2 =")
    pliemoicebordel([list(coords)], fold, False)

    return

if __name__ == '__main__':
    main()