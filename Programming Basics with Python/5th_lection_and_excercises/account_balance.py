input_line = input()

sum = 0
while input_line != 'NoMoreMoney':
    amount = float(input_line)
    if amount < 0:
        print(f'Invalid operation!')
        break
    sum += amount
    print(f'Increase: {amount:.2f}')
    input_line = input()

print(f'Total: {sum:.2f}')