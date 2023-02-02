def min_num(num):
    return min(num)


def max_num(num):
    return max(num)


def sum_of_num(num):
    return sum(num)


nums = input().split()

numbers = []

for n in nums:
    numbers.append(int(n))

print(f"The minimum number is {min_num(numbers)}")
print(f"The maximum number is {max_num(numbers)}")
print(f"The sum number is: {sum_of_num(numbers)}")