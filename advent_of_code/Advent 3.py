from functools import reduce

# read in file, cut new line and extend file 100 times to the right
f = open("input3.txt", "r")
lines = f.readlines()
full_map = [line.replace('\n', '')*100 for line in lines]


def count_trees(this_map, inc_right, inc_down):
    x, trees = 0, 0
    try:
        for row in range(0, len(this_map), inc_down):
            if this_map[row][x] == '#':
                trees += 1
            x = x + inc_right
    except IndexError:
        return trees
    return trees


print(f'Task1: {count_trees(full_map, 3, 1)}')
num_trees = [count_trees(full_map, x, y) for (x, y) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
print(f'Task2: {reduce(lambda x, y: x*y, num_trees)}')
