first_number = input()
second_number = input()

for index_one in range(int(first_number[0]), int(second_number[0]) + 1):
    if index_one % 2 == 0:
        continue
    for index_two in range(int(first_number[1]), int(second_number[1]) + 1):
        if index_two % 2 == 0:
            continue
        for index_three in range(int(first_number[2]), int(second_number[2]) + 1):
            if index_three % 2 == 0:
                continue
            for index_four in range(int(first_number[3]), int(second_number[3]) + 1):
                if index_four % 2 == 0:
                    continue
                print(f'{index_one}{index_two}{index_three}{index_four}', end=' ')
