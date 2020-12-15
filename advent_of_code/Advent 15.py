starting_numbers = [12, 1, 16, 3, 11, 0]


def play_game(starting_numbers, target_turn):
    numbers_spoken = {}
    # add starting numbers (except last one) to dictionary of numbers spoken
    for index in range(len(starting_numbers) - 1):
        numbers_spoken[starting_numbers[index]] = index
    # initialize the game using the last of the starting numbers
    last_spoken = starting_numbers[-1]
    # take turns
    for turn_number in range(len(starting_numbers) - 1, target_turn):
        # check if we are at the target_turn
        result = last_spoken if turn_number == target_turn-1 else None
        # if it's been said before add this turn to the spoken_numbers dic
        # and make last spoken equal the gap between this turn and the last time it was spoken
        # otherwise add it the the spoken_numbers dictionary and set last spoken = 0 for next loop
        if last_spoken in numbers_spoken:
            temp = turn_number - numbers_spoken[last_spoken]
            numbers_spoken[last_spoken] = turn_number
            last_spoken = temp
        else:

            numbers_spoken[last_spoken] = turn_number
            last_spoken = 0
    return result

print(f'Task1: {play_game(starting_numbers, 2020)}')
print(f'Task2: {play_game(starting_numbers, 30000000)}')