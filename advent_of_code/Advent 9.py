import itertools

f = open("input9.txt", "r")
entries = f.read().split("\n")
entries = list(map(int, entries[:-1]))


def find_outlier(nums, combo_no, target):
    for combo in itertools.combinations(nums, combo_no):
        if sum(combo) == target:
            return False
    return True


# Task 1
for position in range(len(entries)):
    if find_outlier(entries[position:25 + position], 2, entries[25 + position]):
        task1 = entries[25 + position]
        print(f'Task1: {task1}')
        break
        
# Task 2
for i in range(len(entries)):
    total = entries[i]
    for j in range(i+1, len(entries)):
        total += entries[j]
        if total > task1:
            break
        elif total == task1:
            print(f'Task2: {min(entries[i:j + 1]) + max(entries[i:j + 1])}')