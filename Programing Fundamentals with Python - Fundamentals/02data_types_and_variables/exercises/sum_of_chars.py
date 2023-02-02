characters = int(input())
sum = 0
for char in range(characters):
    letter = input()
    sum += ord(letter)
print(f"The sum equals: {sum}")