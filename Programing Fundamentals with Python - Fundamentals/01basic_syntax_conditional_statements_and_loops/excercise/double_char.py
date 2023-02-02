input_line = input()
# final = ''
while input_line != 'End':
    final = ''
    if input_line == 'SoftUni':
        input_line = input()
        continue
    else:
        for char in input_line:
            final += char * 2
    print(final)
    input_line = input()