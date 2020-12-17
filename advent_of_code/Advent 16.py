import re

f = open("input16.txt", "r")
file = f.read().split('\n')

#make dictionary of validations
valid_entries = {}
for i in range(0,20):
    field_name = re.search(r"^[^:]+", file[i]).group(0)
    a = int(re.search(r"\d*(?=-)", file[i]).group(0))
    b = int(re.search(r"(?<=-)\d*", file[i]).group(0))+1
    c = int(re.search(r"(?<=or\s)\d*(?=-)", file[i]).group(0))
    d = int(re.search(r"(?<=or\s\d\d\d-)\d*", file[i]).group(0))+1
    limits = list(range(a,b)) + list(range(c,d))
    valid_entries[field_name] = limits

#get my ticket details
my_ticket = file[22].split(',')

# loop through rest of file to get nearby tickets
nearby_tickets = []
for i in range(25,len(file)-1):
    nearby_tickets.append(file[i].split(','))

error_rate = 0
indexes_of_invalid_tickets = []
for index, ticket in enumerate(nearby_tickets):
    # check if each number in the ticket is in the list of valid entries
    for number in ticket:
        if any(int(number) in val for val in valid_entries.values()):
            continue
        else:
            error_rate += int(number)
            indexes_of_invalid_tickets.append(index)

print(f'Task1: {error_rate}')

# get list of valid tickets by ignoring those in the list of invalid indexes
valid_tickets =[]
for index, ticket in enumerate(nearby_tickets):
    if index not in indexes_of_invalid_tickets:
        valid_tickets.append(ticket)

# add my ticket to the list of valid tickets
valid_tickets.append(my_ticket)

# get list of entries for each field
fields = []
for i in range(len(valid_tickets[0])):
    fields.append([ticket[i] for ticket in valid_tickets])

# create dictionary of field_indexes with the possible field names for each one.
field_indexes_with_possible_names = {}
for i in range(len(fields)):
    field = set(list(map(int, fields[i])))
    possible = []
    for key, val in valid_entries.items():
        value = set(val)
        if field.issubset(value):
            possible.append(key)
    field_indexes_with_possible_names[i] = possible

# loop through dic of possible names
# if only one possible name for a field index,
# add the match to final indexes dictionary,
# and remove that name from all other dictionaries
final_indexes = {}
for i in range(20):
    for key, val in field_indexes_with_possible_names.items():
        if len(val) == 1:
            final_indexes[val[0]] = key
            item_to_remove = val[0]
            for keyx, valx in field_indexes_with_possible_names.items():
                try:
                    valx.remove(item_to_remove)
                except ValueError:
                    None

print(f'Task2: {int(my_ticket[final_indexes["departure date"]]) * int(my_ticket[final_indexes["departure time"]]) * int(my_ticket[final_indexes["departure track"]]) * int(my_ticket[final_indexes["departure location"]]) * int(my_ticket[final_indexes["departure station"]]) * int(my_ticket[final_indexes["departure platform"]])}')
