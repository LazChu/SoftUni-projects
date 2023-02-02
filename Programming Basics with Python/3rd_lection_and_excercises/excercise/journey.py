budget = float(input())
season = input()
is_valid = False
vacation = ' '
price = 0
destination = ' '

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation = 'Camp'
        price = budget * 0.70
    elif season == 'winter':
        vacation = 'Hotel'
        price = budget * 0.30
    is_valid = True
if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        vacation = 'Camp'
        price = budget * 0.60
    if season == 'winter':
        vacation = 'Hotel'
        price = budget * 0.20
    is_valid = True
if is_valid == False:
    destination = 'Europe'
    price = budget * 0.10
    vacation = 'Hotel'
money = budget - price
print(f"Somewhere in {destination}")
print(f"{vacation} - {money:.2f}")