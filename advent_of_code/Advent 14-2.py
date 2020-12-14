import re


def make_36_chars_long(string):
    zeros_to_add = 36 - len(string)
    string_out = '0' * zeros_to_add + string
    return string_out


def mask_address(mask, address):
    masked = []
    for ch in range(len(mask)):
        # if mask is 0 leave address character unchanged, otherwise add mask character
        if mask[ch] == '0':
            masked.append(address[ch])
        else:
            masked.append(mask[ch])
    return masked


def list_possible_addresses(base_address):
    address_book = []
    new_address = base_address.copy()
    # get base case if all Xs are zeroes
    new_address[:] = [ch if ch != 'X' else '0' for ch in base_address]
    decimal_address = int(''.join(new_address),2)
    address_book.append(decimal_address)

    for ch in range(1, len(base_address) + 1):
        if base_address[-ch] == 'X':
            x = len(address_book)
            # add value of new bit to each address in address_book and append to address_book
            for i in range(x):
                address_book.append(address_book[i] + (2 ** (ch - 1)))
    return address_book


f = open("input14.txt", "r")
# make dictionary of memory addresses and the values assigned to them
memory = {}

for line in f.readlines():
    if 'mask' in line.strip():
        mask = line.lstrip('mask = ').strip()
    else:
        address = make_36_chars_long(bin(int(re.search(r"(?<=mem\[)\d+", line).group(0))).lstrip('0b)'))
        val_to_memorise = int(re.search(r"(?<==\s)\d*", line).group(0))
        masked_address = mask_address(mask, address)
        for address in list_possible_addresses(masked_address):
            memory[address] = val_to_memorise

print(f'Task2: {sum(memory.values())}')
