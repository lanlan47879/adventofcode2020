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

def get_yes_count(entries):
    count = 0
    alphabet = list(string.ascii_lowercase)

    for letter in alphabet:
        for entry in entries:
            if letter in entry:
                count += 1

    return count

def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day06_part01.py question_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    yes_count = get_yes_count(entries)

    print("total answered questions is {}".format(yes_count))

if __name__ == "__main__":
    main()
