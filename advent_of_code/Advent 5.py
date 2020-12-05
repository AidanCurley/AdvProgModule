f = open("input5.txt", "r")
tickets = f.read().split('\n')


def binary_to_decimal(n):
    return int(n, 2)


def convert_to_binary(string, ch):
    result = ""
    for x in string:
        result += "1" if x == ch else "0"
    return result


ticket_ids = []
for ticket in tickets:
    if len(ticket) == 10:
        row = binary_to_decimal(convert_to_binary(ticket[:7], 'B'))
        seat = binary_to_decimal(convert_to_binary(ticket[7:], 'R'))
        ticket_ids.append(row *8 + seat)

print(f'Task1: {max(ticket_ids)}')

for i in range(min(ticket_ids), max(ticket_ids)):
    if i not in ticket_ids:
        print(f'Task2: {i}')
