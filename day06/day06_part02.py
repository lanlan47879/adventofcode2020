import sys
import string


def get_entries(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        f.seek(0)

        entry = ""
        entries = []
        for line in f:
            entry = entry + " " + line.strip('\n')
            if line == '\n' or line == last_line:
                entries.append(entry)
                entry = ""
                continue

    return entries


def rm_whitespace_from_entry(split_entry):
    return [entry_part for entry_part in split_entry if entry_part != '']


def get_split_entries(entries):
    split_entries = []
    for entry in entries:
        split_entry = entry.split(' ')
        clean_split_entry = rm_whitespace_from_entry(split_entry)
        split_entries.append(clean_split_entry)

    return split_entries


def get_yes_count(split_entries):
    count = 0
    alphabet = list(string.ascii_lowercase)
    for split_entry in split_entries:
        alphabet_counts = [0] * 26
        entry_count = len(split_entry)

        for entry in split_entry:
            for letter in alphabet:
                if letter in entry:
                    alphabet_counts[alphabet.index(letter)] += 1

        for alphabet_count in alphabet_counts:
            if alphabet_count == entry_count:
                count += 1

    return count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day06_part02.py question_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    split_entries = get_split_entries(entries)
    yes_count = get_yes_count(split_entries)

    print("total answered questions is {}".format(yes_count))


if __name__ == "__main__":
    main()
