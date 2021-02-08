import sys
import math


def get_entries(input_file):
    with open(input_file, 'r') as f:
        start_departure = int(f.readline().strip())
        bus_ids = f.readline().split(',')

    return start_departure, [int(bus_id) for bus_id in bus_ids if bus_id != 'x']


def get_next_departures(start_departure, bus_ids):
    next_departures = [None] * len(bus_ids)

    curr_departure, found_departures = start_departure, []
    while not all(next_departures):
        tmp_departures = [curr_departure / bus_id for bus_id in bus_ids]

        if any(tmp_departure.is_integer() for tmp_departure in tmp_departures):
            i = 0
            for tmp_departure in tmp_departures:
                if tmp_departure.is_integer() and bus_ids[i] not in found_departures:
                    next_departures[i] = curr_departure
                    found_departures.append(bus_ids[i])
                i += 1

        curr_departure += 1

    return next_departures


def main():
    if(len(sys.argv) != 2):
        print("usage: python3 day13_part01.py bus_schedule_file")
        exit(-1)

    start_departure, bus_ids = get_entries(sys.argv[1])
    next_departures = get_next_departures(start_departure, bus_ids)

    next_departure = min(next_departures)
    next_bus = bus_ids[next_departures.index(next_departure)]
    wait_time = next_departure - start_departure

    print('the product is {}'.format(next_bus * wait_time))


if __name__ == "__main__":
    main()
