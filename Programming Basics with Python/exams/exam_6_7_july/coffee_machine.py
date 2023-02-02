beverage = input()
sugar = input()
number_of_beverages = int(input())

if beverage == 'Espresso':
    if sugar == 'Without':
        price = 0.90
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.20
elif beverage == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.20
    elif sugar == 'Extra':
        price = 1.60
elif beverage == 'Tea':
    if sugar == 'Without':
        price = 0.50
    elif sugar == 'Normal':
        price = 0.60
    elif sugar == 'Extra':
        price = 0.70

total_price = number_of_beverages * price
if sugar == 'Without':
    total_price *= 0.65
if beverage == 'Espresso' and number_of_beverages >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_beverages} cups of {beverage} for {total_price:.2f} lv.")