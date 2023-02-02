fruit = input()
size = input()
number_sets = int(input())

if fruit == 'Watermelon':
    if size == 'small':
        price = 56 * (2 * number_sets)
    elif size == 'big':
        price = 28.70 * (5 * number_sets)
elif fruit == 'Mango':
    if size == 'small':
        price = 36.66 * (2 * number_sets)
    elif size == 'big':
        price = 19.60 * (5 * number_sets)
elif fruit == 'Pineapple':
    if size == 'small':
        price = 42.10 * (2 * number_sets)
    elif size == 'big':
        price = 24.80 * (5 * number_sets)
elif fruit == 'Raspberry':
    if size == 'small':
        price = 20 * (2 * number_sets)
    elif size == 'big':
        price = 15.20 * (5 * number_sets)


if 400 <= price <= 1000:
    price = price - (price * 0.15)
elif price > 1000:
    price = price - (price * 0.50)

print(f'{price:.2f} lv.')