budget = float(input())
flour_price = float(input())
colored_eggs = 0
loaves = 0
lost_eggs = 0
total_lost_eggs = 0
loav_cost = 0
total_colored_eggs = 0
while budget > loav_cost:
    egg_price = flour_price - (flour_price * 0.25)
    milk_per_litre = flour_price * 1.25
    milk_price = milk_per_litre / 4
    loav_cost = flour_price + egg_price + milk_price
    loaves += 1
    colored_eggs += 3
    budget -= loav_cost

    money_left = budget - loav_cost
    if loaves % 3 == 0:
        lost_eggs = loaves - 2
        total_lost_eggs += lost_eggs
    total_colored_eggs = colored_eggs - total_lost_eggs

print(f"You made {loaves} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {budget:.2f}BGN left.")
