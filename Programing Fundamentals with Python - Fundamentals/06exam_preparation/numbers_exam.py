def greater_number(numbers_list, average):
    final_list = []
    for num in numbers:
        if int(num) > average_number:
            final_list.append(num)
        if len(final_list) >= 5:
            break

    if len(final_list) == 0:
        return 'No'
    # elif int(final_list[0]) < 0:
    #     return ' '.join(sorted(final_list))
    else:
        return ' '.join(sorted(final_list)[::-1])


numbers = input().split()
# sorted_numbers = sorted(numbers, reverse=True)
sum_of_list = sum([int(x) for x in numbers])
average_number = sum_of_list / len(numbers)
print(greater_number(numbers, average_number))
