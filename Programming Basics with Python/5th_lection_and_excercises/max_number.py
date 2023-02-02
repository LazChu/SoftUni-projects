import sys

input_line = input()

max_num = -sys.maxsize

while input_line != 'Stop':
    number = int(input_line)
    if number > max_num:
        max_num = number

    input_line = input()
print(max_num)