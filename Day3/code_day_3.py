def power_comsumption(data, N):
    bits = [2 ** n for n in range(N)]
    gamma = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit >= len(data) / 2)
    epsilon = sum(bit for bit in bits if sum(datum & bit for datum in data) // bit <= len(data) / 2)
    print("Part 1 = {}".format(epsilon * gamma))


def filter_data_bitwise(data, N,filter_by_most_common=True):
    filtered = [x for x in data]
    bits = [2 ** n for n in range(N)]
    for bit in reversed(bits):
        ratio = sum(1 for num in filtered if num & bit) / len(filtered)
        wanted_bit_value = bit * int((ratio >= 0.5) == filter_by_most_common)
        filtered = [x for x in filtered if x & bit == wanted_bit_value]
        if len(filtered) == 1:
            break
    return filtered

def life_support(data, N):
    oxygen = filter_data_bitwise(data, N)
    co2 = filter_data_bitwise(data,N ,filter_by_most_common=False)
    print("Part 2 = {}".format(oxygen[0] * co2[0]))

def main():
    with open("input.sql", "r") as f:
        lines = f.readlines()
    N = len(lines[0].strip())
    data = [int(line, base=2) for line in lines]
    power_comsumption(data, N)
    life_support(data, N)

if __name__ == '__main__':
    main()