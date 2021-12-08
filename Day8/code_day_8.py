def part2(line):
    input = line[:10]
    decode_number = [None] * 10
    #easy part
    for i, wanted in zip([1,4,7,8], [2,4,3,7]):
        decode_number[i] = ["".join(sorted(w)) for w in input if len(w) == wanted][0]

    #kind of want to die
    decode_number[3] = ["".join(sorted(w)) for w in input if len(w) == 5 and len(set(decode_number[7]) & set(w)) == 3][0]
    decode_number[9] = ["".join(sorted(w)) for w in input if len(w) == 6 and set(decode_number[3]) < set(w)][0]
    decode_number[5] = ["".join(sorted(w)) for w in input if len(w) == 5 and set(w) != set(decode_number[3]) and set(w) < set(decode_number[9])][0]
    decode_number[2] = ["".join(sorted(w)) for w in input if len(w) == 5 and set(w) != set(decode_number[3]) and set(w) != set(decode_number[5])][0]
    decode_number[6] = ["".join(sorted(w)) for w in input if len(w) == 6 and set(w) != set(decode_number[9]) and set(decode_number[5]) < set(w)][0]
    decode_number[0] = ["".join(sorted(w)) for w in input if len(w) == 6 and set(w) != set(decode_number[6]) and set(w) != set(decode_number[9])][0]

    #I like this
    return int("".join(str(decode_number.index("".join(sorted(w)))) for w in line[-4:]))

def main():
    input = [[n for n in line.replace(' | ', ' ').strip().split(' ')] for line in open('input.sql','r').readlines()]
    print("Part1 = {}".format(sum(len([n for n in line.split('|')[1].strip().split(' ') if len(n) == 2 or len(n) == 3 or len(n) == 4 or len(n) == 7]) for line in open('input.sql','r').readlines())))
    print("Part2 = {}".format(sum(part2(line) for line in input)))
    return

if __name__ == '__main__':
    main()