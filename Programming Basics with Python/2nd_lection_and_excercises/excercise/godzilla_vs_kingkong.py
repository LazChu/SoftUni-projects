budget = float(input())
statists = int(input())
price_cloathing = float(input())
money_needed = statists * price_cloathing
decor = budget * 0.10

if statists >= 150:
    money_needed = money_needed - (money_needed * 0.10)

money = money_needed + decor
total_sum = abs(money - budget)

if money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_sum:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {total_sum:.2f} leva left.")
