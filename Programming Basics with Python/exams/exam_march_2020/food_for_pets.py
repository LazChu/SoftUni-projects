days = int(input())
food_quantity = float(input())

total_dog = 0
total_cat = 0
bonus = 0
biscuits = 0
current_day = 0
for i in range(days):
    dog = int(input())
    cat = int(input())
    total_dog += dog
    total_cat += cat
    food_eaten = total_cat + total_dog
    dog_eaten = total_dog / food_eaten * 100
    cat_eaten = total_cat / food_eaten * 100
    food_eaten_percent = food_eaten / food_quantity * 100
    current_day += 1
    if current_day % 3 == 0:
        bonus = (cat + dog) * 0.10
        biscuits += bonus
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{food_eaten_percent:.2f}% of the food has been eaten.")
print(f"{dog_eaten:.2f}% eaten from the dog.")
print(f"{cat_eaten:.2f}% eaten from the cat.")