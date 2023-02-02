number = int(input())
my_dict = {}

synonyms = []
for word in range(number):
    word = input()
    synonim = input()
    my_dict[word] = word
    my_dict[word] = {}

    if synonim != word:
        synonyms.append(synonim)
    my_dict[word] = synonyms

for word in my_dict.keys():
    print(f"{word} - {' '.join(synonyms)}")
