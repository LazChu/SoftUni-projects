start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
sum = 0
combination_found = False

for n1 in range(start, end+ 1):
    for n2 in range(start, end +1):
        counter += 1
        sum = n1 + n2
        if sum == magic_number:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter} ({n1} + {n2} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")