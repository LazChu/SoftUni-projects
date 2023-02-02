budget = float(input())
gender = input()
age = int(input())
sport = input()

if gender == 'm':
    if sport == 'Gym':
        cost = 42
    elif sport == 'Boxing':
        cost = 41
    elif sport == 'Yoga':
        cost = 45
    elif sport == 'Zumba':
        cost = 34
    elif sport == 'Dances':
        cost = 51
    elif sport == 'Pilates':
        cost = 39
elif gender == 'f':
    if sport == 'Gym':
        cost = 35
    elif sport == 'Boxing':
        cost = 37
    elif sport == 'Yoga':
        cost = 42
    elif sport == 'Zumba':
        cost = 31
    elif sport == 'Dances':
        cost = 53
    elif sport == 'Pilates':
        cost = 37
if age <= 19:
    cost = cost - (cost * 0.20)

if budget >= cost:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = abs(budget - cost)
    print(f"You don't have enough money! You need ${diff:.2f} more.")