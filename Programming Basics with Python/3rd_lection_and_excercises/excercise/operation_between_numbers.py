number_one = int(input())
number_two = int(input())
operation = input()

type = ' '
result = 0

if number_two == 0:
    print(f'Cannot divide {number_one} by zero')
elif operation == '+':
    result = number_one + number_two
elif operation == '-':
    result = number_one - number_two
elif operation == '*':
    result = number_one * number_two
elif operation == '/':
    result = number_one / number_two
    print(f"{number_one} / {number_two} = {result:.2f}")
elif operation == '%':
    result = number_one % number_two
    print(f"{number_one} % {number_two} = {result}")
if operation == '+' or operation == '-' or operation == '*':
    if result % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    print(f"{number_one} {operation} {number_two} = {result} - {type}")