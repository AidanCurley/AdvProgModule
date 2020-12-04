from functools import reduce

# read in file, cut new line
f = open("input3.txt", "r")
full_map = [line.replace('\n', '') for line in f.readlines()]


def count_trees(this_map, inc_x, inc_y):
    x, trees = 0, 0
    for row in range(0, len(this_map), inc_y):
        if this_map[row][x % len(this_map[row])] == '#':
            trees += 1
        x = x + inc_x
    return trees


print(f'Task1: {count_trees(full_map, 3, 1)}')
num_trees = [count_trees(full_map, x, y) for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(f'Task2: {reduce(lambda x, y: x * y, num_trees)}')
