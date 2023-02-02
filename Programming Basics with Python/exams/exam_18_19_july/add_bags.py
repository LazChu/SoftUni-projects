bags_price = float(input())
weight = float(input())
days_till_trip = int(input())
bags = int(input())

if weight < 10:
    price = bags_price * 0.20
elif 10 <= weight <= 20:
    price = bags_price * 0.50
else:
    price = bags_price

if days_till_trip > 30:
    price *= 1.10
elif 7 <= days_till_trip <= 30:
    price *= 1.15
elif days_till_trip < 7:
    price *= 1.40

total_price = price * bags

print(f"The total price of bags is: {total_price:.2f} lv. ")