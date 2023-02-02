numbers_of_joinery = int(input())
type_joinery = input()
way_of_delivery = (input())

price = 0

if type_joinery == '90X130':
    price = numbers_of_joinery * 110
    if 30 <= numbers_of_joinery < 60:
        price *= 0.95
    elif numbers_of_joinery >= 60:
        price *= 0.92
    elif numbers_of_joinery < 10:
        print('Invalid order')
elif type_joinery == '100X150':
    price = numbers_of_joinery * 140
    if 40 <= numbers_of_joinery < 80:
        price *= 0.94
    elif numbers_of_joinery >= 80:
        price *= 0.90
elif type_joinery == '130X180':
    price = numbers_of_joinery * 190
    if 20 <= numbers_of_joinery < 50:
        price *= 0.93
    elif numbers_of_joinery >= 50:
        price *= 0.88
elif type_joinery == '200X300':
    price = numbers_of_joinery * 250
    if 25 <= numbers_of_joinery < 50:
        price *= 0.91
    elif numbers_of_joinery >= 50:
        price *= 0.86
if way_of_delivery == 'With delivery':
    price = price + 60
else:
    price = price

if numbers_of_joinery >= 99:
    price *= 0.96
    print(f'{price:.2f} BGN')
elif numbers_of_joinery < 10:
    print('Invalid order')
else:
    print(f'{price:.2f} BGN')