juniors = int(input())
seniors = int(input())
race_type = input()

cost = 0
total_racers = juniors + seniors
tax_junior = 0
tax_senior = 0
discount = 0
if race_type == 'trail':
    tax_junior = 5.50 * juniors
    tax_senior = 7 * seniors
elif race_type == 'cross-country':
    tax_junior = 8 * juniors
    tax_senior = 9.50 * seniors
elif race_type == 'downhill':
    tax_junior = 12.25 * juniors
    tax_senior = 13.75 * seniors
elif race_type == 'road':
    tax_junior = 20 * juniors
    tax_senior = 21.50 * seniors

total_tax = tax_junior + tax_senior

if race_type == 'cross-country' and total_racers >= 50:
    total_tax = total_tax * 0.75
cost = total_tax * 0.95

print(f'{cost:.2f}')