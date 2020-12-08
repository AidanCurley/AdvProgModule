f = open("input8.txt", "r")
file = f.read().split("\n")
file = file[:-1]  # get rid of annoying last line


# run file and return accumulator and boolean end_of_file_reached
def run_file(f):
    accumulator, i = 0, 0
    visited = []  # stores indexes already visited
    while True:
        if i in visited or i == len(f): # break if revisiting index or reach end of file
            end_of_file_reached = i == len(f)
            break
        else:
            visited.append(i)
        if 'acc' in f[i]:
            accumulator += int(f[i].strip('acc '))
            i += 1
        elif 'jmp' in f[i]:
            i += int(f[i].strip('jmp '))
        else:
            i += 1
    return accumulator, end_of_file_reached

print(f'Task1: {run_file(file)}')

# loop through instructions - substitute 'nop' for 'jmp'
# or vice versa, save to temp_file and run
for instruction in range(len(file)):
    temp_file = file.copy()
    if 'jmp' in temp_file[instruction]:
        temp_file[instruction] = temp_file[instruction].replace('jmp', 'nop')
    elif 'nop' in temp_file[instruction]:
        temp_file[instruction] = temp_file[instruction].replace('nop', 'jmp')
    if True in run_file(temp_file):
        print(f'Task2: {run_file(temp_file)} ---- instruction changed: {file[instruction]}')

        break

