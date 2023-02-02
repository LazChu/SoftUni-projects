lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        expenses += helmet_price
    if fight % 3 == 0:
        expenses += sword_price
    if fight % 6 == 0:
        expenses += shield_price
    if fight % 12 == 0:
        expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
