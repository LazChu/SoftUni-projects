words = input().split(' ')
my_dict = {}
final_list = []
for word in words:
    counter = 1
    key = word.lower()
    value = int(counter)
    if key not in my_dict.keys():
        my_dict[key] = 0
    my_dict[key] += 1
for key,value in my_dict.items():
    if value % 2 != 0:
        final_list.append(key)
print(' '.join(final_list))