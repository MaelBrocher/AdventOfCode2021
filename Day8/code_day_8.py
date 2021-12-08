def part2(line):
    input = line[:10]
    output = line[10:]
    decode_number = [None] * 10
    #easy but ugly part
    #https://imgur.com/a/LIS2zZr
    for i, wanted in zip([1,4,7,8], [2,4,3,7]):
        decode_number[i] = ["".join(sorted(w)) for w in input if len(w) == wanted][0]
    for l in input:
        if len(l) == 5:
            if len(''.join(set(decode_number[7]).intersection(l))) == len(decode_number[7]):
                decode_number[3] = "".join(sorted(l))
            elif len(''.join(set(decode_number[4]).intersection(l))) == 3:
                decode_number[5] = "".join(sorted(l))
            else:
                decode_number[2] = "".join(sorted(l))
        elif len(l) == 6:
            if len(''.join(set(decode_number[4]).intersection(l))) == len(decode_number[4]):
                decode_number[9] = "".join(sorted(l))
            elif len(''.join(set(decode_number[7]).intersection(l))) == len(decode_number[7]):
                decode_number[0] = "".join(sorted(l))
            else:
                decode_number[6] = "".join(sorted(l))
    #I like this
    return int("".join(str(decode_number.index("".join(sorted(w)))) for w in output))

def main():
    input = [[n for n in line.replace(' | ', ' ').strip().split(' ')] for line in open('input.sql','r').readlines()]
    print("Part1 = {}".format(sum(len([n for n in line.split('|')[1].strip().split(' ') if len(n) == 2 or len(n) == 3 or len(n) == 4 or len(n) == 7]) for line in open('input.sql','r').readlines())))
    print("Part2 = {}".format(sum(part2(line) for line in input)))
    return

if __name__ == '__main__':
    main()