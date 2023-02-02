budget = float(input())
season = input()

loan_price = 0
if season == 'Summer':
    car_type = 'Cabrio'
else:
    car_type = 'Jeep'

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        loan_price = budget * 0.35
    else:
        loan_price = budget * 0.65
elif budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        loan_price = budget * 0.45
    else:
        loan_price = budget * 0.80
else:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    loan_price = budget * 0.90

print(f'{car_class}')
print(f'{car_type} - {loan_price:.2f}')