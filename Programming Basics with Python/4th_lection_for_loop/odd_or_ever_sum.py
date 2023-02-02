numbers = int(input())

even_sum = 0
odd_sum = 0

for num in range(1, numbers + 1):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if even_sum == odd_sum:
    print(f'Yes')
    print(f'Sum = {odd_sum}')
else:
    print('No')
    difference = abs(even_sum - odd_sum)
    print(f'Diff = {difference}')