import sys


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


def count_valid_entries(entries):
    valid_count = 0
    for entry in entries:
        has_byr = 'byr' in entry
        has_iyr = 'iyr' in entry
        has_eyr = 'eyr' in entry
        has_hgt = 'hgt' in entry
        has_hcl = 'hcl' in entry
        has_ecl = 'ecl' in entry
        has_pid = 'pid' in entry
        has_all = has_byr & has_iyr & has_eyr & has_hgt & has_hcl & has_ecl & has_pid

        if has_all:
            valid_count += 1

    return valid_count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day04_part01.py passport_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    valid_count = count_valid_entries(entries)
    print("there are {} valid entries".format(valid_count))


if __name__ == "__main__":
    main()
