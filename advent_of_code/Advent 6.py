
f = open("input6.txt", "r")
answers = f.read().split('\n\n')

num_respondants = [answer.count("\n") + 1 for answer in answers]
qs_answered = [answer.replace('\n', '') for answer in answers]
set_qs_answered = [set(answer) for answer in qs_answered]
print(f'Task1: {sum(len(set_qs) for set_qs in set_qs_answered)}')

count = 0
for i in range(len(num_respondants)):
    for ch in set_qs_answered[i]:
        if answers[i].count(ch) == num_respondants[i]:
            count += 1
print(f'Task2: {count}')


## David Buck's answer:
data = [list(map(set, x.split('\n'))) for x in open("input6.txt", 'r').read().split('\n\n')]
print(f"""AoC 2020 Day 6 Part 1 answer is: {sum(len(set.union(*x)) for x in data)}""")
print(f"""AoC 2020 Day 6 Part 2 answer is: {sum(len(set.intersection(*x)) for x in data)}""")
