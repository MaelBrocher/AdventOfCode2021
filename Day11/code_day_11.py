from colorama import init
from colorama import Fore, Back, Style
import time
 
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

def countN(data):
    c10,c0=0,0
    for x in range(10):
        for y in range(10):
            if data[x][y]==10:
                c10+=1
            if data[x][y]==0:
                c0+=1
    return c10,c0

def processSquids(data, step):
    f=0
    neighbors = [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1] ]
    for s in range(step):
        for x in range(10):
            for y in range(10):
                data[x][y]+=1
        while countN(data)[0]>0:
            for x in range(10):
                for y in range(10):
                    if data[x][y]==10:
                        data[x][y]=0
                        f+=1
                        for dx,dy in neighbors:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<10 and 0<=ny<10:
                                if data[nx][ny]!=10 and data[nx][ny]!=0:
                                    data[nx][ny]+=1
        if countN(data)[1]==100:
            print(s)
            exit()
    return f

def SquidBlink(data):
    neighbors = [ [-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1] ]
    s = 0
    while countN(data)[1] !=100:
        for x in range(10):
            for y in range(10):
                data[x][y]+=1
        while countN(data)[0]>0:
            for x in range(10):
                for y in range(10):
                    if data[x][y]==10:
                        data[x][y]=0
                        for dx,dy in neighbors:
                            nx,ny=x+dx,y+dy
                            if 0<=nx<10 and 0<=ny<10:
                                if data[nx][ny]!=10 and data[nx][ny]!=0:
                                    data[nx][ny]+=1
        s+=1
        if countN(data)[1]==100:
            return s

def main():
    print("Part 1 = {}".format(processSquids([[int(n) for n in line.strip()] for line in open("input.sql").readlines()], 100)))
    print("Part 2 = {}".format(SquidBlink([[int(n) for n in line.strip()] for line in open("input.sql").readlines()])))
    return

if __name__ == '__main__':
    main()