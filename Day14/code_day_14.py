from collections import Counter

def polymerization(start, instructions, length):
    for i in range(length) :
        j = 0
        try :
            while start[j] != len(start):
                if len(start[j:j+2]) == 2:
                    start = start[:j+1] + instructions[start[j:j+2]] + start[j+1:]
                j+=2
        except IndexError:
            pass
    print(Counter(start).most_common()[0][1]-Counter(start).most_common()[-1][1])

def main():
    start, instruction = open("input.sql").read().split("\n\n")
    dict_instruction = { j.split(" -> ")[0] :j.split(" -> ")[1] for j in instruction.split('\n')}
    polymerization(start, dict_instruction, 10)
    polymerization(start, dict_instruction, 40)
    return

if __name__ == '__main__':
    main()