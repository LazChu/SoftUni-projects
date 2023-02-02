shopping_list = input().split('!')
command = input()
while command != "Go Shopping!":
    order = command.split()
    item = order[1]
    action = order[0]
    if action == 'Urgent':
        if item in shopping_list:
            command = input()
            continue
        else:
            shopping_list.insert(0, item)
    elif action == 'Unnecessary':
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == 'Correct':
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.insert(index, order[2])
    elif action == 'Rearrange':
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.append(item)
    command = input()
print(', '.join(shopping_list))
