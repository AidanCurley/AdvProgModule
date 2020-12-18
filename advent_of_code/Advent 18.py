def evaluate(num1,operator, num2):
    if operator == '+':
        result = str(int(num1) + int(num2))
    elif operator == '*':
        result = str(int(num1) * int(num2))
    return result


def count_parentheses(expression):
    return expression.count('(')


def get_indexes_of_parentheses(expression):
    first_parenthesis, last_parenthesis = 0, 0
    for index,ch in enumerate(list(expression)):
        if ch == '(':
            first_parenthesis = index
        elif ch == ')':
            last_parenthesis = index
            return first_parenthesis, last_parenthesis


def solve_expression(expression):
    expression = expression.split(" ")
    result = evaluate(expression[0], expression[1], expression[2])
    for i in range(3,len(expression),2):
        result = evaluate(result, expression[i], expression[i+1])
    return result


f = open("input18.txt", "r")
input = f.read().split('\n')[:-1]

total = 0
for line in input:
    expression = line.strip()
    for i in range(count_parentheses(expression)):
        x, y = get_indexes_of_parentheses(expression)
        expression = expression[:x] + solve_expression(expression[x+1:y]) + expression[y+1:]
    total += float(solve_expression(expression))

print(f'Task1: {total}')


def solve_expression_task2(expression):
    expression = expression.split(" ")
    for _ in range(expression.count('+')):
        index = expression.index('+')
        solution = evaluate(expression[index-1], expression[index], expression[index + 1])
        for _ in range(3):
            expression.pop(index-1)
        expression.insert(index-1, solution)
    if len(expression) > 1:
        return solve_expression(" ".join(expression))
    else:
        return " ".join(expression)


total = 0
for line in input:
    expression = line.strip()
    for i in range(count_parentheses(expression)):
        x, y = get_indexes_of_parentheses(expression)
        expression = expression[:x] + solve_expression_task2(expression[x+1:y]) + expression[y+1:]
    total += float(solve_expression_task2(expression))

print(f'Task2: {total}')