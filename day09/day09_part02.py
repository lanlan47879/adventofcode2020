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


def get_contiguous_set(entries, invalid_num):
    start_num = 0
    sum = 0
    contiguous_set = []
    for i in range(len(entries)):
        for j in range(start_num, len(entries)):
            entry = entries[j]
            contiguous_set.append(entry)
            sum += entry

            if sum == invalid_num and len(contiguous_set) >= 2:
                return contiguous_set

            if sum > invalid_num:
                sum = 0
                contiguous_set = []

        start_num += 1

    print(contiguous_set)
    return contiguous_set


def get_enc_weakness(contiguous_set):
    return min(contiguous_set) + max(contiguous_set)


def main():
    if(len(sys.argv) != 3):
        print("usage: python3 day09_part02.py preamble_file PREAMBLE")
        exit(-1)

    entries = get_entries(sys.argv[1])
    invalid_num = get_invalid_num(entries, int(sys.argv[2]))
    contiguous_set = get_contiguous_set(entries, invalid_num)
    enc_weakness = get_enc_weakness(contiguous_set)

    print("the encryption weakness is {}".format(enc_weakness))


if __name__ == "__main__":
    main()
