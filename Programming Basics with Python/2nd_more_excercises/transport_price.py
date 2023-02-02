# Такси. Начална такса: 0.70 лв. Дневна тарифа: 0.79 лв. / км. Нощна тарифа: 0.90 лв. / км.
# Автобус. Дневна / нощна тарифа: 0.09 лв. / км. Може да се използва за разстояния минимум 20 км.
# Влак. Дневна / нощна тарифа: 0.06 лв. / км. Може да се използва за разстояния минимум 100 км.

kilometers = int(input())
time_of_day = input()
price = 0
if time_of_day == 'day':
    if kilometers < 20:
        price = kilometers * 0.79 + 0.70
    elif 20 <= kilometers < 100:
        price = kilometers * 0.09
    elif kilometers >= 100:
        price = kilometers * 0.06
else:
    if kilometers < 20:
        price = kilometers * 0.90 + 0.7
    elif 20 <= kilometers < 100:
        price = kilometers * 0.09
    elif kilometers >= 100:
        price = kilometers * 0.06

print(f'{price:.2f}')