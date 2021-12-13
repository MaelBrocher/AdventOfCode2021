from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

def printSquid(data):
    for x,l in enumerate(data):
        for y, squid in enumerate(l):
            if squid == 0:
                print(Fore.YELLOW + Style.BRIGHT + str(squid),end='')
            else:
                print(Style.DIM + str(squid),end='')
        print()
    print()

def too_brigth(data, x, y):
    for xt, yt in zip([x-1,x-1,x-1,x,x+1,x+1,x+1,x],[y-1,y,y+1,y+1,y+1,y,y-1,y-1]):
        try :
            if xt >= 0 and yt >= 0:
                if data[xt][yt] >= 0:
                    data[xt][yt] += 1
                if data[xt][yt] >= 9:
                    data[xt][yt] = -1
                    too_brigth(data,xt,yt)
        except IndexError:
            pass

def incrementsquid(data, n):
    printSquid(data)
    for i in range(0, n):
        for x, line in enumerate(data):
            for y, squid in enumerate(line):
                if squid >= 9:
                    data[x][y] = 0
                    too_brigth(data,x,y)
                else:
                    data[x][y] += 1
        printSquid(data)
    return

def main():
    data = [[int(n) for n in line.strip()] for line in open("input.sql").readlines()]
    incrementsquid(data, 10)
    return

if __name__ == '__main__':
    main()