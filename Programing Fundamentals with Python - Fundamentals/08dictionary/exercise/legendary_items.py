items = {'shards': 0, 'fragments': 0, 'motes': 0}
constructed = False
command = input().split(" ")
while not constructed:
    for index in range(0, len(command), 2):
        quantity = int(command[index])
        material = command[index + 1]
        if material.lower() not in items.keys():
            items[material.lower()] = 0
        items[material.lower()] += quantity
        if items['shards'] >= 250:
            items['shards'] -= 250
            print("Shadowmourne obtained!")
            constructed = True
            break
        elif items['fragments'] >= 250:
            items['fragments'] -= 250
            print("Valanyr obtained!")
            constructed = True
            break
        elif items['motes'] >= 250:
            items['motes'] -= 250
            print("Dragonwrath obtained!")
            constructed = True
            break
    if constructed:
        break
    command = input().split(" ")
for key, value in items.items():
    print(f"{key}: {value}")