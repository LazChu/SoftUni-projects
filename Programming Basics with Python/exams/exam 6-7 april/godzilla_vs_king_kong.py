movie_budget = float(input())
statists = int(input())
costume_price = float(input())

decor = movie_budget * 0.10
costumes_total = statists * costume_price

if statists > 150:
    costumes_total *= 0.90

movie_cost = costumes_total + decor
diff = abs(movie_budget - movie_cost)
if movie_cost > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print('Action!')
    print(f"Wingard starts filming with {diff:.2f} leva left.")
