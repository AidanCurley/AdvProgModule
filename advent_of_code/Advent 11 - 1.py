
def is_seat_occupied(floorplan,row,seat):
    return floorplan[row][seat] == '#'


def count_occupied_surrounding_seats(floorplan, row, seat):
    num_occupied = 0
    for i in range(row-1, row+2):
        for j in range(seat-1, seat+2):
            try:
                if (i,j) == (row,seat):  # skip current seat
                    continue
                else:
                    if j != -1:  # avoid using the last letter in the string [-1]
                        num_occupied += is_seat_occupied(floorplan, i,j)
            except IndexError:
                continue
    return num_occupied


def make_new_floorplan(floorplan):
    new_floorplan = floorplan.copy()    # make a copy so you can change it without affecting calculations
    for row in range(len(floorplan)):   # counter for rows
        for seat in range(len(floorplan[row])):     # counter for seat in row
            if floorplan[row][seat] != '.':
                occupied = is_seat_occupied(floorplan, row, seat)
                neighbours_occupied = count_occupied_surrounding_seats(floorplan, row, seat)
                if not occupied and neighbours_occupied == 0:
                    new_floorplan[row] = new_floorplan[row][:seat] + '#' + new_floorplan[row][seat + 1:]
                if occupied is True and neighbours_occupied >= 4:
                    new_floorplan[row] = new_floorplan[row][:seat] + 'L' + new_floorplan[row][seat + 1:]
    return new_floorplan


def main():
    f = open("input11.txt", "r")
    floorplan = f.read().split("\n")
    # loop until no changes are made
    while make_new_floorplan(floorplan) != floorplan:
        floorplan = make_new_floorplan(floorplan)

    print(f'Task1: {sum(line.count("#") for line in floorplan)}')


if __name__ == '__main__':
    main()



