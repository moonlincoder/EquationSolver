with open("calculator.py", "w") as file:
    file.write("""
num1 = int(input('Введите первое число: '))
sign = input('Выберите операцию [+, -, /, *]: ')
num2 = int(input('Введите второе число: '))
""")

    for a in ['+', '-', '*', '/']:
        for i in range(1, 1000):
            for j in range(1, 1000):
                file.write(
f"""
if num1 == {i} and sign == '{a}' and num2 == {j}:
    print("{i}{a}{j} = {eval(str(i)+a+str(j))}")
""")
