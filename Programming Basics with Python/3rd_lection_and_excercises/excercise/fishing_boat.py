budget = int(input())
season = input()
total_fisherman = int(input())
rent = 0
discount = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600.

if total_fisherman <= 6:
    discount = 0.10
elif 7 <= total_fisherman <= 11:
    discount = 0.15
elif total_fisherman >= 12:
    discount = 0.25

if total_fisherman % 2 == 0 and season != 'Autumn':
    rent = rent - (rent * 0.05)

discount = rent * discount
money = rent - discount
total = abs(budget - money)

if money <= budget:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")