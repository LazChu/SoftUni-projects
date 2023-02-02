import math

people = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

entrance_total = entrance_fee * people
deck_chair = math.ceil(people * 0.75)
umbrella = math.ceil(people / 2)
total_deck_chair = deck_chair * deck_chair_price
total_umbrella = umbrella * umbrella_price

total_amount = entrance_total + total_umbrella + total_deck_chair

print(f"{total_amount:.2f} lv.")