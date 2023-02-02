number_of_plants = int(input())

plants_rating = {}
plants_rarity = {}
for discovery in range(number_of_plants):
    input_plant = input().split("<->")
    plant = input_plant[0]
    rarity = int(input_plant[1])
    if plant not in plants_rarity:
        plants_rarity[plant] = 0
    plants_rarity[plant] = rarity
    plants_rating[plant] = []

command = input()
while command != "Exhibition":
    current_action = command.split()
    action = current_action[0]
    plant = current_action[1]
    if plant not in plants_rating.keys():
        print("error")
        command = input()
        continue
    if action == "Rate:":
        rating = int(current_action[3])
        # plants_rating[plant]
        plants_rating[plant].append(rating)
        # rating_dict = {int(rating)}
        # plants[plant].update(rating_dict)
    elif action == "Update:":
        rarity = int(current_action[3])
        if plant in plants_rarity.keys():
            plants_rarity[plant] = rarity
    elif action == "Reset:":
        if plant in plants_rating.keys():
            plants_rating[plant].clear()

    command = input()
print("Plants for the exhibition:")
for plant, rating in plants_rating.items():
    length = len(rating)
    if len(rating) != 0:
        total_rating = sum(rating) / len(rating)
        plants_rating[plant] = total_rating
    else:
        plants_rating[plant] = 0

for plant in plants_rating.keys() and plants_rarity.keys():
    print(f"- {plant}; Rarity: {plants_rarity[plant]}; Rating: {plants_rating[plant]:.2f}")
