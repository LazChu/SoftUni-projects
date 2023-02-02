divisor = int(input())
boundary = int(input())
number = 0
# for n in range(boundary +1, -1, -1):
#     if n % divisor == 0:
#         print(n)
#         break
for n in range(boundary +1):
    if n % divisor == 0:
        number = n
print(number)