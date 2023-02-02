destination = input()
dates = input()
stay = int(input())

if destination == 'France':
    if dates == '21-23':
        price = 30 * stay
    elif dates == '24-27':
        price = 35 * stay
    elif dates == '28-31':
        price = 40 * stay
elif destination == 'Italy':
    if dates == '21-23':
        price = 28 * stay
    elif dates == '24-27':
        price = 32 * stay
    elif dates == '28-31':
        price = 39 * stay
elif destination == 'Germany':
    if dates == '21-23':
        price = 32 * stay
    elif dates == '24-27':
        price = 37 * stay
    elif dates == '28-31':
        price = 43 * stay

print(f"Easter trip to {destination} : {price:.2f} leva.")