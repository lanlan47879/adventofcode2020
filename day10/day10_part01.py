import sys


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [int(entry.strip()) for entry in entries]
    return entries


def get_available_adapters(entries, valid_adapters):
    available_adapters = []
    for entry in entries:
        for valid_adapter in valid_adapters:
            if entry == valid_adapter:
                available_adapters.append(valid_adapter)

    return available_adapters


def get_differences(entries):
    entries.insert(0, 0)
    max_joltage = max(entries) + 3
    entries.insert(len(entries), max_joltage)

    one_joltage_diffs = 0
    three_joltage_diffs = 0
    for entry in entries:
        valid_adapters = [entry + 1, entry + 2, entry + 3]
        available_adapters = get_available_adapters(entries, valid_adapters)

        if not available_adapters:
            continue

        next_adapter = available_adapters[0]
        diff = next_adapter - entry
        if diff == 1:
            one_joltage_diffs += 1
        elif diff == 3:
            three_joltage_diffs += 1

    return one_joltage_diffs, three_joltage_diffs


def get_mult(one_joltage_diffs, three_joltage_diffs):
    return one_joltage_diffs * three_joltage_diffs


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day10_part01.py joltage_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    entries.sort()
    one_joltage_diffs, three_joltage_diffs = get_differences(entries)

    print("there are {} differences of 1 jolt and {} differences of 3 jolts".format(
        one_joltage_diffs, three_joltage_diffs))
    print("the product of these is {}".format(
        get_mult(one_joltage_diffs, three_joltage_diffs)))


if __name__ == "__main__":
    main()
