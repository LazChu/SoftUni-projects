import sys

numbers = int(input())

max_num = -sys.maxsize
sum = 0
for i in range(numbers):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number
if max_num == sum - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(max_num - (sum - max_num))
    print('No')
    print(f'Diff = {diff}')