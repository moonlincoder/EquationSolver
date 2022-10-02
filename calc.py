import math


def eqSolver(eq: str) -> int:
    eq = eq.replace(" ", '')

    # eq to mas of num and opers
    operations = []
    numbers = []
    s_num = ''
    down = 0

    for pos, symbol in enumerate(eq):
        # recursively count joins into ("(")
        if symbol == '(':
            down += 1

        # after exiting exclude equation and count
        elif symbol == ')':
            down -= 1
            if down == 0:
                numbers.append(eqSolver(s_num))
                s_num = ''

        elif symbol.isdecimal() or symbol == '.' or down != 0:
            s_num = s_num + symbol

        else:
            numbers.append(s_num)
            operations.append(symbol)
            s_num = ''

    numbers.append(s_num)

    # print(operations, numbers)

    # ['-', '*', '+', '/'] => [2,4,1,3]
    index = []
    for searchoper in ['^', '*/', '+-']:
        nowind = 0
        for oper in operations:
            if oper in searchoper:
                index.append(nowind)
            nowind += 1

    # calculate replacing two numbers to solved one
    for i in index:
        if operations[i] == '^':
            numbers[i] = math.pow(float(numbers[i]), float(numbers[i + 1]))
            numbers.pop(i + 1)
        if operations[i] == '*':
            numbers[i] = float(numbers[i]) * float(numbers[i + 1])
            numbers.pop(i + 1)
        elif operations[i] == '/':
            if numbers[i + 1] == 0:
                raise ValueError(f"Dividing by zero")

            numbers[i] = float(numbers[i]) / float(numbers[i + 1])
            numbers.pop(i + 1)
        elif operations[i] == '+':
            numbers[i] = float(numbers[i]) + float(numbers[i + 1])
            numbers.pop(i + 1)
        elif operations[i] == '-':
            numbers[i] = float(numbers[i]) - float(numbers[i + 1])
            numbers.pop(i + 1)

        # move indices
        operations.pop(i)
        for point, value in enumerate(index):
            if value > i:
                index[point] -= 1

    return numbers[0]


if __name__ == '__main__':
    eq = input('equation:')
    # ex:  3-4*4 + (10 - 4^0.5)
    # ans: -5

    print(f'equation: {eq}')
    print(f'answer: {eqSolver(eq)}')
