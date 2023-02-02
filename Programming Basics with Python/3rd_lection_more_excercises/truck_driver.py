season = input()
kilometers_per_month = float(input())

paycheck = 0

if kilometers_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        paycheck = kilometers_per_month * 0.75
    elif season == 'Summer':
        paycheck = kilometers_per_month * 0.90
    else:
        paycheck = kilometers_per_month * 1.05
elif kilometers_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        paycheck = kilometers_per_month * 0.95
    elif season == 'Summer':
        paycheck = kilometers_per_month * 1.10
    else:
        paycheck = kilometers_per_month * 1.25
elif kilometers_per_month <= 20000:
    paycheck = kilometers_per_month * 1.45

season_payment = paycheck * 4
total_payout = season_payment * 0.90

print(f'{total_payout:.2f}')