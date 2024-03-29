def groups(max_num):
    group = (max_num // 10 + 1) * 10
    if max_num % 10 == 0:
        group -= 10
    return group


numbers_list = [int(x) for x in input().split(', ')]
max_num = max(numbers_list)
biggest_group = groups(max_num)
number_groups = []
for num in range(biggest_group // 10):
    number_groups.append([])
for number in numbers_list:
    index = number // 10
    if number % 10 == 0 and number != 0:
        index -= 1
    number_groups[index].append(number)
groups_list = [f"Group of {(x + 1) * 10}'s: {number_groups[x]}" for x in range(len(number_groups))]
print(*groups_list, sep='\n')
