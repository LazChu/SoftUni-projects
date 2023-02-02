word = input()

upper_index = [idx for idx in range(len(word)) if word[idx].isupper()]
print(str(upper_index))