guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_person *= 0.85
elif 15 < guests <= 20:
    price_per_person *= 0.80
elif guests > 20:
    price_per_person *= 0.75

cake = budget * 0.10
cost = guests * price_per_person
total_cost = cost + cake
diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")