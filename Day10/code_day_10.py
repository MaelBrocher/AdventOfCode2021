from collections import Counter

def find_corrupt_char(line):
    stack = []
    corrupt = []
    close_to_open = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in line:
        if char in close_to_open.values():
            stack.append(char)
        elif not stack or stack.pop() != close_to_open[char]:
            corrupt.append(char)
            stack = None
            break
    return "".join(corrupt), stack

def part1(lines):
    var = "".join(find_corrupt_char(line)[0] for line in lines)
    return Counter(var)[">"] * 25137 + Counter(var)["}"] * 1197 + Counter(var)["]"] * 57 + Counter(var)[")"] * 3

def part2(lines):
    var = []
    pts = {'(': 1, '[': 2, '{': 3, '<': 4}
    for l in lines:
        stack = find_corrupt_char(l)[1]
        if stack:
            subtotal = 0
            for char in stack[::-1]:
                subtotal = 5 * subtotal + pts[char]
            var.append(subtotal)
    return sorted(var)[len(var)//2]

def main():
    angrylines = [l.strip() for l in open('input.sql')]
    print("Part 1 = {}".format(part1(angrylines)))
    print("Part 1 = {}".format(part2(angrylines)))
    return

if __name__ == '__main__':
    main()