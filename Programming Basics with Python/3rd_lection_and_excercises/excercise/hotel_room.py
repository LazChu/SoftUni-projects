month = input()
overnight_stays = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = 50 * overnight_stays
    price_apartment = 65 * overnight_stays
    if 7 < overnight_stays <= 14:
        price_studio *= 0.95
    elif overnight_stays > 14:
        price_studio *= 0.70
    elif overnight_stays > 14:
        price_apartment *= 0.90
if month == 'June' or month == 'September':
    price_studio = 75.20 * overnight_stays
    price_apartment = 68.70 * overnight_stays
    if overnight_stays > 14:
        price_studio *= 0.80
if month == 'July' or month == 'August':
    price_studio = 76 * overnight_stays
    price_apartment = 77 * overnight_stays

if overnight_stays > 14:
    price_apartment *= 0.90

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
