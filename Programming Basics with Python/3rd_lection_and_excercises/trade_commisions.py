town = input()
sales = float(input())

commission = 0
validation = True

if town == 'Sofia':
    if sales < 0:
        validation = False
    elif 0 <= sales <= 500:
        commission = 0.05
    elif 500 < sales <= 1000:
        commission = 0.07
    elif 1000 < sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
    money = commission * sales

elif town == 'Varna':
    if sales < 0:
        validation = False
    elif 0 <= sales <= 500:
        commission = 0.045
    elif 500 < sales <= 1000:
        commission = 0.075
    elif 1000 < sales <= 10000:
        commission = 0.10
    elif sales > 10000:
        commission = 0.13
    money = commission * sales

elif town == 'Plovdiv':
    if sales < 0:
        validation = False
    elif 0 <= sales <= 500:
        commission = 0.055
    elif 500 < sales <= 1000:
        commission = 0.08
    elif 1000 < sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    money = commission * sales

else:
    validation = False

if validation is True :
    print(f'{money:.2f}')
else:
    print('error')