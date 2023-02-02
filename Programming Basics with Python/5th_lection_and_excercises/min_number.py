import sys

input_line = input()

min_num = sys.maxsize

while input_line != 'Stop':
    number = int(input_line)
    if number < min_num:
        min_num = number

    input_line = input()
print(min_num)