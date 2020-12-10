from collections import defaultdict

f = open("input10.txt", "r")
joltages = f.read().split("\n")
joltages = list(map(int, joltages[:-1]))

# sort, add first 0, and final destination
joltages.sort()
joltages.append(joltages[-1] + 3)
joltages.insert(0, 0)

# make a list of all differences
diffs = []
for i in range(len(joltages) - 1):
    diffs.append(joltages[i + 1] - joltages[i])

print(f'Task1: {(diffs.count(1)) * (diffs.count(3))}')

# if the path doesn't exist, enter 0
paths = defaultdict(lambda: 0)
paths[0] = 1

# the path to each one is the sum of the previous 3 paths
for i in range(1, len(joltages)):
    paths[joltages[i]] = paths[joltages[i] - 1] + paths[joltages[i] - 2] + paths[joltages[i] - 3]

print(f'Task1: {paths[joltages[-1]]}')


## This solution works for all test data but takes too long to complete using the full input file
## There are just too many paths to count efficiently

# from networkx import *
# from networkx.algorithms.simple_paths import all_simple_paths
#
# g = DiGraph()
#
# for i in range(len(joltages)-1):
#     source_node = joltages[i]
#     for j in range(1,4):
#         if i+j < len(joltages):
#             if joltages[i+j] - joltages[i] <= 3:
#                 dest_node = joltages[i+j]
#                 g.add_edge(source_node, dest_node)
#
# print(f'Result: {len(list(all_simple_paths(g, joltages[0], joltages[-1])))}')