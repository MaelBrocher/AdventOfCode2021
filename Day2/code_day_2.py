def submarine(data, aiming=False):
    values = [0,0,0]
    for d in data:
        position, depth, aim = values
        shift = int(d[1])
        match d[0]:
            case "up":
                values = [position, depth, aim - shift] if aiming else [position, depth - shift, aim]
            case "down":
                values = [position, depth, aim + shift] if aiming else [position, depth + shift, aim]
            case "forward" :
                values = [position + shift, depth + (aim * shift), aim] if aiming else [position + shift, depth, aim]
            case _ :
                print(d[0])
    return (values[0] * values[1])

def main():
    f = open("input.txt", "r")
    data = [(line.split(' ')[0],line.split(' ')[1].replace('\n', ''))  for line in f.readlines()]

    print("Part 1 = {}".format(submarine(data)))
    print("Part 2 = {}".format(submarine(data, aiming=True)))

if __name__ == '__main__':
    main()