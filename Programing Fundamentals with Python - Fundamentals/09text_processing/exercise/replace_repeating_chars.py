text = input()
output = ""
counter = len(text)
for index in range(len(text)):
    current_letter = text[index]
    if current_letter not in output:
        output += current_letter
    else:
        output.replace(current_letter,'')