days = int(input())
food_in_kilos = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

import math
turtle_food_in_kilos = turtle_food / 1000
total_food = (dog_food + cat_food + turtle_food_in_kilos) * days
difference = abs(total_food - food_in_kilos)

if food_in_kilos >= total_food:
    print(f'{math.floor(difference)} kilos of food left.')
else:
    print(f'{math.ceil(difference)} more kilos of food are needed.')