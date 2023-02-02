days = int(input())
accommodation = input()
review = input()

price_per_night = 0
price = 0

nights_stay = days - 1
if accommodation == 'room for one person':
    price = nights_stay * 18
elif accommodation == "apartment":
    if days < 10:
        price = (nights_stay * 25) * 0.70
    elif 10 <= days <= 15:
        price = (nights_stay * 25) * 0.65
    else:
        price = (nights_stay * 25) * 0.50
elif accommodation == "president apartment":
    if days < 10:
        price = (nights_stay * 35) * 0.65
    elif 10 <= days <= 15:
        price = (nights_stay * 35) * 0.85
    else:
        price = (nights_stay * 35) * 0.80

if review == 'positive':
    total_price = price + (price * 0.25)
else:
    total_price = price - (price * 0.10)

print(f'{total_price:.2f}')