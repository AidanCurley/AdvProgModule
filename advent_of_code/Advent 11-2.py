
def is_seat_occupied(floorplan,row,seat):
    if len(floorplan)-1 >= row >= 0 and len(floorplan[row])-1 >= seat >= 0:
        if floorplan[row][seat] == '#':
            return True
        elif floorplan[row][seat] == 'L':
            return False
        else:
            return None
    return False


def is_occupied_in_line(floorplan, row, seat, direction):
    while len(floorplan)-1 >= row >= 0 and 0 <= seat <= len(floorplan[row])-1:
        row += direction[0]
        seat += direction[1]
        if is_seat_occupied(floorplan, row, seat) is not None:   # skip over floor area
            return is_seat_occupied(floorplan, row, seat)
    return False


def count_occupied_seats_in_all_directions(floorplan, row, seat, dirs):
    num_occupied = 0
    for direction in dirs:
        num_occupied += is_occupied_in_line(floorplan, row, seat, direction)  # check for each direction
    return num_occupied


def task2(floorplan):
    new_floorplan = floorplan.copy()
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(floorplan)):
        for seat in range(len(floorplan[row])):
            if floorplan[row][seat] != '.':
                occupied = is_seat_occupied(floorplan, row, seat)
                neighbours_occupied = count_occupied_seats_in_all_directions(floorplan, row, seat, dirs)
                if not occupied and neighbours_occupied == 0:
                    new_floorplan[row] = new_floorplan[row][:seat] + '#' + new_floorplan[row][seat + 1:]
                if occupied and neighbours_occupied >= 5:
                    new_floorplan[row] = new_floorplan[row][:seat] + 'L' + new_floorplan[row][seat + 1:]
    return new_floorplan


def main():
    f = open("input11.txt", "r")
    floorplan = f.read().split("\n")[:-1]
    while task2(floorplan) != floorplan:
        floorplan = task2(floorplan)
    print(f'Task1: {sum(line.count("#") for line in floorplan)}')


if __name__ == "__main__":
    main()