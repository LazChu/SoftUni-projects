start = int(input())
end = int(input())

start_str = str(start)
end_str = str(end)

for number_one in range(int(start_str[0]), int(end_str[0]) + 1):
    if number_one % 2 == 0:
        continue
    for number_two in range(int(start_str[1]), int(end_str[1]) +1):
        if number_two % 2 == 0:
            continue
        for number_three in range(int(start_str[2]), int(end_str[2]) + 1):
            if number_three % 2 == 0:
                continue
            for number_four in range(int(start_str[3]), int(end_str[3])+1):
                if number_four % 2 == 0:
                    continue
                print(f'{number_one}{number_two}{number_three}{number_four}', end=' ')