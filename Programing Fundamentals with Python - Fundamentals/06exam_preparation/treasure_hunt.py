initial_treasure = input().split('|')
command = input()
stolen_treasure = []
treasure_value = 0

while command != "Yohoho!":
    actions = command.split(' ')
    action = actions[0]
    item = actions[1]
    if action == "Loot":
        items = actions[1::]
        for current_item in items:
            if current_item not in initial_treasure:
                initial_treasure.insert(0, current_item)
    elif action == "Drop":
        lenght = len(initial_treasure)
        if int(item) <= len(initial_treasure):
            shuffled_item = initial_treasure.pop(int(item))
            initial_treasure.append(shuffled_item)
    elif action == "Steal":
        items_to_steal = int(item)
        if items_to_steal > len(initial_treasure):
            stolen_treasure = initial_treasure
            print(', '.join(stolen_treasure))
            initial_treasure.clear()
        else:
            stolen_treasure = initial_treasure[-items_to_steal:]
            initial_treasure = initial_treasure[:len(initial_treasure) - items_to_steal]
            print(', '.join(stolen_treasure))
    command = input()
if len(initial_treasure) > 0:
    for treasure in initial_treasure:
        treasure_value += len(treasure)
    average_treasure = treasure_value / len(initial_treasure)
    print(f"Average treasure gain: {average_treasure:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
