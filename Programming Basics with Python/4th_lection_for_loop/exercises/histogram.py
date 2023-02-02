numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for n in range(numbers):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number <= 399:
        p2 += 1
    elif 400 <= number <= 599:
        p3 += 1
    elif 600 <= number <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / numbers * 100:.2f}%")
print(f"{p2 / numbers * 100:.2f}%")
print(f"{p3 / numbers * 100:.2f}%")
print(f"{p4 / numbers * 100:.2f}%")
print(f"{p5 / numbers * 100:.2f}%")
