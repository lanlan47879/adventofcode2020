import sys


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [entry.strip() for entry in entries]
    return entries


def get_exec_order(entries):
    i = 0
    boot_len = len(entries)

    visited_entries = []
    exec_order = []
    while i < boot_len:
        exec_order.append(i)

        entry = entries[i]
        if 'jmp' in entry:
            value = int(entry.split(' ')[1])
            i += value
        else:
            i += 1

        visited_entry = (entry, i)
        if visited_entry in visited_entries:
            break

        visited_entry = (entry, i)
        visited_entries.append(visited_entry)

    return exec_order


def get_exec_instructions(entries, exec_order):
    return [(entries[i], i) for i in exec_order]


def get_acc(exec_instructions):
    acc = 0
    visited_instructions = []
    for instruction in exec_instructions:
        visited_instruction = instruction
        if visited_instruction in visited_instructions:
            break

        if 'acc' in instruction[0]:
            value = int(instruction[0].split(' ')[1])
            acc += value

        visited_instructions.append(visited_instruction)

    return acc


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day08_part01.py boot_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    exec_order = get_exec_order(entries)
    exec_instructions = get_exec_instructions(entries, exec_order)
    acc = get_acc(exec_instructions)

    print("acc is {}".format(acc))


if __name__ == "__main__":
    main()
