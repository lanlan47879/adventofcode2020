import sys

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
TRANS = {FLOOR: 0, EMPTY: 1, OCCUPIED: 2}


def get_seat_layout(input_file):
    entries = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            entries.append(line.strip('\n'))

    seat_layout = [[None]*len(entries[0]) for i in range(len(entries))]
    for i in range(len(entries)):
        for j in range(len(entries[0])):
            seat = entries[i][j]
            seat_layout[i][j] = TRANS[seat]

    return seat_layout


def is_valid_coord(coord, height, width):
    return (-1 not in coord) and (coord[0] < height) and (coord[1] < width)


def get_neighbors(seat_layout, i, j):
    neighbors = []
    height, width = len(seat_layout), len(seat_layout[0])

    up, down = [i - 1, j], [i + 1, j]
    left, right = [i, j - 1], [i, j + 1]
    up_left, up_right = [i - 1, j - 1], [i - 1, j + 1]
    down_left, down_right = [i + 1, j - 1], [i + 1, j + 1]

    if is_valid_coord(up, height, width):
        neighbors.append(up)

    if is_valid_coord(down, height, width):
        neighbors.append(down)

    if is_valid_coord(left, height, width):
        neighbors.append(left)

    if is_valid_coord(right, height, width):
        neighbors.append(right)

    if is_valid_coord(up_left, height, width):
        neighbors.append(up_left)

    if is_valid_coord(up_right, height, width):
        neighbors.append(up_right)

    if is_valid_coord(down_left, height, width):
        neighbors.append(down_left)

    if is_valid_coord(down_right, height, width):
        neighbors.append(down_right)

    return neighbors


def are_neighbors_empty(seat_layout, neighbors):
    return not any(seat_layout[neighbor[0]][neighbor[1]] ==
                   TRANS[OCCUPIED] for neighbor in neighbors)


def are_four_adjacent_occupied(seat_layout, neighbors):
    count = sum(seat_layout[neighbor[0]][neighbor[1]] ==
                TRANS[OCCUPIED] for neighbor in neighbors)

    return count >= 4


def occupy_seats(seat_layout):
    new_seat_layout = [[None]*len(seat_layout[0])
                       for i in range(len(seat_layout))]

    for i in range(len(new_seat_layout)):
        for j in range(len(new_seat_layout[0])):
            curr_spot = seat_layout[i][j]
            neighbors = get_neighbors(seat_layout, i, j)

            if curr_spot == TRANS[EMPTY]:
                if are_neighbors_empty(seat_layout, neighbors):
                    new_seat_layout[i][j] = TRANS[OCCUPIED]
                else:
                    new_seat_layout[i][j] = TRANS[EMPTY]
            elif curr_spot == TRANS[OCCUPIED]:
                if are_four_adjacent_occupied(seat_layout, neighbors):
                    new_seat_layout[i][j] = TRANS[EMPTY]
                else:
                    new_seat_layout[i][j] = TRANS[OCCUPIED]
            else:
                new_seat_layout[i][j] = TRANS[FLOOR]
                continue

    return new_seat_layout


def print_seat_layout(seat_layout):
    keys = list(TRANS.keys())
    vals = list(TRANS.values())
    for row in seat_layout:
        for col in row:
            pos = vals.index(col)
            print(keys[pos], end='')
        print()


def get_occupied_seats(seat_layout):
    count = sum(col == TRANS[OCCUPIED] for row in seat_layout for col in row)

    return count


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day11_part01.py seat_layout_file")
        exit(-1)

    seat_layout = get_seat_layout(sys.argv[1])

    tracker = seat_layout
    seat_layout = occupy_seats(seat_layout)
    while seat_layout != tracker:
        print_seat_layout(seat_layout)
        print()

        tracker = seat_layout
        seat_layout = occupy_seats(seat_layout)

    occupied_seats = get_occupied_seats(seat_layout)
    print("there are {} occupied seats".format(occupied_seats))


if __name__ == "__main__":
    main()
