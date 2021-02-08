import sys


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [entry.strip() for entry in entries]
    return entries


def get_row(entry):
    row_chars = 7
    lower_bound, upper_bound = 0, 127
    for i in range(row_chars):
        section = int((upper_bound - lower_bound) / 2)
        if entry[i] == 'F':
            upper_bound = lower_bound + section

        if entry[i] == 'B':
            lower_bound = upper_bound - section

    row = lower_bound
    return row


def get_col(entry):
    col_chars = 3
    lower_bound, upper_bound = 0, 7
    for i in range(col_chars):
        section = int((upper_bound - lower_bound) / 2)
        if entry[i] == 'L':
            upper_bound = lower_bound + section

        if entry[i] == 'R':
            lower_bound = upper_bound - section

    col = lower_bound
    return col


def find_my_seat_id(seat_ids):
    seat_ids.sort()
    lower_bound, upper_bound = seat_ids[0], seat_ids[-1]

    for i in range(lower_bound, upper_bound + 1):
        if i not in seat_ids:
            return i


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day05.py boarding_pass_file")
        exit(-1)

    entries = get_entries(sys.argv[1])

    seat_ids = []
    for entry in entries:
        row = get_row(entry[:7])
        col = get_col(entry[-3:])

        seat_id = row * 8 + col
        seat_ids.append(seat_id)

        print("{}: row {:3}, column {:1}, seat ID {:3}".format(
            entry, row, col, seat_id))

    max_seat_id = max(seat_ids)
    print("\nthe maximum seat id is {}".format(max_seat_id))

    my_seat_id = find_my_seat_id(seat_ids)
    print("my seat id is {}".format(my_seat_id))


if __name__ == "__main__":
    main()
