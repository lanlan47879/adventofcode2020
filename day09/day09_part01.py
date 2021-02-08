import sys


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [int(entry.strip()) for entry in entries]
    return entries


def is_valid_sum(num, preamble):
    for i in preamble:
        for j in preamble:
            sum = i + j
            if sum == num and i != j:
                return True


def get_invalid_num(entries, length):
    j = length
    for i in range(len(entries)):
        next_num = entries[j]
        preamble = get_preamble(entries, i, j)

        if not is_valid_sum(next_num, preamble):
            return next_num

        if j + 1 < len(entries):
            j += 1


def get_preamble(entries, start, end):
    return entries[start:end]


def main():
    if(len(sys.argv) != 3):
        print("usage: python3 day09_part01.py preamble_file PREAMBLE")
        exit(-1)

    entries = get_entries(sys.argv[1])
    invalid_num = get_invalid_num(entries, int(sys.argv[2]))

    print("the first invalid number is {}".format(invalid_num))


if __name__ == "__main__":
    main()
