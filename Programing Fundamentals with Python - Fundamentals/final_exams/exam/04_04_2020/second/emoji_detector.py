import re

pattern = r"(:{2}|\*{2})([A-Z]{1}[a-z]{2,})(\1)"

string = input()

matches = re.findall(pattern, string)

total_coolness = 1
for number in string:
    if number.isdigit():
        total_coolness *= int(number)
emoji_dict = {}
for match in matches:
    emoji = match[1]
    coolness = 0
    sep = match[0]
    for letter in emoji:
        coolness += ord(letter)
    emoji_dict[emoji] = {'coolness': coolness, 'sep': sep}

print(f"Cool threshold: {total_coolness}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for emoji in emoji_dict:
    if emoji_dict[emoji]['coolness'] > total_coolness:
        separator = emoji_dict[emoji]['sep']
        print(f"{separator}{emoji}{separator}")