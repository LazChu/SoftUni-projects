food_in_kilos = int(input())
command = input()

total_food_eaten = 0
food_is_enough = False

while command != 'Adopted':
    eaten_food = int(command)
    food = food_in_kilos * 1000
    total_food_eaten += eaten_food
    if total_food_eaten <= food:
        food_is_enough = True
    else:
        food_is_enough = False
    diff = abs(total_food_eaten - food)
    command = input()
if food_is_enough:
    print(f"Food is enough! Leftovers: {diff} grams." )
else:
    print(f"Food is not enough. You need {diff} grams more." )