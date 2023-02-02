budget = float(input())
nights = int(input())
price_per_night = float(input())
expenses_percent = int(input())

overnights_cost = nights * price_per_night
if nights > 7:
    overnights_cost *= 0.95

expenses = budget * expenses_percent / 100
total_cost = expenses + overnights_cost
diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")