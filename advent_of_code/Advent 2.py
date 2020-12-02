import re
from operator import itemgetter

f = open("input2.txt", "r")
lines = f.readlines()
counter = 0
counter2 = 0

for line in lines:
    split_line = re.split('[-:\\s]', line)
    num1, num2, search_char, password = itemgetter(0, 1, 2, 4)(split_line)
    # task 1
    if int(num1) <= password.count(search_char) <= int(num2):
        counter += 1
    # task 2
    if not password[int(num1) - 1] == search_char == password[int(num2) - 1]:
        if search_char == password[int(num1) - 1] or search_char == password[int(num2) - 1]:
            counter2 += 1

print(f'Task 1: {counter}')
print(f'Task 2: {counter2}')
