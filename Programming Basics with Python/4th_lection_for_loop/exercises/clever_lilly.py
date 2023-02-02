years_old = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
total_toys = 0
birthday_money = 0

for y in range(1 , years_old +1):
    if y % 2 != 0:              #нечетна
        total_toys += 1
    else:
        birthday_money += 10
        money += birthday_money - 1

money = money + total_toys * toy_price
diff = abs(washing_machine_price - money)
if money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")




years_old = int(input())
washing_machine_price = float(input())
toy_price = int(input())

birthday_money = 0
toys = 0
brother_money = 0
money = 0
for years in range(1, years_old + 1):
    if years % 2 == 0:
        birthday_money += 10
        brother_money += 1
        money += birthday_money
    else:
        toys += 1

toys_profit = toys * toy_price
total_money = money + toys_profit - brother_money
money_left = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {money_left:.2f}')
else:
    print(f'No! {money_left:.2f}')