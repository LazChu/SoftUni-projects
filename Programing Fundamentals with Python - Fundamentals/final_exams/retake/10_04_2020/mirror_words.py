import re
text = input()
pattern = r"(\@|\#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
searched = re.findall(pattern, text)
matches = []
mirrored_words = []
for word in searched:
    matches.append([word[1], word[2]])
total_matches = len(matches)

for match in matches:
    if match[0] == match[1][::-1]:
        joined_match = ' <=> '.join(match)
        mirrored_words.append(joined_match)
if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if len(mirrored_words) > 0:
    print(f"The mirror words are:")
    print(', '.join(mirrored_words))
else:
    print("No mirror words!")
