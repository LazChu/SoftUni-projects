numbers = list(map(int, input().split()))
input_line = input()
while input_line != 'end':
    command = input_line.split()
    if command[0] == 'swap':
        numbers[int(command[1])], numbers[int(command[2])] = numbers[int(command[2])], numbers[int(command[1])]

    elif command[0] == 'multiply':
        numbers[int(command[1])] = numbers[int(command[1])] * numbers[int(command[2])]
    elif command[0] == 'decrease':
        numbers = list([num - 1 for num in numbers])
    input_line = input()
numbers_as_srting = [str(number) for number in numbers]
print(', '.join(numbers_as_srting))
