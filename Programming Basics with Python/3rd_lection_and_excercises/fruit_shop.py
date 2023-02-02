fruit = input()
day = input()
quantity = float(input())

work_days = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday'\
    or day == 'Thursday' or day == 'Friday'
weekend = day == 'Saturday' or day == 'Sunday'
invalid = False
price = 0

if work_days:
    if fruit == 'apple':
        price = 1.20
    elif fruit == 'banana':
        price = 2.50
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    else:
        invalid = True
    total = price * quantity

elif weekend:
    if fruit == 'apple':
        price = 1.25
    elif fruit == 'banana':
        price = 2.70
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        invalid = True
    total = price * quantity

else:
    invalid = True

if invalid is True:
    print('error')
else:
    print(f'{total:.2f}')
