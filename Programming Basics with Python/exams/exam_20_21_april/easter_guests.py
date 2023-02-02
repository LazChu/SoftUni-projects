import cmath
import math

guests = int(input())
budget = int(input())

egg_price = 0.45
easter_bread_price = 4

eggs = guests * 2
easter_bread = math.ceil(guests / 3)
cost_eggs = egg_price * eggs
cost_easter_bread = easter_bread * easter_bread_price
total_cost = cost_eggs + cost_easter_bread
diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Lyubo bought {easter_bread} Easter bread and {eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")
