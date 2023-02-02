numbers = input().split(', ')

integers = list(map(int, numbers))
indices = []

for index in range(len(integers)):
    if integers[index] % 2 == 0:
        indices.append(index)
print(indices)
