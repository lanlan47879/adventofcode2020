import sys

REQ_SUM = 2020


def get_entries(input_file):
    with open(input_file, 'r') as f:
        entries = f.readlines()

    entries = [int(entry) for entry in entries]
    return entries


def find_two_nums(entries):
    for i in entries:
        for j in entries:
            sum = i + j
            if(sum == REQ_SUM):
                return i, j

    return -1, -1


def two_nums(entries):
    x, y = find_two_nums(entries)
    if(x == -1 and y == -1):
        print("no numbers in the expense report add up to 2020")
        exit()

    mult = get_mult(x, y, 1)
    print("{} + {} add up to 2020".format(x, y))
    print("{} * {} multiply to {}".format(x, y, mult))


def find_three_nums(entries):
    for i in entries:
        for j in entries:
            for k in entries:
                sum = i + j + k
                if(sum == REQ_SUM):
                    return i, j, k

    return -1, -1, -1


def three_nums(entries):
    x, y, z = find_three_nums(entries)
    if(x == -1 and y == -1 and z == -1):
        print("no numbers in the expense report add up to 2020")
        exit()

    mult = get_mult(x, y, z)
    print("{} + {} + {} add up to 2020".format(x, y, z))
    print("{} * {} * {} multiply to {}".format(x, y, z, mult))


def get_mult(x, y, z):
    return x * y * z


def main():
    if(len(sys.argv) != 3):
        print("usage: python3 day01.py expense_report numbers_to_find")
        exit(-1)

    entries = get_entries(sys.argv[1])

    if(int(sys.argv[2]) != 2 and int(sys.argv[2]) != 3):
        print("can only find two or three numbers whose sum add up to 2020")
        exit(-1)
    elif(int(sys.argv[2]) == 2):
        two_nums(entries)
    elif(int(sys.argv[2]) == 3):
        three_nums(entries)


if __name__ == "__main__":
    main()
