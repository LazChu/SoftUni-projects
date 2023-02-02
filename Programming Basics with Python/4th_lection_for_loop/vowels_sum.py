text = input()

sum = 0
text_lenght = len(text)
for letter in text:
    if letter == 'a':
        sum += 1
    elif letter == 'e':
        sum += 2
    elif letter == 'i':
        sum += 3
    elif letter == "o":
        sum += 4
    elif letter == 'u':
        sum += 5
print(sum)