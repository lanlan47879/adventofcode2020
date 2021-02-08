import sys


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [entry.strip() for entry in entries]
    return entries


def get_split_entries(entries):
    split_entries = []
    for entry in entries:
        count, char, pw = entry.split(" ")
        min_count = int(count.split("-")[0])
        max_count = int(count.split("-")[1])

        d = {"min count": min_count, "max count": max_count,
             "char": char[0], "password": pw}
        split_entries.append(d)

    return split_entries


def count_valid_passwords(split_entries):
    valid_count = 0
    for entry in split_entries:
        min_count = entry["min count"]
        max_count = entry["max count"]
        char = entry["char"]
        pw = entry["password"]

        first_inst = pw[min_count - 1] == char
        second_inst = pw[max_count - 1] == char
        if(first_inst ^ second_inst):
            valid_count = valid_count + 1

    return valid_count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day02_part02.py password_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    split_entries = get_split_entries(entries)
    valid_count = count_valid_passwords(split_entries)
    print("there are {} valid passwords".format(valid_count))


if __name__ == "__main__":
    main()
