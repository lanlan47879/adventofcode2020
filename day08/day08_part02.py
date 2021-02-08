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


def jmps_to_nops(entries):
    i = 0
    entries_with_jmps_to_nops = []
    for entry in entries:
        if 'jmp' in entry:
            value = entry.split(' ')[1]
            new_entry = 'nop ' + value

            new_entries = entries[:]
            new_entries[i] = new_entry

            entries_with_jmps_to_nops.append(new_entries)

        i += 1

    return entries_with_jmps_to_nops


def nops_to_jmps(entries):
    i = 0
    entries_with_nops_to_jmps = []
    for entry in entries:
        if 'nop' in entry:
            value = entry.split(' ')[1]
            new_entry = 'jmp ' + value

            new_entries = entries[:]
            new_entries[i] = new_entry

            entries_with_nops_to_jmps.append(new_entries)

        i += 1

    return entries_with_nops_to_jmps


def exec_order_has_loop(exec_order):
    return len(exec_order) != len(set(exec_order))


def find_solution(entries):
    solution = 0
    entries_with_jmps_to_nops = jmps_to_nops(entries)

    for entries in entries_with_jmps_to_nops:
        exec_order = get_exec_order(entries)
        if not exec_order_has_loop(exec_order):
            exec_instructions = get_exec_instructions(entries, exec_order)
            solution = get_acc(exec_instructions)

    if solution == 0:
        print("solution can't be found by chaning jmps to nops\nnow changing nops to jmps")

    entries_with_nops_to_jmps = nops_to_jmps(entries)
    for entries in entries_with_nops_to_jmps:
        exec_order = get_exec_order(entries)
        if not exec_order_has_loop(exec_order):
            exec_instructions = get_exec_instructions(entries, exec_order)
            solution = get_acc(exec_instructions)

    if solution == 0:
        print("solution can't be found")
        exit()

    return solution


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day08_part02.py boot_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    acc = find_solution(entries)
    print("acc is {}".format(acc))


if __name__ == "__main__":
    main()
