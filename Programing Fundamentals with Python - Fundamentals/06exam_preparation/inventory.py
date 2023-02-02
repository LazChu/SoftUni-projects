collecting_items = input().split(', ')

command = input()
while command != "Craft!":
    command = command.split(' - ')
    action = command[0]
    item = command[1]
    if action == 'Collect':
        if item not in collecting_items:
            collecting_items.append(item)
    elif action == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif action == "Combine Items":
        items = item.split(':')
        first_item = items[0]
        second_item = items[1]
        if first_item in collecting_items:
            index = collecting_items.index(first_item)
            collecting_items.insert(index + 1, second_item)
    elif action == 'Renew':
        if item in collecting_items:
            index = collecting_items.index(item)
            item_to_replace = collecting_items.pop(index)
            collecting_items.append(item_to_replace)
    command = input()

print(', '.join(collecting_items))