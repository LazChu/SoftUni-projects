# Бензин – 2.22
# Дизел – 2.33
# Газ – 0.93

# намаления за литър гориво:
# 18 ст. за литър бензин,
# 12 ст. за литър дизел
# 8 ст. за литър газ.

fuel_type = input()
litres_fuel = float(input())
club_card = input()
price = 0
discount = 0
if fuel_type == 'Gasoline':
    price = litres_fuel * 2.22
    if club_card == 'Yes':
        discount = litres_fuel * 0.18
    else:
        discount = 0
elif fuel_type == 'Diesel':
    price = litres_fuel * 2.33
    if club_card == 'Yes':
        discount = litres_fuel * 0.12
    else:
        discount = 0
elif fuel_type == 'Gas':
    price = litres_fuel * 0.93
    if club_card == 'Yes':
        discount = litres_fuel * 0.08

total_price = price - discount

if 20 <= litres_fuel <= 25:
    total_price = total_price - (total_price * 0.08)
elif litres_fuel > 25:
    total_price = total_price - (total_price * 0.10)

print(f'{total_price:.2f} lv.')