numbers = input().split()
number = int(input())


for index in range(0, len(numbers)):
    numbers[index] = int(numbers[index])

for num in range(number):
    numbers.remove(min(numbers))

string_list = map(str, numbers)
print(', '.join(string_list))