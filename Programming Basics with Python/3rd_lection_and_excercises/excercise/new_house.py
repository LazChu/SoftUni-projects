flower_type = input()
flowers = int(input())
budged = int(input())
price = 0
discount = 0
increase = 0
money_difference = 0
total_price = 0
# discount_price = price - discount
# price_increase = price + increase
if flower_type == 'Roses':
    price = flowers * 5.00
    if flowers > 80:
        discount = price * 0.10
elif flower_type == 'Dahlias':
    price = flowers * 3.80
    if flowers > 90:
        discount = price * 0.15
elif flower_type == 'Tulips':
    price = flowers * 2.80
    if flowers > 80:
        discount = price * 0.15
elif flower_type == 'Narcissus':
    price = flowers * 3
    if flowers < 120:
        increase = price * 0.15
elif flower_type == 'Gladiolus':
    price = flowers * 2.50
    if flowers < 80:
        increase = price * 0.20
if flower_type == 'Narcissus' or flower_type == 'Gladiolus':
    total_price = price + increase
    money_difference = abs(budged - total_price)
elif flower_type == 'Roses' or flower_type == 'Dahlias' or flower_type == 'Tulips':
    total_price = price - discount
    money_difference = abs(budged - total_price)
if total_price <= budged:
    print(f"Hey, you have a great garden with {flowers} {flower_type} and {money_difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference:.2f} leva more.")