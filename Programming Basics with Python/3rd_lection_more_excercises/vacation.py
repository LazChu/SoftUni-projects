budget = float(input())
season = input()

trip_price = 0

if budget <= 1000:
    accommodation = 'Camp'
    if season == 'Summer':
        trip_price = budget * 0.65
    else:
        trip_price = budget * 0.45
elif budget <= 3000:
    accommodation = 'Hut'
    if season == 'Summer':
        trip_price = budget * 0.80
    else:
        trip_price = budget * 0.60
else:
    accommodation = 'Hotel'
    trip_price = budget * 0.90

if season == 'Summer':
    location = 'Alaska'
else:
    location = 'Morocco'

print(f'{location} - {accommodation} - {trip_price:.2f}')