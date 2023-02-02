# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.

vacation_price = float(input())
puzzels = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
total_toys = puzzels + dolls + teddy_bears + minions + trucks
money_made = (puzzels * 2.60) + (dolls * 3) + (teddy_bears * 4.10)\
    + (minions * 8.20) + (trucks * 2)
if total_toys >= 50:
    money_made = money_made - (money_made * 0.25)
rent = money_made * 0.10
all_money = money_made - rent
money_left = abs(all_money - vacation_price)
if all_money >= vacation_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_left:.2f} lv needed.")
