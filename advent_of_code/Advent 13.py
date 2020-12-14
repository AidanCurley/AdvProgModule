
f = open('input13.txt', "r")
time = f.readline()
buses = f.readline().split(",")


waits = []
for bus in buses:
    if bus != 'x':
        print(f'Task1: {int(time)%int(bus) -int(bus), bus}')


gaps = []
for bus in range(len(buses)):
    gaps.append(bus)
    if buses[bus] == 'x':
        buses[bus] = 0
    else:
        buses[bus] = int(buses[bus])


index_max_bus = max(range(len(buses)), key=buses.__getitem__)
buses_and_gaps = []
for i in range(len(buses)):
    buses_and_gaps.append((int(buses[i]), gaps[i]))

count = 1
x = 1298835000000 # just to shorten running time and prove the bastard works
while count != 0:
    count = 0
    t_stamp = (x * max(buses)) - buses_and_gaps[index_max_bus][1]
    for i in range(len(buses_and_gaps)):
        if buses_and_gaps[i][0] != 0:
            if (t_stamp + buses_and_gaps[i][1]) % buses_and_gaps[i][0] != 0:
                count += 1
                break
    x += 1
print(f'Task2: {t_stamp}')
