import re


def read_file(file):
    f = open(file, "r")
    return f.read().split("\n")[:-1]


journey = read_file("input12.txt")
directions = {1: 'N', 2: 'NE', 3: 'E', 4: 'SE', 5: 'S', 6: 'SW', 7: 'W', 8: 'NW'}
compass = {'N': [0, 1], 'NE': [1, 1], 'E': [1, 0], 'SE': [1, -1], 'S': [0, -1], 'SW': [-1, -1], 'W': [-1, 0],
           'NW': [-1, 1]}


def move(pos, direction, distance):
    for i in range(len(pos)):
        pos[i] += distance * direction[i]
    return pos


def move_waypoint(waypoint, direction, distance):
    for i in range(len(waypoint)):
        waypoint[i] += distance * direction[i]
    return waypoint


def rotate_waypoint(waypoint, degrees):
    times = int(degrees/90)
    if times > 0:
        for i in range(times):
            y = waypoint[0] * -1
            x = waypoint[1]
            waypoint = [x, y]
    else:
        for i in range(times):
            y = waypoint[0]
            x = waypoint[1] * -1
            waypoint = [x, y]
    return waypoint


def task1():
    current_position = [0, 0]
    current_direction = 3  ## East
    for entry in journey:
        if 'F' in entry:
            current_position = move(current_position, compass[directions[current_direction]], int(entry.lstrip('F')))
        elif 'R' in entry:
            current_direction = (current_direction + int(entry.lstrip('R'))/45) % 8
        elif 'L' in entry:
            current_direction = (current_direction - int(entry.lstrip('L')) / 45) % 8
        else:
            distance = int(re.search(r"\d+", entry).group(0))
            direction = re.search(r"\D+", entry).group(0)
            current_position = move(current_position, compass[direction], distance)
    print(f'Task1: {abs(current_position[0])+abs(current_position[1])}')


def task2():
    current_waypoint = [10, 1]
    current_position = [0, 0]
    for entry in journey:
        if 'F' in entry:
            current_position = move(current_position, current_waypoint, int(entry.lstrip('F')))
        elif 'R' in entry:
            current_waypoint = rotate_waypoint(current_waypoint, int(entry.lstrip('R')) % 360)
        elif 'L' in entry:
            current_waypoint = rotate_waypoint(current_waypoint, -int(entry.lstrip('L')) % 360)
        else:
            distance = int(re.search(r"\d+", entry).group(0))
            direction = re.search(r"\D+", entry).group(0)
            current_waypoint = move_waypoint(current_waypoint, compass[direction], distance)
    print(f'Task2: {abs(current_position[0])+abs(current_position[1])}')


task1()
task2()
