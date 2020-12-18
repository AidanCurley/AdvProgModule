import numpy as np

f = open("input17.txt", "r")
input = f.read().split("\n")[:-1]
# change to boolean
result = [[y == '#' for y in x] for x in input]

pocket = np.zeros((60, 60, 60,60), dtype=np.int8)
active = True
for y in range(8):
    for x in range(8):
        pocket[26+x,26+y,30,30] = result[y][x]


def count_active_neighbours(x,y,z,w):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for m in range(-1, 2):
                #print(f'{x+i,y+j,z+k,pocket[x+i][y+j][z+k]}')
                    count += 1 if pocket[x+i][y+j][z+k][w+m] == 1 else 0
    count -= pocket[x][y][z][w]
    return count

cycle = 1
while cycle <= 6:
    new_pocket = np.zeros((60, 60, 60, 60), dtype=np.int8)
    for x in range(20,40):
        for y in range(20,40):
            for z in range(20,40):
                for w in range(20,40):
                    if pocket[x][y][z][w] == 1:
                        neighbours = count_active_neighbours(x,y,z,w)
                        if neighbours == 2 or neighbours == 3:
                            new_pocket[x][y][z][w] = 1
                        else:
                            new_pocket[x][y][z][w] = 0
                    else:
                        new_pocket[x][y][z][w] = 1 if count_active_neighbours(x, y, z, w) == 3 else 0
        print(cycle,x)

    pocket = np.copy(new_pocket)
    cycle += 1

print(f'Task2: {np.count_nonzero(pocket)}')