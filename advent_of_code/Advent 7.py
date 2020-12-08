from networkx import *
from networkx.algorithms.simple_paths import all_simple_paths
import re

f = open("input7.txt", "r")
file = f.read().split("\n")
lines = [line.split('contain') for line in file]
lines = lines[:-1]  # get rid of last blank line

g = DiGraph()

# add weighted edges
for line in lines:
    for entry in line[1].split(','):
        if "no other bags" not in entry:
            source_node = re.search(r'\w*\s\w*', line[0]).group(0)
            dest_node = re.search(r'(?<=\d\s)\w*\s\w*', entry).group(0)
            weight = re.search(r'(?<=\s)\d*', entry).group(0)
            g.add_edge(source_node, dest_node, weight=weight)

sources = []
# get all paths to shiny gold
for source in list(g.nodes):
    for path in all_simple_paths(g, source=source, target='shiny gold'):
        sources.append(path[0])

# remove duplicate sources and count
print(f'Task1: {len(set(sources))}')

# get all paths from shiny gold
res = []
for dest in list(g.nodes):
    for path in all_simple_paths(g, source='shiny gold', target=dest):
        res.append(path)

final_total = 0
# loop through each path from shiny gold
for path in res:
    total = 1
    # get product of the weights of the edges
    for node in range(len(path) - 1):
        total = total * int(g[path[node]][path[node + 1]]['weight'])
    # add to final total
    final_total += total

print(f'Task2: {final_total}')