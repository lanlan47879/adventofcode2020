import sys
import numpy

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

    return numpy.array(seat_layout)


def is_valid_coord(coord, height, width):
    return not any(n < 0 for n in coord) and (coord[0] < height) and (coord[1] < width)


def is_not_floor(seat_layout, coord):
    return seat_layout[coord[0]][coord[1]] == TRANS[EMPTY] or seat_layout[coord[0]][coord[1]] == TRANS[OCCUPIED]


def get_neighbors(seat_layout, i, j):
    height, width = len(seat_layout), len(seat_layout[0])

    left = []
    for k, seat in enumerate(seat_layout[i, 0:j]):
        coord = [i, j - k - 1]
        if not is_valid_coord(coord, height, width):
            continue
        left.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    right = []
    for k, seat in enumerate(seat_layout[i, j + 1:]):
        coord = [i, j + k + 1]
        if not is_valid_coord(coord, height, width):
            continue
        right.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    down = []
    for k, seat in enumerate(seat_layout[i + 1:, j]):
        coord = [i + k + 1, j]
        if not is_valid_coord(coord, height, width):
            continue
        down.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    up = []
    for k, seat in enumerate(seat_layout[0:i, j]):
        coord = [i - k - 1, j]
        if not is_valid_coord(coord, height, width):
            continue
        up.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    down_left = []
    for k in range(1, height):
        coord = [i + k, j - k]
        if not is_valid_coord(coord, height, width):
            continue
        down_left.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    down_right = []
    for k in range(1, height):
        coord = [i + k, j + k]
        if not is_valid_coord(coord, height, width):
            continue
        down_right.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    up_left = []
    for k in range(1, height):
        coord = [i - k, j - k]
        if not is_valid_coord(coord, height, width):
            continue
        up_left.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    up_right = []
    for k in range(1, height):
        coord = [i - k, j + k]
        if not is_valid_coord(coord, height, width):
            continue
        up_right.append(coord)
        if is_not_floor(seat_layout, coord):
            break

    neighbors = []
    neighbors = left + right + down + up + \
        down_left + down_right + up_left + up_right

    return neighbors


def are_neighbors_empty(seat_layout, neighbors, test, i, j):
    return not any(seat_layout[neighbor[0]][neighbor[1]] ==
                   TRANS[OCCUPIED] for neighbor in neighbors)


def are_five_adjacent_occupied(seat_layout, neighbors):
    count = sum(seat_layout[neighbor[0]][neighbor[1]] ==
                TRANS[OCCUPIED] for neighbor in neighbors)

    return count >= 5


def occupy_seats(seat_layout):
    new_seat_layout = [[None]*len(seat_layout[0])
                       for i in range(len(seat_layout))]

    for i in range(len(new_seat_layout)):
        for j in range(len(new_seat_layout[0])):
            curr_spot = seat_layout[i][j]
            neighbors = get_neighbors(seat_layout, i, j)

            if curr_spot == TRANS[EMPTY]:
                if are_neighbors_empty(seat_layout, neighbors, neighbors, i, j):
                    new_seat_layout[i][j] = TRANS[OCCUPIED]
                else:
                    new_seat_layout[i][j] = TRANS[EMPTY]
            elif curr_spot == TRANS[OCCUPIED]:
                if are_five_adjacent_occupied(seat_layout, neighbors):
                    new_seat_layout[i][j] = TRANS[EMPTY]
                else:
                    new_seat_layout[i][j] = TRANS[OCCUPIED]
            else:
                new_seat_layout[i][j] = curr_spot
                continue

    return numpy.array(new_seat_layout)


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
        print("usage: python3 day11_part02.py seat_layout_file")
        exit(-1)

    seat_layout = get_seat_layout(sys.argv[1])

    count = 0
    tracker = seat_layout
    seat_layout = occupy_seats(seat_layout)
    while not numpy.array_equal(seat_layout, tracker):
        # print_seat_layout(seat_layout)
        # print()

        tracker = seat_layout
        seat_layout = occupy_seats(seat_layout)

        print("iteration {}".format(count))
        count += 1

    occupied_seats = get_occupied_seats(seat_layout)
    print("there are {} occupied seats".format(occupied_seats))


if __name__ == "__main__":
    main()
