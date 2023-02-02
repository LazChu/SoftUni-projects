input_line = input()
coffies = 0
while input_line != 'END':
    if input_line == 'coding' or input_line == 'dog' or input_line == 'cat' or \
            input_line == 'movie':
        coffies += 1
    elif input_line == 'CODING' or input_line == 'DOG' or input_line == 'CAT' \
            or input_line == 'MOVIE':
        coffies += 2
    else:
        input_line = input()
        continue
    input_line = input()
if coffies > 5:
    print('You need extra sleep')
else:
    print(coffies)