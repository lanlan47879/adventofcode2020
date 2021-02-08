import sys
import re


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


def is_valid(entry):
    has_byr = 'byr' in entry
    has_iyr = 'iyr' in entry
    has_eyr = 'eyr' in entry
    has_hgt = 'hgt' in entry
    has_hcl = 'hcl' in entry
    has_ecl = 'ecl' in entry
    has_pid = 'pid' in entry
    has_all = has_byr & has_iyr & has_eyr & has_hgt & has_hcl & has_ecl & has_pid

    return has_all


def rm_invalid_entries(old_entries):
    new_entries = [entry for entry in old_entries if is_valid(entry)]

    return new_entries


def check_byr(byr_str):
    byr_str = re.search('.*([0-9]{4}).*', byr_str)
    byr = int(byr_str.group(1))

    if byr >= 1920 and byr <= 2002:
        return True


def check_iyr(iyr_str):
    iyr_str = re.search('.*([0-9]{4}).*', iyr_str)
    iyr = int(iyr_str.group(1))

    if iyr >= 2010 and iyr <= 2020:
        return True


def check_eyr(eyr_str):
    eyr_str = re.search('.*([0-9]{4}).*', eyr_str)
    eyr = int(eyr_str.group(1))

    if eyr >= 2020 and eyr <= 2030:
        return True


def check_hgt(hgt_str):
    if 'cm' in hgt_str:
        cm_str = re.search('.*([0-9]{3}).*', hgt_str)

        if cm_str:
            cm = int(cm_str.group(1))

            if cm >= 150 and cm <= 193:
                return True

    if 'in' in hgt_str:
        inc_str = re.search('.*([0-9]{2}).*', hgt_str)

        if inc_str:
            inc = int(inc_str.group(1))

            if inc >= 59 and inc <= 76:
                return True


def check_hcl(hcl_str):
    valid = re.search('(\#)([0-9a-f]{6})$', hcl_str)

    if valid:
        return True


def check_ecl(ecl_str):
    if 'amb' in ecl_str or 'blu' in ecl_str or 'brn' in ecl_str or 'gry' in ecl_str or 'grn' in ecl_str or 'hzl' in ecl_str or 'oth' in ecl_str:
        return True


def check_pid(pid_str):
    valid = re.search('[^\[0-9\]*]([0-9]{9})$', pid_str)

    if valid:
        return True


def count_valid_entries(entries):
    entries = rm_invalid_entries(entries)

    valid_count = 0
    for entry in entries:
        split_entry = entry.split(' ')
        byr = iyr = eyr = hgt = hcl = ecl = pid = -1
        for entry_part in split_entry:
            if 'byr' in entry_part:
                byr = entry_part
            if 'iyr' in entry_part:
                iyr = entry_part
            if 'eyr' in entry_part:
                eyr = entry_part
            if 'hgt' in entry_part:
                hgt = entry_part
            if 'hcl' in entry_part:
                hcl = entry_part
            if 'ecl' in entry_part:
                ecl = entry_part
            if 'pid' in entry_part:
                pid = entry_part

        if check_byr(byr) and check_iyr(iyr) and check_eyr(eyr) and check_hgt(hgt) and check_hcl(hcl) and check_ecl(ecl) and check_pid(pid):
            valid_count += 1
    return valid_count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day04_part02.py passport_file")
        exit(-1)

    entries = get_entries(sys.argv[1])
    valid_count = count_valid_entries(entries)
    print("there are {} valid entries".format(valid_count))


if __name__ == "__main__":
    main()
