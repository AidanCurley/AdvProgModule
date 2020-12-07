from networkx import *
from networkx.algorithms.simple_paths import all_simple_paths
import re

f = open("input7.txt", "r")
file = f.read().split("\n")
lines = [line.split('contain') for line in file]

# # need 595 vertices
g = DiGraph()
g.add_node(line[0].strip(" bags") for line in lines)
lines = lines[:-1] # get rid of last blank line
for line in lines:
    for entry in line[1].split(','):
        # add weighted edges
        if "no other bags" not in entry:
            source_node = re.search(r'\w*\s\w*', line[0]).group(0)
            node = re.search(r'(?<=\d\s)\w*\s\w*', entry).group(0)
            weight = re.search(r'(?<=\s)\d*', entry).group(0)
            g.add_edge(source_node, node, weight=weight)

# get all paths to shiny gold
sources = []
source_nodes = [node for node in g.nodes]
for source in source_nodes:
    for path in all_simple_paths(g, source=source, target='shiny gold'):
        sources.append(path[0])

print(f'Task1: {len(set(sources))}')

# get all paths from shiny gold
res = []
dest_nodes = [node for node in g.nodes]
for dest in dest_nodes:
    for path in all_simple_paths(g, source='shiny gold', target=dest):
        res.append(path)


final_total = 0
# loop through each path from shiny gold
for path in res:
    total = 1
    # multiply the weights of the edges
    for node in range(len(path) - 1):
        total = total * int(g[path[node]][path[node + 1]]['weight'])
    # add to final total
    final_total += total

print(f'Task2: {final_total}')