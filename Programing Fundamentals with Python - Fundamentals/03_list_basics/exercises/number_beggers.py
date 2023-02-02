beggars_take = input().split(', ')
number_of_beggars = int(input())
beggars_total = []
total_beggars = 0
for beggars in range(number_of_beggars):
    sum_beggars = 0
    for beggar in range(total_beggars, len(beggars_take), number_of_beggars):
        sum_beggars += int(beggars_take[beggar])
        if number_of_beggars > len(beggars_take):
            break
    total_beggars += 1
    beggars_total.append(sum_beggars)
print(beggars_total)
