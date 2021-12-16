from collections import Counter

def polymerization(start, instructions, length):
    pairs = Counter(map(str.__add__, start, start[1:]))
    chars = Counter(start)

    for bite in range(length):
        for (a,b), c in pairs.copy().items():
            x = instructions[a+b]
            pairs[a+b] -= c
            pairs[a+x] += c
            pairs[x+b] += c
            chars[x] += c
    return max(chars.values())-min(chars.values())

def main():
    start, instruction = open("input.sql").read().split("\n\n")
    dict_instruction = { j.split(" -> ")[0] :j.split(" -> ")[1] for j in instruction.split('\n')}
    print("Part1 = {}".format(polymerization(start, dict_instruction, 10)))
    print("Part2 = {}".format(polymerization(start, dict_instruction, 40)))

if __name__ == '__main__':
    main()